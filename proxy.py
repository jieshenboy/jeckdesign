class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), '\r\n'.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('add user {}'.format(user))

class Info:

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = 'pass'

    def read(self):
        self.protected.read()

    def add(self,user):
        sec = input('what is the secret')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

def main():
    info = Info()
    while True:
        print('1. read list\r\n2. add user\r\n 3.quit\r\n')
        key = input('choose option:\r\n')
        if key == '1':
            info.read()
        elif key== '2':
            name = input("choose username:\r\n")
            info.add(name)
        elif key == '3':
            exit()

        else:
            print('unkown option: {}'.format(key))

if __name__=="__main__":
    main()

