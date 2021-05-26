# -*- codeing =utf-8 -*-
# @Time : 2021/5/26 11:25
# @Author : 小洛
# @File : hashlib_加密.py
# @Software: PyCharm

#引入模块你
import hashlib
#随机产生一串数字
a = hash("a")
print(a)

#--------md5加密---128位
m = hashlib.md5()

m.update(b"hell word")   #将字符串交个md5加密
print(m.hexdigest())

m.update("欢迎".encode("utf-8"))     #中文要以"utf-8"解码

#print(m.digest())       #消化b

print(m.hexdigest())    #转换成十六进制数


#拼接
m2 = hashlib.md5()
m2.update("hell word欢迎".encode("utf-8"))
print(m2.hexdigest())

#密文---- 明文
'''
alipy  hell word a166985348271b3368e596d8d0bb92fc --密文

jd     hell word a166985348271b3368e596d8d0bb92fc --密文

weixin   hell word  a166985348271b3368e596d8d0bb92fc --密文

撞库   穷举

脱库

加盐

hell word  -->md5  a166985348271b3368e596d8d0bb92fc
'''


#-------SHA-1加密----产生一个160位消息摘要
s1 = hashlib.sha1()
s1.update(b"alex")
print(s1.hexdigest())


s2 = hashlib.sha3_256()
s2.update(b"alex")
print(s2.hexdigest())


s3 = hashlib.sha3_224()
s3.update(b"alex")
print(s3.hexdigest())


s4 = hashlib.sha384()
s4.update(b"alex")
print(s4.hexdigest())


#设置密码
s5 = hashlib.sha512()
s5.update(b"alex")
ne = s5.hexdigest()
print(s5.hexdigest())

mn = hashlib.sha512()
print("请输入")
n = str(input(">>:").strip())
mn.update(n.encode("utf-8"))
n1 = mn.hexdigest()
print(n1)

if n1==ne:
    print(n1)
    print("输入正确")


# if hasattr(ne,str(n1)):
#     func = getattr(ne,str(n1))
#     print(func)


