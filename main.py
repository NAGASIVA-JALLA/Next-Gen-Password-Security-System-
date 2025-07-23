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
            update_hash=reset_password(uname)
            update_password(uname, update_hash)
          

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
