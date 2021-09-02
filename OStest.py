# os 模块可用于文件处理操作，os 模块是Python的内置模块，不需要安装可以直接导入。
import os 
# 获取所有文件的名称，需要使用 os 调用 listdir()函数。
# os.listdir() 函数中要求传入参数文件夹路径。
downloadPath = r"C:\Users\Administrator\Pictures"
# 使用 os.listdir() 函数获取文件名后，返回一个列表，列表中的每个元素是图片文件夹中的文件。
allItems = os.listdir(downloadPath)
print(allItems)
for item in allItems:
    # 使用 os.path.splitext() 函数就能对文件进行分隔操作。
    # os.path.splitext() 函数中要传入待分隔文件，例如："主持人_试音.mp3"。
    extension = os.path.splitext(item)[1]
    # print(os.path.splitext(item))
        # 使用 os.path.splitext() 函数对文件进行分隔后，返回的是一个元组。
        # 如：对文件"主持人_试音.mp3"进行分隔后，输出的是 ('主持人_试音', '.mp3')。
        # 元组的第一项是文件名称，元组的第二项是文件后缀名。
    # print(extension)
    # 根据后缀判断视频文件，并输出文件名和文件类型
    if extension in [".jpg", ".jpeg", ".gif", ".png", ".bmp"]:
        print(f"{item} 图片文件")
    elif extension in [".avi", ".mp4", ".wmv", ".mov", ".flv"]:
        print(f"{item} 视频文件")    
    elif extension in [".wav", ".mp3", ".mid", ".ape", ".flac"]:
        print(f"{item} 音频文件")
    elif extension in [".pdf"]:
        print(f"{item} PDF文件")
    elif extension in [".docx", ".doc"]:
        print(f"{item} Word文件")
    elif extension in [".xlsx", ".xls"]:
        print(f"{item} Excel文件" )
    elif extension in [".pptx", ".ppt"]:
        print(f"{item} PPT文件")
    else:
        print(f"{item} 其他文件")