import caiwu
import payment
import re


kemu_P = payment.kemu_P('1.15', '垃圾处理费', 100)
print(kemu_P.num, kemu_P.name, kemu_P.value)
kemu_P.time = 20191219
kemu_P.beizhu = '李洪翔南昌出差12.19'
print(kemu_P.time, kemu_P.beizhu)



budget = caiwu.budget(1)
# print(budget.key, budget.kemus)
budget.Addkemu(0)
budget.Addkemu(1, '1.1.4', '垃圾处理费')
budget.Addkemu(-1, '', '垃圾处理费')
budget.Addkemu(1, '1.14', '垃圾处理费')
budget.fixkemu('垃圾处理费', 100)

for i in budget.kemus:
    # print(i.num, i.name, i.value, i.N)
    pass

payment = payment.payment()
payment.New(budget)
for i in payment.budget_P.kemus:
    print(i.num, i.name, i.value, i.N)
    pass
payment.Addpayment('垃圾处理费', 100, 20191219, '李洪翔南昌出差12.19')
print(payment.kemu_Ps[0].name, payment.kemu_Ps[0].value, payment.kemu_Ps[0].time, payment.kemu_Ps[0].beizhu)
for i in payment.budget_P.kemus:
    print(i.num, i.name, i.value, i.N)
    pass


# print(budget.names, budget.values)

# print(budget.key, budget.kemus[0].num, budget.kemus[0].name)
# print(dir(budget))

