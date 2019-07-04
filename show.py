import os

def shoe():
    student_new=[]
    # 判断文件是否存在
    if os.path.exists(r"E:\p1\student.txt"):
        # 打开文件
        with open(r"E:\p1\student.txt","r")as rfile:
            # 读取全部内容
            student_old=rfile.readlines()
        for list in student_old:
            # 将找到学生的信息保存到列表
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息。。。")
