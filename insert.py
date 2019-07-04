def save(student):
    try:
        # 以追加模式打开
        student_txt = open(r"E:\p1\student.txt","a")
    except Exception as e:
        student_txt=open(r"E:\p1\student.txt","w")
    for info in student:
        # 按行存储添加换行符
        student_txt.write(str(info)+"\n")
    #     关闭文件
    student_txt.close()

def insert():
    # 保存学生消息列表
    studentList = []
    # 是否继续添加
    mark=True
    while mark:
        id = input("请输入ID(如1001)：")
        # 如果ID为空，跳出循环
        if not id :
            break
        name =input("请输入名字：")
        if not name :
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入c成绩："))
        except:
            print("输入无效，不是整形数字。。。。。。请重新录入信息")
            continue
        # 将输入学生信息保存到字典中
        student = {"id":id,"name":name,"english":english,"python":python,"c":c}
        studentList.append(student)
        inputMark = input("是否继续添加(y/n):")
        # 继续添加
        if inputMark == "y":
            mark=True
        # 不继续添加
        else:
            mark=False
    # save(studentList)
    print("学生信息录入完毕！！！")

insert()
