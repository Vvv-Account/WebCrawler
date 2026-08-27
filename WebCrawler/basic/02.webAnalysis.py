from lxml import html

# 读取 html 文件
with open("resources/portfolio.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 解析html文本，将其转换成一个文档对象
    document = html.fromstring(html_text)

    # 解析-xpath语法
    document.xpath("")
    # /
    # //
    # .
    # [n]
    # [last()]
    # [@attr]
    # [@attr='value']
    # *
    # @*
    # text()