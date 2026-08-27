# csv操作 - 方式：
# 写
# with open("csv_data/01.csv", "w", encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n") # 写入表头
#     f.write("小王,18,男,football\n")
#     f.write("小李,18,女,Python\n")
#     f.write("张三,18,男,'Java,Python'\n")
#     f.write("张三,20,男,Go\n")
#
# with open("csv_data/01.csv", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# 文件操作的原始方式

import csv
with open("csv_data/01.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    writer.writeheader() # 写入表头
    writer.writerows([{"姓名": "小王", "年龄": "18", "性别": "男", "爱好": "football"},
                      {"姓名": "小李", "年龄": "18", "性别": "女", "爱好": "Python"},
                      {"姓名": "张三", "年龄": "18", "性别": "男", "爱好": "Java,Python"},
                      {"姓名": "李四", "年龄": "20", "性别": "男", "爱好": "Go"}])

with open("csv_data/01.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
