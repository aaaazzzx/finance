# 用于财务父类

class Caiwu():
    '''用于给项目提供财务数据'''

    def __init__(self,key,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0):
        self.key = key
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
        self.其他费 = {'name': '其他费', 'value': p, '备注': '', 'key':key}
        self.间接费 = {'name': '间接费', 'value': q, '备注': '', 'key':key}
        self.绩效支出 = {'name': '绩效支出', 'value': r, '备注': '', 'key':key}

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


