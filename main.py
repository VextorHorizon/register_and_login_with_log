
import time


def log_login(username, success):
    with open("login.log", "a") as log:
        log.write(f"{time.ctime()}) - USER: {username} - {'Success' if success else 'Failed'}\n")

def register_user_data(username_data, password_data):
    with open("user_data.txt", "a") as user_data:
        user_data.write(f"{username_data},{password_data}\n")

def load_user_data():
    users = {}
    try:
        with open("user_data.txt", "r") as user_file:
            for line in user_file:
                u, p = line.strip().split(",")
                users[u] = p
    except FileNotFoundError:
        pass
    return users

mode = input("register or login \n")

if mode == "register":
    user_register_username = input("Username = ").strip()
    user_register_password = input("Password = ").strip()
    register_user_data(user_register_username, user_register_password)
    print(f"ลงทะเบียนสำเร็จ {user_register_username}")
    
    
elif mode == "login":
    users = load_user_data()
    attempt = 0
    while attempt < 5:
        print("=== Login System ===")
        user_login_username = input("Username = ").strip()
        user_login_password = input("Password = ").strip()
        if user_login_username in users:            
            if users[user_login_username] == user_login_password:
                print("Login Successful")
                log_login(user_login_username, True)
                break
        
        else:
            print("Login Failed")
            log_login(user_login_username, False)
            attempt += 1

    if attempt >= 5:
        print("Too many attempt")

else:
    print("Failed")