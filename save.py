


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
