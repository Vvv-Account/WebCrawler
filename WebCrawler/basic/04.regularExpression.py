import re

s1="18809090000是我的手机号，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗？"
s2="我的手机号是18809090000，你记住了吗？我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗？"

# match - 从字符串开头开始匹配(匹配第一个匹配项)
result_1 = re.match(r"1[3-9]\d{9}", s1)
print(result_1.group())
print(result_1.span())
print(result_1.start())
print(result_1.end())

# search - 从任意位置开始，搜索第一个匹配项
result_2 = re.search(r"1[3-9]\d{9}", s2)
print(result_2.group())
print(result_2.span())


# findall - 从任意位置开始，搜索所有匹配项
result_3 = re.findall(r"1[3-9]\d{9}", s1)
print(result_3)
 

