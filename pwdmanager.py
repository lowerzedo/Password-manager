from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pass = input("Enter master password: ")
key = load_key() + master_pass.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r')as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "| Password:", fer.decrypt(passw.encode()).decode()) 

def add():
    name = input("Enter account name: ")
    pwd = input("Enter password ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    option = input("Do you want to view or add password (view/add) ? To quit enter 'Q' ").lower()
    if option == 'q':
        break

    if option == 'view':
        view()
    elif option == 'add':
        add()
    else:
        print("Enter correct keyword! ")
        continue