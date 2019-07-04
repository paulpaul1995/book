import re

def menu():
    print("==============学生信息管理系统============\n"
          "**************功能菜单********************\n"
          "1 录入学生信息\n"
          "2 查找学生信息\n"
          "3 删除学生信息\n"
          "4 修改学生信息\n"
          "5 排序\n"
          "6 统计学生总人数\n"
          "7 显示所有学生信息\n"
          "0  退出系统\n"
          "==========================================\n"
          "说明：通过数字或↑↓方向键选择菜单\n" )

def main():
    # 标记是否退出系统
    ctrl=True
    while(ctrl):
        # 显示菜单
        menu()
        # 显示菜单选项
        option = input("请选择：")
        # 提取数字
        option_str = re.sub("\D","",option)
        if option_str in["0","1","2","3","4","5","6","7"]:
            option_int = int(option_str)
            # 退出系统
            if option_int ==0:
                print("您已退出学生信息管理系统！")
                ctrl = False
            # 录入学生成绩信息
            elif option_int==1:
                pass
            # 查找学生成绩
            elif option_int==2:
                pass
            # 删除学生成绩
            elif option_int==3:
                pass
            # 修改学生成绩
            elif option_int==4:
                pass
            # 排序
            elif option_int==5:
                pass
            # 统计学生成绩信息
            elif option_int==6:
                pass
            # 显示所有学生信息
            elif option_int==7:
                pass

main()

