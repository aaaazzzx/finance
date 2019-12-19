a_list = ['a','b','c','c','d','c']
b_list = [1,1,1,1,1,1]
find = 'c'
print('重复元素出现的位置索引分别是 = ',[j for j,v in enumerate(a_list) if v==find])
aaa = [j for j,v in enumerate(a_list) if v==find]
if aaa != []:
    print('有重复')
else:
    print('无重复')