# 支出及账面
import caiwu

class kemu_P(caiwu.kemu):
    '''以财务的kemu子类'''

    def __init__(self,num, name, value, N=0):
        '''初始化父类属性'''
        super().__init__(num, name, value, N)

        '''自有属性'''
        self.time = 20190101
        self.beizhu = ''

class payment():
    '''与budget类似'''

    def __init__(self):
        # 总统计表
        self.budget_P = caiwu.budget(1)

        # 各开支项目
        self.kemu_Ps = []

        # 用于统计时间序列
        self.times = []

        # 用于统计科目序列（指按时间排序的支出科目）
        self.names = []

        # 用于统计数值序列（指按时间排序的支出科目）
        self.values = []

    def New(self,budget):
        # 新建支出时，应当导入预算中的科目及相关信息
        self.budget_P = budget

        # 将其中关键字修正，0表示预算，-1表示支出
        self.budget_P.key = -1

        # 将其中预算调整为0
        for i in self.budget_P.names:
            self.budget_P.fixkemu(i, 0)


    def Addpayment(self, name, value, time, beizhu):
        '''增加支出项目'''
        # 根据名称找到项目序号
        num = 0
        for i in range(len(self.budget_P.names)):
            if name == self.budget_P.names[i]:
                num = self.budget_P.nums[i]
        # 输入基本信息
        kemu_p = kemu_P(num, name, value)
        # 输入时间及备注
        kemu_p.time = time
        kemu_p.beizhu = beizhu
        self.kemu_Ps.append(kemu_p)

        # 重新统计支出
        self.times = self.tongjitimes()
        self.names = self.tongjinames()
        self.values = self.tongjivalues()

        self.jisuan()

# ========= 内部调用区 ===============

    def tongjitimes(self):
        times= []
        for i in self.kemu_Ps:
            times.append(i.time)
        return times

    def tongjinames(self):
        names = []
        for i in self.kemu_Ps:
            names.append(i.name)
        return names

    def tongjivalues(self):
        values= []
        for i in self.kemu_Ps:
            values.append(i.value)
        return values

    # ================计算区===========

    def jisuan(self):
        names = self.budget_P.names
        values = []
        for i in names:
            '''统计支出，并保存'''
            bbb = 0

            '''查找list中指定的相（可重复）返回位置'''
            find = i
            aaa = [j for j, v in enumerate(self.names) if v == find]
            if aaa != []:
                for k in aaa:
                    # 将各项支出累加
                    bbb = bbb + self.values[k]
            else:
                bbb = 0
            # 按序号保存各项支出之和
            values.append(bbb)

        # 将支出保存至总统计表中
        for i in range(len(names)):
            self.budget_P.fixkemu(names[i], values[i])

