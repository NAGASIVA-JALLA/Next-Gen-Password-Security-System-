import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
pass_word=generate_password()
if __name__=='__main__':
    print(pass_word)