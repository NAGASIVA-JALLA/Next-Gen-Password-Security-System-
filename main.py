from password_generator import generate_password
from password_strength import analyze_strength
from password_hasher import hash_password, verify_password
from user_validation import register_user, login_user,update_password


def main():
    while True:
        print("\n==== Next-Gen Password Security ====")
        print("1. System Generated Password")
        print("2. User Created Password")
        print("3. Login User")
        print("4.Reset/change password ")
        print("5. Exit")

        choice = input("Enter your choice: ")
        #system will randomly generate a password ,analyze the strength of that and it can hashe  that password
        """
        hashing using argon2 because of it's nature.basically it adds a unique salt to your password
        """
        if choice == '1':
            uname = input("Enter username: ")
            length = int(input("Enter desired password length: "))
            pwd = generate_password(length)
            strength = analyze_strength(pwd)
            hashed = hash_password(pwd)

            print(f"\nGenerated Password: {pwd}")
            print(f"Password Strength: {strength}")

            if register_user(uname, hashed):
                print("User registered successfully with system-generated password.")
            else:
                print("Username already exists.")

        #user will  generate a password ,analyze the strength of that password and after hashe that password using argon2 technique
        elif choice == '2':
            uname = input("Enter username: ")
            pwd = input("Enter your password: ")
            strength = analyze_strength(pwd)
            hashed = hash_password(pwd)

            print(f"\nPassword Strength: {strength}")

            if register_user(uname, hashed):
                print("User registered successfully with custom password.")
            else:
                print("Username already exists.")

        #checking user credentials
        elif choice == '3':
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            if login_user(uname, pwd, verify_password):
                print("Login successful.")
            else:
                print(" Invalid credentials.")

        # ==== Forgot Password / Reset Password ====
        elif choice =="4":
           uname = input("Enter your username: ")
        # Check if user exists
           if uname not in update_password.__globals__["users_db"]:
                print("Username not found. Please register first.")
           else:
                print("\n1. Generate a new password")
                print("2. Enter a new password manually")
                sub_choice = input("Choose an option: ")
                if sub_choice == '1':
                    length = int(input("Enter password length: "))
                    new_pwd = generate_password(length)
                    print(f"🔐 Generated New Password: {new_pwd}")
                elif sub_choice == '2':
                    new_pwd = input("Enter your new password: ")
                else:
                    print("Invalid option.")
                    exit()

                strength = analyze_strength(new_pwd)
                hashed = hash_password(new_pwd)
                update_password(uname, hashed)
                print(f"✅ Password updated successfully.\n🛡 New Strength: {strength}")
                print("⚠ Please save your new password securely.")

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()