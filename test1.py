import caiwu
import re


budget = caiwu.budget(1)
# print(budget.key, budget.kemus)
budget.Addkemu(0)
budget.Addkemu(1, '1.1.4', '垃圾处理费')
budget.Addkemu(-1, '', '垃圾处理费')
budget.Addkemu(1, '1.14', '垃圾处理费')
budget.fixkemu('垃圾处理费', 100)

for i in budget.kemus:
    print(i.num, i.name, i.value, i.N)
    pass


# print(budget.names, budget.values)

# print(budget.key, budget.kemus[0].num, budget.kemus[0].name)
# print(dir(budget))

