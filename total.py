import os
def total():
    if os.path.exists(r"E:\p1\student.txt"):
        # 打开文件
        with open(r"E:\p1\student.txt","r")as rfile:
            # 读取全部内容
            sorted_old=rfile.readlines()
            if student_old:
                # 统计学生人数
                print("一共有%d名学生！%len(syudent_old)")
            else：
            print("还没有录入学生信息")
    else:
        print("暂未保存数据信息，，，")