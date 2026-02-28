from 重拾db自信.main import Table, new_file, close

class Quick():
    def __init__(self, filename):
        new_file(filename)

    # 以下是快速功能：

    # 以后会经常开发！
    def register(self, name, password, email):

        registering = Table("user", password="int", name='text', email='text')
        registering.write(password, name, email)

        for i in registering.read_all():
            print("item")
            for row in i:
                print(row)

    def login(self, name, password):

        pass

    def logout(self):
        pass

    def exit(self):
        close()


class Web():
    #还没想好自定义用户管理类:(
    def __init__(self):
        pass
    def main(self):
        pass
