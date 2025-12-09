import bcrypt
import os

USER_DATA_FILE = "users.txt"

def hash_password(plain_text_password):
    # Encode the password to bytes, required by bcrypt
    password_bytes = plain_text_password.encode('utf-8')
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    # Decode the hash back to a string to store in a text file
    return hashed_password.decode('utf-8')

def verify_password(plain_text_password, hashed_password):
    # Encode both the plaintext password and stored hash to bytes
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    # bcrypt.checkpw handles extracting the salt and comparing
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)



def register_user(username, password, role="user"):
    if user_exists(username):
        print(f"User {username} already exists.")
        return False
    else:
        # Register a new user
        hashed_password = hash_password(password)

        with open(USER_DATA_FILE, "a") as f:
            f.write(f"{username},{hashed_password},{role}\n")

        print(f"User '{username}' registered with role '{role}'.")
        return True


def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        f = open(USER_DATA_FILE, "x")
        f.close()

    with open(USER_DATA_FILE, "r") as f:
        for line in f.readlines():
            parts = line.strip().split(',', 2)
            if len(parts) < 3:
                continue  # skip old or malformed entries
            user, hash_value, role = parts
            if username == user:
                return True
    return False

def login_user(username, password):
    with open(USER_DATA_FILE, "r") as f:
        lines = f.readlines()
        if lines == "":
            print("No user registered.")
            return False

        for line in lines:
            parts = line.strip().split(',', 2)
            if len(parts) < 3:
                continue
            user, hash_value, role = parts

            if user == username:
                if verify_password(password, hash_value):
                    print(f"Login successful! Your role is: {role}")
                    return True
                else:
                    return False

    print("Username not found.")
    return False


def validate_username(username):
        # check minimum length
        if len(username) <4 or len(username) > 20:
           print("Username must be 3-20 characters long.")
           return False,"Username is not valid"

        if not username.isalnum():
            print ("Username must contain only letters and numbers.")
            return False,"Username is not valid"

        print(f"username {username} is valid")
        return True,"Username is valid"


def validate_password(password):
    if len(password) < 6 or len(password) > 50:
       print("Password must be 6-50 characters.")
       return False,"Password is invalid"
    return True,"Password is valid"

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)


def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()

            # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

         # ROLE INPUT
            role = input("Enter role (user/admin/analyst): ").strip().lower()
            if role not in ["user", "admin", "analyst"]:
                print("Error: Invalid role. Use user/admin/analyst.")
                continue




            # Register the user
            register_user(username, password, role)

        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the dashboard.)")

            else:
                print("\nError: Invalid username or password.")

            input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()