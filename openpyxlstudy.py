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

# 要获取工作表中指定的单元格对象，我们可以通过在中括号[ ]内填入列号和行号的方式去获取。
print(orderSheet["A1"]) # <Cell '工作表名称'.A1>
# 输出单元格对象并没有输出单元格内的值。要访问单元格里的值，我们可以在单元格对象后加一个 .value 。
print(orderSheet["A1"].value)
# 若单元格中包含公式，现有方式读取出的值是公式本身。若需要读取公式计算后的值，要在读取工作簿的代码部分，传入一个参数： data_only=True ，便可以得出公式计算后的值了。
wb = openpyxl.load_workbook("文件路径", data_only=True)
print(orderSheet["A1"].value)
# 要对整个工作表的每一行数据进行浏览查询，可以使用for循环对工作表对象的行属性（rows）进行遍历。具体代码为 for rowData in orderSheet.rows:
# 这样程序就会以从上到下的顺序，逐个获取到指定工作表内的每一行数据。
# 可以从运行结果中看到，读取出的每一行数据是由单元格对象组成的元组。
for rowData in orderSheet.rows:
    print(rowData)
    # 行遍历的输出结果，是由单元格对象组成的元组。在元组中要定位到具体的列需要用索引。
    productName = rowData[2].value
    print(productName)

    # 如果要定位的列数字比较大，比如在第I列，通过肉眼观察来确定索引略显繁琐。这时，可以使用函数：openpyxl.utils.cell.column_index_from_string()，来获取列号对应的数字，比如传入参数“E”就会获取到数字5，表示“E”列是第5列。这个数字减一即可得到对应的索引。
    priceIndex = openpyxl.utils.cell.column_index_from_string("I") - 1
    price = rowData[priceIndex].value
    print(price)