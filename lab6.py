name = input("Enter your name: ")
roll = input("Enter your roll no: ")
email = name.lower() + roll + "@university.edu.pk"
print("Your email:", email)

email = input("Enter your email: ")
at = email.find("@")
domain = email[at + 1:]
print("Domain:", domain)

name = input("Enter full name: ").strip()
age = input("Enter age: ").strip()

if name.replace(" ", "").isalpha() and name.istitle():
    print("Name is valid")
else:
    print("Invalid name (letters only, each word capitalized)")

if age.isdigit() and age.isnumeric() and age.isdecimal():
    print("Age is valid:", age)
else:
    print("Invalid age (digits only)")

cnic = input("Enter CNIC (42101-1234567-1): ")
first_six = cnic[:6]          # "42101-"
rest = cnic[6:]               # "1234567-1"
masked = first_six + rest.replace(rest, "XXXXXXX-X")
print(masked)

desc = input("Enter product description: ")
print("Number of characters:", len(desc))

address = input("Enter full address: ")
parts = address.split(",")
clean = [p.strip() for p in parts]
label = " | ".join(clean)
print(label)
