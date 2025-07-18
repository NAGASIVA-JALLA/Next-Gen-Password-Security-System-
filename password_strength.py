import re
import password_generator as d
def analyze_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if all([length, upper, lower, digit, special]):
        return "Strong"
    elif length and (upper or lower) and (digit or special):
        return "Moderate"
    else:
        return "Weak"
password_strength=analyze_strength(d.pass_word)
if __name__=="__main__":
    print(password_strength)
