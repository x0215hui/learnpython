import os
# 使用os.getcwd()函数可以用来获取当前程序的工作目录。
print(os.getcwd())
# 要修改程序运行时的工作目录，需要使用os.chdir()函数。
# os.chdir("targetdir")
# 刚才我们已经知道，若待处理文件夹的绝对路径为 /Volumes/backup/照片。
# 将工作目录修改到移动硬盘路径/Volumes/backup/后，此文件夹的相对路径也就变成“照片”了。