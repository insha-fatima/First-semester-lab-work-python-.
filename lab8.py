
# LAB SESSION 08 - Loop Control Statements in Python

# Task 1: Student Attendance
print("Task 1: Student Attendance")

for roll_no in range(1, 6):
    print("Roll Number:", roll_no, "- Present")


# Task 2: OTP Verification
print("\nTask 2: OTP Verification")

correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter your 4-digit OTP: ")
    attempts += 1

    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")

if otp != correct_otp:
    print("Maximum attempts reached.")


# Task 3: Store Inventory
print("\nTask 3: Store Inventory")

items = ["Milk", "Out of Stock", "Bread", "Eggs", "Out of Stock", "Juice"]

for item in items:
    if item == "Out of Stock":
        continue

    print("Available item:", item)


# Task 4: Factory Machine Status
print("\nTask 4: Factory Machine Status")

machine_status = ["Working", "Working", "Idle", "Malfunction", "Working"]

for status in machine_status:
    if status == "Malfunction":
        print("Malfunction detected. Stopping the system.")
        break

    print("Machine status:", status)


# Task 5: Menu Using Pass
print("\nTask 5: Menu Options")

menu = ["Home", "About", "Contact", "Coming Soon", "Services"]

for option in menu:
    if option == "Coming Soon":
        pass
    else:
        print("Menu option:", option)


# Task 6: Login System
print("\nTask 6: Login System")

correct_password = "python123"
attempts = 0

while attempts < 5:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

if attempts == 5:
    print("Too many failed attempts. Login stopped.")
