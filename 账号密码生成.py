import random


def get_firstname():
    # 常见的英文名
    firstname_list = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin', 'Jason', 'Matthew', 'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Scott', 'Eric', 'Stephen', 'Andrew', 'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis', 'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas', 'Henry', 'Carl', 'Arthur',
                      'Ryan', 'Roger', 'Joe', 'Juan', 'Jack', 'Albert', 'Jonathan', 'Justin', 'Terry', 'Gerald', 'Keith', 'Samuel', 'Willie', 'Ralph', 'Lawrence', 'Nicholas', 'Roy', 'Benjamin', 'Bruce', 'Brandon', 'Adam', 'Harry', 'Fred', 'Wayne', 'Billy', 'Steve', 'Louis', 'Jeremy', 'Aaron', 'Randy', 'Howard', 'Eugene', 'Carlos', 'Russell', 'Bobby', 'Victor', 'Martin', 'Ernest', 'Phillip', 'Todd', 'Jesse', 'Craig', 'Alan', 'Shawn', 'Clarence', 'Sean', 'Philip', 'Chris', 'Johnny', 'Earl', 'Jimmy', 'Antonio']
    # 随机选择一个名字返回
    return random.choice(firstname_list)


def get_lastname():
    # 常见的英文姓氏
    lastname_list = ['Amos', 'Berry', 'Benz', 'Brooks', 'Colt', 'Cox', 'Cruz', 'Cyrus', 'Darcy', 'Day', 'Duke',
                     'Earp', 'Finn', 'Hardy', 'Henn', 'Hyde', 'Lott', 'Luna', 'Nash', 'Oak', 'Peck', 'Pope', 'Rossi', 'York', 'Zade']
    # 随机选择一个姓氏返回
    return random.choice(lastname_list)


def get_password():
    # 10位随机密码（大小写字母+数字）
    password_list = []
    for i in range(10):
        # 随机选择一个字符
        password_list.append(random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    # 将列表转换为字符串
    return ''.join(password_list)


def get_email(f, l):
    # 拼接firstname和lastname再加上两位随机数字
    return f.lower() + l.lower() + str(random.randint(10, 99)) + '@gmail.com'


if __name__ == '__main__':
    # 生成一个账号密码并保存到文件
    with open('account.txt', 'w') as f:
        firstname = get_firstname()
        lastname = get_lastname()
        password = get_password()
        email = get_email(firstname, lastname)
        f.write('firstname:' + firstname + '\n')
        f.write('lastname:' + lastname + '\n')
        f.write('email:' + email + '\n')
        f.write('password:' + password + '\n')
        f.write('key:\n')
