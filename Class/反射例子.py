import sys


class Manager:
    OPERATE_DIC = [
        ('创造学生账号', 'create_student'),
        ('创建课程', 'create_course'),
        ('查看学生信息', 'check_student_info'),
    ]

    def __init__(self, name):
        self.name = name

    def create_student(self):
        print('创建学生账号')

    def create_course(self):
        print('创建课程')

    def check_student_info(self):
        print('查看学生信息')


class Student:
    OPERATE_DIC = [
        ('查看所有课程', 'check_course'),
        ('选择课程', 'choose_course'),
        ('查看已选择的课程', 'choosed_course')
    ]

    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('check_course')

    def choose_course(self):
        print('choose_course')

    def choosed_course(self):
        print('查看已选择的课程')


def login():
    username = input('请输入user : ')
    password = input('请输入pwd : ')
    with open('user_info.txt') as f:
        for line in f:
            user, pwd, ident = line.strip().split('|')  # ident = 'Manager'
            if user == username and pwd == password:
                print('登录成功')
                return username, ident


def main():
    usr, id = login()
    print('user,id :', usr, id)
    file = sys.modules['__main__']  # 获取到该文件的内存对象
    cls = getattr(file, id)  # Manager = getattr(当前文件,'Manager')
    # cls ==< class '__main__.Manager'>
    obj = cls(usr)  # 实例化类
    operate_dic = cls.OPERATE_DIC  # 调用类下的静态属性
    while True:
        for num, i in enumerate(operate_dic):
            print(num, i[0])
        choice = int(input('num >>>'))
        choice_item = operate_dic[choice]
        getattr(obj, choice_item[1])()  # 执行类下的方法


main()