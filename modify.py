import os
def modify():
    # show()
    # 判断文件是否存在
    if os.path.exists(r"E:\p1\student.txt"):
        # 打开文件
        with open(r"E:\p1\student.txt","r",)as rfile:
            # 读取全部内容
            student_old = rfile.readlines()
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    # 以只写模式打开文件
    with open(r"E:\p1\student.txt","w")as wfile:
        for student in student_old:
            d=dict(eval(student))
            # 是否是修改的学生
            if d["id"]==studentid:
                print("找到了这名学生可以修改信息")
                while True:
                    try:
                        d["name"]=input("请输入姓名：")
                        d["english"]=int(input("请输入英语成绩"))
                        d["python"]=int(input("请输入python成绩"))
                        d["c"]=int(input("请输入c成绩"))
                    except:
                        print("您输入有误请重新输入")
                    else:
                        break
                        # 将字典转化为字符串
                        student=str(d)
                        # 将修改的东西写入到文件
                        wfile.write(student + "\n")
                        print("修改成功")
            else:
                # 将未修改的信息写入到文件中
                wfile.write(student)
                mark=input("是否继续修改其他学生的信息？(y/n)")
                if mark=="y":
                    # 重新执行修改操作
                    modify()


