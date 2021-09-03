'''
首先，获取文件夹中所有文件名称，用 os.path.join() 函数拼接出要移动到的目标地址。

然后，使用 os.path.exists() 函数判断目标文件夹是否存在，不存在用 os.mkdir() 创建文件夹。

再者，使用 os.path.isdir() 函数判断是否为文件夹。

最后，当不是文件夹时，使用 shutil.move() 函数移动。
'''
# os 模块可用于文件处理操作，os 模块是Python的内置模块，不需要安装可以直接导入。
import os 
# 要想移动文件，我们需要导入Python中另一个内置的模块 shutil ，然后使用 shutil.move() 函数来对文件进行移动。
import shutil

# 获取所有文件的名称，需要使用 os 调用 listdir()函数。
# os.listdir() 函数中要求传入参数文件夹路径。
downloadPath = r"C:\Users\dandan\Pictures"
# FIXME 使用 os.listdir() 函数获取文件名后，返回一个列表，列表中的每个元素是图片文件夹中的文件。
allItems = os.listdir(downloadPath)
print(allItems)

for item in allItems:
    # 使用 os.path.splitext() 函数就能对文件进行分隔操作。
    # os.path.splitext() 函数中要传入待分隔文件，例如："主持人_试音.mp3"。
    # 通过文件后缀名判断文件类型是不区分大小写的，.mp3和.MP3都表示音频文件。为了解决这个问题，我们可以对文件后缀名使用 lower() 函数。
    extension = os.path.splitext(item)[1].lower()
    # print(os.path.splitext(item))
        # FIXME 使用 os.path.splitext() 函数对文件进行分隔后，返回的是一个元组。
        # 如：对文件"主持人_试音.mp3"进行分隔后，输出的是 ('主持人_试音', '.mp3')。
        # 元组的第一项是文件名称，元组的第二项是文件后缀名。
    # 根据后缀判断文件类型，并输出文件名和文件类型
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
    # 完成了文件分类后，要想办法把文件移动到对应的文件夹中。
    # 在移动文件之前，我们首先需要确认文件的移动路径。
    # 在代码中，使用 os.path.join() 函数来拼接每个分类文件夹的路径。
    # 该函数在合并时，会根据操作系统的不同，在路径之间添加合适的路径分隔符
    targetPath = os.path.join(downloadPath, "其他文件") # target = r"C:\Users\Administrator\Pictures\其他文件"
    # FIXME 此处只是拼接了这样一个路径，并不会生成相应的文件夹。

    # 确定了每个文件需要移动的目标文件夹，那么在移动前还需要确定目标文件夹是否存在。
    # 得到了目标文件夹的路径后，我们可以使用 os.path.exists() 函数来判断该文件夹是否已经存在。
    # os.path.exists() 函数接受一个路径字符串作为参数，当该路径的文件夹存在时，返回True，不存在时，则返回False。
    if not os.path.exists(targetPath):
        # 如果文件夹不存在，我们需要先创建文件夹，再移动文件。
        # 创建文件夹可以使用 os.mkdir() 函数：将要创建的文件夹路径作为参数传入函数中即可。
        os.mkdir(targetPath)

    # 为了避免将文件夹移动到其他文件中，我们需要先判断该文件是否是文件夹，不是文件夹再移动。
    # 我们先使用 os.path.join() 函数拼接出文件目前所在路径，也就是使用下载文件夹的路径和文件名进行合并。
    itemPath = os.path.join(downloadPath, item)
    # 将文件路径传入 os.path.isdir() 函数中，由于该函数返回的是布尔数。我们可以使用 if 语句进行判断，在程序判断 itemPath 不是一个文件夹的时候，使用 shutil.move() 函数将itemPath路径的文件移动到targetPath路径的文件夹下。
    if not os.path.isdir(itemPath):
        # shutil.move() 函数可以用来移动文件或文件夹。它接收两个参数，第一个参数是要移动的文件（夹）路径，第二个参数是目标文件（夹）的路径。
        shutil.move(itemPath, targetPath)
