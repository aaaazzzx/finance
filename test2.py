import re


pattern = re.compile('^1\.[0-9]+$')
aaa = '1.2.13'
bbb = '2'
ccc = '1.3'
# 需要匹配1.3 不要1.2.13 或2
ddd = [aaa, bbb, ccc]
for i in ddd:
    if re.match(pattern, i):
        print(i)



    if i == pattern:
        print(i)
