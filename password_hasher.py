from argon2 import PasswordHasher
import password_generator as d

ph = PasswordHasher()

def hash_password(password):
    return ph.hash(password)

def verify_password(hashed, password):
    try:
        ph.verify(hashed, password)
        return True
    except:
        return False

password_hash=hash_password(d.pass_word)
if __name__=="__main__":
    print(password_hash)
    password_verifying=verify_password(password_hash,d.pass_word)
    print(password_verifying)