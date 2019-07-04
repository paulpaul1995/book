
import os
def delete():
    # 标记是否循环
    mark =True
    #
    while mark:
        studentsId=input("请输入要删除的学生id：")
        # 判断是否输入要删除的学生
        if studentsId is not "":
            # 判断文件是否存在
            if os.path.exists(filename):
                # 打开文件
                with open(filename,"r") as rfile:
                    # 读取全部内容
                    student_old = rfile.readlines()
            else:
                student_old=[]
                # 标记是否删除
                ifdel =False
                if student_old:
                    # 以写方式打开文件
                    with open(filename,"w")as wfile:
                        # 定义空字典
                        d={}
                        for list in student_old:
                            # 字符串转字典
                            d=dict(eval(list))
                            if d[id]!=studentsId:
                                # 将一条学生信息写入文件
                                wfile.write(str(d)+"\n")
                            else: ifdel = True
                        if ifdel:
                            print("id为%s的学生信息已经删除。。。。"% studentsId)
                        else:
                            print("没有找到%s的学生信息。。。。。。"%studentsId)
                else:
                    print("无学生信息。。。。")
                    # 退出循环
                    break

                # show()显示全部学生信息
                inputMark = input("是否继续删除？(y/n):")
                if inputMark=="y":
                    # 继续删除
                    mark = True
                else:
                    # 退出删除学生信息功能
                    mark = False

