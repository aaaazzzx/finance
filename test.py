import caiwu
import re

'''
budget = caiwu.budget(1)
print(budget.key, budget.kemus)
budget.Addkemu(-1)

for i in budget.kemus:
    print(i.num, i.name)

# print(budget.key, budget.kemus[0].num, budget.kemus[0].name)
print(dir(budget))
'''


aaa = '1.2.13'
bbb = '2'
ccc = '1.3'
ddd = [aaa, bbb, ccc]
eee = []
# print(ddd)
for i in ddd:

    if i.count('.') < 1:
        eee.append(int(i)*10000 )
    elif i.count('.') == 1:
        sb1 = int(re.findall('[0-9]+', i)[0]) * 10000
        sb2 = int(re.findall('[0-9]+', i)[1]) * 100
        eee.append(sb1 + sb2)
    elif i.count('.') == 2:
        sb1 = int(re.findall('[0-9]+', i)[0]) * 10000
        sb2 = int(re.findall('[0-9]+', i)[1]) * 100
        sb3 = int(re.findall('[0-9]+', i)[2])
        eee.append(sb1 + sb2 + sb3)

'''
Kemus = sorted(eee)
for i in Kemus:
    j = eee.index(i)
    print(j)
'''


print(eee)
