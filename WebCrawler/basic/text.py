import requests
import re
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE = "csv_data/movie_list2.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"

# 获取电影年份
def get_movie_year(movie_years):
    if not movie_years:
        return None
    return movie_years[0].replace("(", "").replace(")", "")

# 获取电影上映日期
def get_movie_public_data(movie_datas):
    movie_data = movie_datas[0].strip() if movie_datas else None
    if not movie_data:
        return None
    data_match = re.search(r"\d{4}-\d{2}-\d{2}", movie_data)
    return data_match.group() if data_match else None

# 获取电影时长
def get_movie_cost_time(movie_cost_times):
    if not movie_cost_times:
        return 0
    movie_cost_time = movie_cost_times[0].strip()
    if not movie_cost_time:
        return 0
    h_res = re.search(r"(\d+)h", movie_cost_time)
    m_res = re.search(r"(\d+)m", movie_cost_time)
    h = int(h_res.group(1) if h_res else 0)
    m = int(m_res.group(1) if m_res else 0)
    return h*60+m


# 解析数据，获取电影列表
def get_movie_info(movie_info_url):
    # 1. 发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url, timeout=60)
    print(f"发送请求{movie_info_url}, 获取电影详情数据...")

    # 2. 解析数据，获取电影详情
    movie_document = html.fromstring(movie_response.text)
    movie_names = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")  # 电影名称
    movie_years = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")  # 电影年份
    movie_datas = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")  # 电影数据
    movie_tags = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")  # 电影标签
    movie_cost_times = movie_document.xpath(
        "//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")  # 电影时长
    movie_scores = movie_document.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")  # 电影评分
    movie_languages = movie_document.xpath(
        "//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")  # 电影语言
    movie_directors = movie_document.xpath(
        "//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")  # 电影导演
    movie_authors = movie_document.xpath(
        "//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")  # 电影作者
    movie_slogans = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")  # 电影宣创语
    movie_descriptions = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")  # 电影简介

    # 3. 返回电影详情
    movie_info = {
        "电影名称": movie_names[0].strip() if movie_names else None,
        "电影年份": get_movie_year(movie_years),
        "电影数据": get_movie_public_data(movie_datas),
        "电影标签": ",".join(movie_tags) if movie_tags else None,
        "电影时长": get_movie_cost_time(movie_cost_times),
        "电影评分": movie_scores[0].strip() if movie_scores else None,
        "电影语言": movie_languages[0].strip() if movie_languages else None,
        "电影导演": ",".join(movie_directors) if movie_directors else None,
        "电影作者": ",".join(movie_authors) if movie_authors else None,
        "电影宣创语": movie_slogans[0].strip() if movie_slogans else None,
        "电影简介": movie_descriptions[0].strip() if movie_descriptions else None,
    }
    return movie_info


# 保存电影数据到csv文件中
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名称", "电影年份", "电影数据", "电影标签", "电影时长", "电影评分", "电影语言", "电影导演", "电影作者", "电影宣创语", "电影简介"])
        writer.writeheader()
        writer.writerows(all_movies)


# 主函数，定义核心逻辑
def main():
    all_movies = []# 保存所有电影数据
    for page_num in range(1, 6):
        # 1.发送请求来获取高分电影榜单数据
        if page_num == 1:
           response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
           response = requests.post(TMDB_TOP_URL_2,
                                    data="air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page=" + str(page_num) + "&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-23&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                    timeout=60)
        print("发送请求，访问第" + str(page_num) + "页的数据，获取TMDB电影榜单数据...")
        # 2.解析数据，获取电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath("//div[@class='media-list-results contents']/div[@data-object-id]")
        # 3.遍历电影列表，获取电影详情
        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                # 电影详情的url
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)
        # 4.保存数据为 csv 文件
    print("获取到所有的电影数据，保存电影数据为 csv 文件")
    save_all_movies(all_movies)


if __name__ == "__main__":
    main()
