import re
pattern = re.compile('^1.[0-9]+')

aaa = '1.2.13'
bbb = '2'
ccc = '1.3'
ddd = [aaa, bbb, ccc]
for i in ddd:
    print(i)
    if i == pattern:
        print(i)
