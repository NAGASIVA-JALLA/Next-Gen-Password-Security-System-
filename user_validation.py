from password_hasher import password_hash
from password_generator import pass_word
from password_hasher import verify_password
users_db = {}

def register_user(username, hashed_password):
    if username in users_db:
        return False
    users_db[username] = hashed_password
    return True

def login_user(username, password, verify_func):
    if username in users_db:
        return verify_func(users_db[username], password)
    return False
def update_password(username, new_hashed_password):
    users_db[username]=new_hashed_password
if __name__=='__main__':
    user_name=input("ENTER YOU NAME")
    print(register_user(user_name,password_hash))
    print(login_user(user_name,pass_word,verify_password))
    print(users_db)