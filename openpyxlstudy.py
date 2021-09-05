'''
要使用Python对Excel表格进行读取，我们需要安装一个用于读取数据的工具 openpyxl 。openpyxl 是一个用于读、写Excel文件的开源模块。
安装openpyxl非常简单，在终端中输入代码：pip install openpyxl即可。
如果在自己电脑上安装不上或安装缓慢，可在命令后添加如下配置进行加速：
pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple/
'''
import openpyxl
# 在安装和导入openpyxl之后，读取指定路径的工作簿需要使用函数：openpyxl.load_workbook()。
# 工作簿文件的路径需要作为函数参数传入。
wb = openpyxl.load_workbook("文件路径")

# 得到了工作表名称后，我们可以通过在变量wb后添加中括号[ ]和工作表名称的方式来获得对应的工作表对象。
orderSheet = wb["工作表名称"]
# 如果事先不知道工作簿内有哪些工作表，我们可以通过访问工作簿的 .sheetnames 属性来获取一个包含所有工作表名称的列表。
# 具体操作为在变量wb之后添加代码 .sheetnames 。
# print(wb.sheetnames)

