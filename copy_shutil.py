# -*- codeing =utf-8 -*-
# @Time : 2021/5/26 21:12
# @Author : 小洛
# @File : copy_shutil.py
# @Software: PyCharm


#shutil   将文件内容拷贝到另一个文件中
import shutil

#一写的形式打开文件
#shutil.copyfileobj(open("pick_time.py","r"),open("pick2_time.py","w"))

#简单
#shutil.copyfile("pick_time.py","pick2_time.py")


#copymode----拷贝权限
#shutil.copymode("pick-json_mod.py","pick2_time.py")


#拷贝状态信息----目标文件要存在
#shutil.copystat("pick-json_mod.py","pick3-json_mod.py")

#拷贝权限
#shutil.copy("pick-json_mod.py","pick5-json_mod.py")

#拷贝文件和状态信息
#shutil.copy2("pick-json_mod.py","pick5_time.py")

#将整个目录下的文件拷贝到下一及目录
#shutil.copytree("../moudule_模块","moudule_rt")



#压缩文件
#shutil.make_archive(base_name="/Users/alex/Downloads/test",format="zip",root_dir="../",owner="root")

#压缩文件

import zipfile
'''
z = zipfile.ZipFile("test_compress.zip","w")

z.write("pick_time.py")
z.close()
'''
import os
filelist = []
for root_dir,dirs,files in os.walk("moudule_模块"):
    for filename in files:
        filelist.append(os.path.join(root_dir,filename))


for i in filelist:
    print(i)


#解压

z = zipfile.ZipFile("test.zip","r")
z.extractall(path="/Users/drg/")

z.close()




















