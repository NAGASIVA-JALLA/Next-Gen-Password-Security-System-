import random
#import time
from password_hasher import hash_password
from user_validation import users_db # Simulated database (dict)
from password_strength import analyze_strength
from user_validation import update_password

# Simulate sending OTP (we'll just print it)
def send_otp():
    otp = random.randint(100000, 999999)
    print(f"\n OTP sent to your registered email: {otp}")  # Simulate send
    return str(otp)


def reset_password(username):
    if username not in users_db:
        print(" Username not found.")
        return

    otp = send_otp()
    attempts = 3

    while attempts > 0:
        user_input = input("Enter the OTP: ")
        if user_input == otp:
            new_pwd = input("Enter your new password: ")
            strength = analyze_strength(new_pwd)
            hashed = hash_password(new_pwd)

            print(" Password reset successfully!")
            print(f"✅ Password updated successfully.\n🛡 New Strength: {strength}")
            print("⚠ Please save your new password securely.")
            return hashed
        else:
            attempts -= 1
            print(f" Incorrect OTP. Attempts left: {attempts}")

    print(" OTP verification failed. Try again later.")