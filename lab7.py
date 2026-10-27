
# Lab Session 07: Conditional Statements in Python

# Task 1: Calculate Grade
def task1():
    try:
        marks = float(input("Enter your marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Please enter marks between 0 and 100.")
        elif marks >= 90:
            print("Your grade is A+")
        elif marks >= 80:
            print("Your grade is A")
        elif marks >= 70:
            print("Your grade is B")
        elif marks >= 60:
            print("Your grade is C")
        elif marks >= 50:
            print("Your grade is D")
        else:
            print("You have failed.")

    except ValueError:
        print("Invalid input! Enter numbers only.")


# Task 2: Check Email
def task2():
    email = input("Enter your email address: ").strip()

    if "@" in email and email.endswith(".com"):
        print("Email address is valid.")
    else:
        print("Email address is invalid.")


# Task 3: Calculate Order Discount
def task3():
    try:
        amount = float(input("Enter your order amount: Rs. "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        if amount > 5000:
            discount = amount * 0.10
            print(f"You received a 10% discount: Rs. {discount:.2f}")
        else:
            discount = 0
            print("No discount available.")

        bill = amount - discount
        print(f"Your final bill is: Rs. {bill:.2f}")

    except ValueError:
        print("Please enter a valid amount.")


# Task 4: Calculate Library Fine
def task4():
    try:
        days = int(input("How many days late is the book? "))

        if days < 0:
            print("Days cannot be negative.")
        elif days <= 7:
            fine = days * 10
            print(f"Your fine is Rs. {fine}")
        else:
            fine = days * 20
            print(f"Your fine is Rs. {fine}")

    except ValueError:
        print("Please enter a whole number.")


# Task 5: Check Food Availability
def task5():
    menu = ["Burger", "Pizza", "Pasta", "Sandwich", "Fries"]

    print("Available items:", ", ".join(menu))
    item = input("What would you like to order? ").strip().title()

    if item in menu:
        print(item, "is available.")
    else:
        print(item, "is not available.")


# Task 6: BMI Calculator
def task6():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kg: "))

        if height <= 0 or weight <= 0:
            print("Height and weight must be greater than zero.")
            return

        bmi = weight / (height * height)
        print(f"BMI value: {bmi:.2f}")

        if bmi < 18.5:
            print("BMI category: Underweight")
        elif bmi < 25:
            print("BMI category: Normal")
        else:
            print("BMI category: Overweight")

    except ValueError:
        print("Please enter valid numbers.")


# Main Menu
while True:
    print("\n===== Python Lab Tasks =====")
    print("1. Calculate Grade")
    print("2. Check Email")
    print("3. Calculate Discount")
    print("4. Library Fine")
    print("5. Check Food Menu")
    print("6. BMI Calculator")
    print("0. Exit")

    choice = input("Choose a task: ").strip()

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "5":
        task5()
    elif choice == "6":
        task6()
    elif choice == "0":
        print("Program ended. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 0-6.")
