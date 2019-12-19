# 用于财务父类
import re

class kemu():
    '''科目，用于保存最基础的数据'''

    def __init__(self, num, name, value, add=0):
        self.num = num    # 序号 1.2.3
        self.name = name
        self.value = value
        self.N = add      # 编号  10203

class budget():
    '''用于给项目提供财务数据'''

    def __init__(self, key):    # ,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0
        self.key = key

        # 用于存放预算科目
        self.kemus = []

        # 用于统计项目序号
        self.nums = []     # 序号 1.2.3

        # 用于统计项目名称
        self.names = []

        # 用于统计项目名称
        self.values = []

        # 用于统计编号
        self.Ns = []

    def Addkemu(self, key, num='', name='', value=0):
        '''用于增加科目'''

        if key == 0:
            # 默认添加的项目
            self.kemus.append(kemu('0', '总费用', 0))
            self.kemus.append(kemu('1', '直接费用', 0))
            self.kemus.append(kemu('1.1', '设备费', 0))
            self.kemus.append(kemu('1.1.1', '购置设备费', 0))
            self.kemus.append(kemu('1.1.2', '试制设备费', 0))
            self.kemus.append(kemu('1.1.3', '设备改造与租赁费', 0))
            self.kemus.append(kemu('1.2', '材料费', 0))
            self.kemus.append(kemu('1.3', '测试化验加工费', 0))
            self.kemus.append(kemu('1.4', '燃料动力费', 0))
            self.kemus.append(kemu('1.5', '差旅费/会议费、国际合作与交流费', 0))
            self.kemus.append(kemu('1.6', '出版/文献/信息传播/知识产权事务费', 0))
            self.kemus.append(kemu('1.7', '劳务费', 0))
            self.kemus.append(kemu('1.8', '专家咨询费', 0))
            self.kemus.append(kemu('1.9', '其他费用', 0))
            self.kemus.append(kemu('2', '间接费', 0))
            self.kemus.append(kemu('2.1', '绩效支出', 0))

            self.kemus = self.paixu()  # 增加科目后应当排序

            # 重新统计
            self.nums = self.tongjinum()     # 序号 1.2.3
            self.names = self.tongjiname()
            self.values = self.tongjivalue()
            self.Ns = self.tongjiN()

            # 添加提示
        elif key == 1:
            # 增加项目
            self.kemus.append(kemu(num, name, value))

            self.kemus = self.paixu()    # 增加科目后应当排序

            # 重新统计
            self.nums = self.tongjinum()     # 序号 1.2.3
            self.names = self.tongjiname()
            self.values = self.tongjivalue()
            self.Ns = self.tongjiN()
            # 添加提示

        elif key == -1:
            # 删除项目
            i = self.names.index(name)
            del self.kemus[i]

            self.kemus = self.paixu()  # 增加科目后应当排序

            # 重新统计
            self.nums = self.tongjinum()     # 序号 1.2.3
            self.names = self.tongjiname()
            self.values = self.tongjivalue()
            self.Ns = self.tongjiN()

    def fixkemu(self, name, value):
        # 预算调整

        i = self.names.index(name)
        self.kemus[i].value = value

        for i in range(3):
            self.jisuan()

        # 重新统计
        self.nums = self.tongjinum()     # 序号 1.2.3
        self.names = self.tongjiname()
        self.values = self.tongjivalue()
        self.Ns = self.tongjiN()

# ==============内部调用区======================

    def paixu(self):
        n = len(self.kemus)
        kemus = []
        aaa = []
        for i in self.kemus:
            j = i.num
            if j.count('.') < 1:
                kemus.append(int(j) * 10000)
                i.N = int(j) * 10000
            elif j.count('.') == 1:
                sb1 = int(re.findall('\d+', j)[0])*10000
                sb2 = int(re.findall('\d+', j)[1])*100
                kemus.append(sb1 + sb2)
                i.N = (sb1 + sb2)
            elif j.count('.') == 2:
                sb1 = int(re.findall('\d+', j)[0]) * 10000
                sb2 = int(re.findall('\d+', j)[1]) * 100
                sb3 = int(re.findall('\d+', j)[2])
                kemus.append(sb1 + sb2 + sb3)
                i.N = sb1 + sb2 + sb3
        Kemus = sorted(kemus)
        for i in Kemus:
            j = kemus.index(i)
            aaa.append(self.kemus[j])
        return aaa

    # ======== 统计区 ========

    def tongjinum(self):
        # 用于统计所有项目序号
        nums = []     # 序号 1.2.3
        for i in self.kemus:
            nums.append(i.num)
        return nums

    def tongjiname(self):
        # 用于统计所有项目名称
        names = []
        for i in self.kemus:
            names.append(i.name)
        return names

    def tongjivalue(self):
        # 用于统计所有项目值
        values = []
        for i in self.kemus:
            values.append(i.value)
        return values

    def tongjiN(self):
        # 用于统计所有项目编号
        Ns = []
        for i in self.kemus:
            Ns.append(i.value)
        return Ns

    # ======== 计算区 ========

    def jisuan(self):
        # 用于计算总值
        Ns = self.Ns    # 编号 10203
        nums = self.nums    # 序号 1.2.3
        for i in range(len(self.kemus)):
            kemu = self.kemus[i]
            N = kemu.num
            # print(N)
            if N == '0':
                # print(self.kemus[i].num) 开始匹配总费用
                N1 = nums.index('1')
                N2 = nums.index('2')
                self.kemus[i].value = self.kemus[N1].value + self.kemus[N2].value    # 0总费用等与序号1和2
            if N == '1':
                # print('开始匹配直接费用')
                self.kemus[i].value = 0
                for j in range(len(self.kemus)):
                    if re.match('^1\.[0-9]+$', self.kemus[j].num):
                        # print(self.kemus[j].num)
                        self.kemus[i].value = self.kemus[i].value + self.kemus[j].value
            if N == '1.1':
                # print('开始匹配设备费用')
                self.kemus[i].value = 0
                for j in range(len(self.kemus)):
                    if re.match('^1\.1\.[0-9]+$', self.kemus[j].num):
                        # print(self.kemus[j].num)
                        self.kemus[i].value = self.kemus[i].value + self.kemus[j].value

    '''
        self.总费用 = {'name': '总费用', 'value': a, '备注': '', 'key':key}
        self.直接费用 = {'name': '直接费用', 'value': b, '备注': '', 'key':key}
        self.设备费 = {'name': '设备费', 'value': c, '备注': '', 'key':key}
        self.购置设备费 = {'name': '购置设备费', 'value': d, '备注': '', 'key':key}
        self.试制设备费 = {'name': '试制设备费', 'value': e, '备注': '', 'key':key}
        self.设备改造与租赁费 = {'name': '设备改造与租赁费', 'value': f, '备注': '', 'key':key}
        self.材料费 = {'name': '材料费', 'value': g, '备注': '', 'key':key}
        self.测试化验加工费 = {'name': '测试化验加工费', 'value': h, '备注': '', 'key':key}
        self.燃料动力费 = {'name': '燃料动力费', 'value': i, '备注': '', 'key':key}
        self.差旅费 = {'name': '差旅费', 'value': j, '备注': '', 'key':key}
        self.会议费 = {'name': '会议费', 'value': k, '备注': '', 'key':key}
        self.国际合作与交流费 = {'name': '国际合作与交流费', 'value': l, '备注': '', 'key':key}
        self.出版等 = {'name': '出版/文献/信息传播/知识产权事务费', 'value': m, '备注': '', 'key':key}
        self.劳务费 = {'name': '劳务费', 'value': n, '备注': '', 'key':key}
        self.专家咨询费 = {'name': '专家咨询费', 'value': o, '备注': '', 'key':key}
        self.其他费 = {'name': '其他支出', 'value': p, '备注': '', 'key':key}
        self.间接费 = {'name': '间接费用', 'value': q, '备注': '', 'key':key}
        self.绩效支出 = {'name': '绩效支出', 'value': r, '备注': '', 'key':key}
    '''

    '''
    def Change(self,a,b,c,d,e,f,g,h):
        #  用于修改财务数据
        self.总费用['value'] = a
        self.直接费用['value'] = a
        self.设备费['value'] = a
        self.购置设备费['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
        self.总费用['value'] = a
    '''


