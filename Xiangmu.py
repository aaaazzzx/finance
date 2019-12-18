'''用于洞庭湖科技项目财务管理的父类'''
import caiwu

class Xiangmu():
    '''项目父类'''
    '''
    1.项目基本信息
    2.项目预算
    3.项目支出
    4.项目结余经费
    '''


    def __init__(self,name):
        '''初始化项目名称及基本信息'''
        self.name = name     # 项目名称
        self.qiantou = ''    # 牵头单位
        self.leibie = ''     # 项目类别
        self.fuze = ''       # 项目负责人
        self.start = 0       # 项目开始时间
        self.end = 0         # 项目结束时间

        '''初始化预算'''
        self.budget = caiwu.budget(0)

        '''初始化变更，一般为支出'''
        self.payment = []

        '''初始化经费结余'''
        # self.rest = caiwu.Caiwu(1)

    def budgetChange(self,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0):
        '''预算变更'''
        key = 0

    def paymentAdd(self,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0):
        '''支出条目增加'''
        key = 1


    def restChange(self):
        '''结余变更'''
        key = 2


