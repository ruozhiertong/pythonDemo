import csv
import random
import time

# 3个属性下的初始值
x_value = 0
total_1 = 1000
total_2 = 1000

# 生成的csv数据的头部标签
fieldnames = ["x_value", "total_1", "total_2"]

# 写入文件头部标签, 因文件打开方式是w, 故而会覆盖掉前面的内容从头开始写
with open('data_6.csv', 'w') as csv_file:
    # 以字典的方式写入文件
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # 写入头部信息: x_vale, total_1, total_2的标签信息
    csv_writer.writeheader()

# 永真循环, 程序每隔一秒(time.sleep(1))就写入一次数据
while True:
    with open('data_6.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # 因为创建的是DictWriter(以字典的方式写入文件), 因此创建的数据也是字典格式的, 键是列的标签, 值是对应标签上的数据
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }
        # 写入一行信息
        csv_writer.writerow(info)
        # 打印刚刚写入的信息
        #print(x_value, total_1, total_2)
        # 时间往后移一天
        x_value += 1
        # 两个value值随机变动
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
    # 程序等待1秒钟
    time.sleep(1)
