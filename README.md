# WebCrawler
#爬取高分电影-TOP100 

🎬 TMDB 高分电影 TOP100 爬虫 一个基于 Python + lxml + XPath 的实战爬虫项目，从 The Movie Database（TMDB）抓取高分电影 TOP100 的完整信息，最终将电影详情信息提取为结构化CSV文件

---
## 📋 项目特点

- 🎯 **目标明确**：爬取 TMDB 评分最高的 100 部电影（Top Rated）
- 🔍 **解析方式**：全链路使用 XPath 定位元素，训练手写路径的能力
- 📊 **数据丰富**：电影名、年份、上映日期、类型、时长、评分、语言、导演、编剧、标语、简介……共计 11 个维度
- 💾 **持久化存储**：数据保存为 CSV，可直接用于数据分析
- 📄 **分页处理**：支持多页爬取（前 5 页），每页 20 条，共 100 条
- ⏰ **自动格式化**：电影时长自动转换为分钟（如 "2h 30m" → 150 分钟）
- 🛡️ **数据清洗**：自动处理空值、去除特殊字符，保证数据完整性
- 🔄 **请求管理**：支持 GET/POST 混合请求，适配 TMDB 分页机制
- ⚡ **高效稳定**：设置超时保护，避免请求卡死
  
---
## 📦 安装依赖

pip install requests lxml

---
## 🛠️ 技术栈

库 用途
requests 发送 HTTP 请求，获取网页源码
lxml 解析 HTML，提供 XPath 支持
re（正则） 辅助数据清洗日期、时长等字段中的特定格式
csv 将字典数据写入 CSV 文件

---
## 📁 项目结构
```
WebCrawler/                          # 项目根目录
├── .venv/                           # Python 虚拟环境
├── basic/                           # 源代码
│   ├── csv_data/                    # CSV 数据文件夹
│   |    ├── 01.csv                  # CSV 文件格式样式
│   |    ├── movie_list.csv          # 爬取top100电影数据
│   |   └── movie_list2.csv          # 正则清洗数据后的电影数据
|   ├─resources/                     # 资源文件目录
│     ├── 01.basicCode.py              
│     ├── 02.webAnalysis.py
│     ├── 03.csvBasic.py
│     ├── 04.regularExpression.py
│     ├── text.py                    #main
└── External Libraries               # 外部库（PyCharm 显示）
```
