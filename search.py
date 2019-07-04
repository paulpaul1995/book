import os


def search():
    mark=True
    # 保存查询结果的学生列表
    student_query=[]
    while mark:
        id=""
        name=""
        # 判断文件是否存在
        if os.path.exists(filename):
            mode=input("按id输入1；按姓名查询输入2：")
            if mode =="1":
                id=input("请输入学生id：")
            elif mode=="2":
                name=input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入")
            search()
            # 打开文件
            with open("E:\p1\student.txt","r")as file:
                # 读取全部内容
                student=file,readlines()
                for list in student:
                    d=dict(eval(list))
                    # 判断是否按姓名查询
                    if id is not "":
                        if d[id]==id:
                            student_query.append(d)
                    elif name is not "":
                        if d[name] == name:
                            student_query.append(d)
                #             显示查询结果
                show_student(student_query)
                # 清空列表
                student_query.clear()
                inputMark=input("是否继续查询（y/n）:")
                if inputMark =="y"
                    mark=True
                else:
                    mark=false
        else:
            print("暂未保存数据信息。。。")
            return

# 将保存在列表的学生信息显示出来
def show_student(stuedent_list):
    # 如果没有要显示的数据
    if not studnet_list:
        print("**无数据信息**\n")
        return 
#     定义标题显示格式
    format_title="{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    # 按指定格式显示标题
    print(format_title.format("id","名字","英语成绩","python成绩","c成绩","总成绩"))
#     定义具体内容显示格式
    format_date="{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    # 通过for循环将列表中的数据全部显示出来
    for info in stuedent_list:
        print(format_date.format(info.get("id")))
        info.get("name"),str(info.get("engish")),str(info.get("python")),str(info.get("c"))
        str(info.get("engish"))+str(info.get("python"))+str(info.get("c").center(12))

        
