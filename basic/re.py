import re

# . ^ $ * + ? {m} {m, n} [] | \d \D \s ()
# ^$ 空行
# .*? 不使用贪婪模式
# * 本身会尽可能长的匹配

# * 0 次到多次
# + 1 次到多次
# \? 0 次或者一次
# \d 和 [0-9]+ 一样

# match 匹配之前必须清楚的知道字符串是什么样子的

p = re.compile(r'(\d+)-(\d+)-(\d+)')

# ----------- 匹配功能，完全匹配 -----------
# print(p.match('2018-05-10').group(1))
# year, month, day = p.match('2018-05-10').groups()
# print(year, month, day)

# ----------- 搜索功能，包含匹配 -----------
print(p.search('aa2018-05-10bb'))

# ----------- 替换 sub -----------
print(re.sub('c', '*', 'abcd'))
phone = '123-31314 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
p3 = re.sub(r'\D', '', p2)
