import os
import show
def sort():
    show()
    # 判断文件是否存在
    if os.path.exists(r"E:\p1\student.txt"):
        with open("E:\p1\student.txt","r"):as file:
        # 读取全部内容
        student_old = file.readlins()
        student_new=[]
        for list in student_old:
            d=dict(eval(list))
            student_new.append(d)
        else:
            return
        ascORdesc = input("请选择（0升序；1降序：）")
        if ascORdesc=="0":
            ascORdescBool=False
        elif ascORdesc=="1":
            ascORdescBool = True
        else:
            print("您输入有误，请重新输入！")
            sort()
        mode=input("请选择排序方式(1按英语成绩排序；2按Python成绩排序；3按c语言成绩排序，0按总成绩排序)")
        if mode =="1":
            student_new.sort(key=lambda x:x["english"],reverse=ascORdesc)
        if mode == "2":
            student_new.sort(key=lambda x: x["python"], reverse=ascORdesc)
        if mode == "3":
            student_new.sort(key=lambda x: x["c"], reverse=ascORdesc)
        if mode == "0":
            student_new.sort(key=lambda x: x["english"]+ x["python"]+ x["c"],reverse=ascORdescBool)
        else:
            print("您的输入有误，请重新输入！")
            sort()
        #     显示排序结果
        show_student(student_new)