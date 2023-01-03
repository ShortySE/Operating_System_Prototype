from System.command_prompt import*

def check_username():
    file = open('User/users.os', 'r')
    ids = file.read()
    if ids == '':
        create_username()

    else:
        pass

# This runs the first time you boot
def create_username():
    file = open('User/users.os', 'w')
    username = input("Enter a new username: ")
    password = input("Enter your password: ")
    file.write(username + '\n')
    file.write(password + '\n')

def on_boot() -> bool:
    file = open('User/users.os', 'r')
    ids = file.read()
    username = input("Username: ")
    password = input('Password: ')
    if username in ids:
        pass

    else:
        print("Incorrect username")

    if password in ids:
        cd_prompt(username)
        return True

    else:
        print("Incorrect password")
        return False