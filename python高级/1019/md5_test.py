#coding=utf-8
import hashlib 

m = hashlib.md5()#创建hash对象  



m.update('lixianzhu') #更新哈希以字符串参数


print m.digest()  #返回摘要，作为二进制数据字符串值

print m.hexdigest() #返回十六进驻数字字符串


