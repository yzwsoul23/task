import re
a = '宋体 SimSun黑体 SimHei微软雅黑 Microsoft YaHei微软正黑体 Microsoft JhengHei新宋体 NSimSun新细明体 PMingLiU细明体 MingLiU标楷体 DFKai-SB仿宋 FangSong楷体 KaiTi仿宋_GB2312 FangSong_GB2312楷体_GB2312 KaiTi_GB2312宋SimSuncss'
#\d 匹配一个数字字符。等价于 [0-9]
#\D 匹配一个非数字字符。等价于 [^0-9]

#提取汉字
str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", a)
print(str)

#从字符串中提取数字
totalCount = re.sub("\D", "", a)
print(totalCount)

#提取字母字符串
result = ''.join(re.findall(r'[A-Za-z0-9\ \_]', a))
print(result)
newss =''
for i in result:
    if i == ' ':
        i = ','
        newss += i
    else:
        newss += i

print(newss)