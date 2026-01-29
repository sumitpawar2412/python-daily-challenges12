n = input("Enter your Name: ")
mail = input("Enter your Email ID: ")
number = input("Enter your Mobile Number: ")
age = int(input("Enter your Age: "))
valid = True
if n.count(" ") < 1 or n[0] == " " or n[len(n)-1] == " ":
    valid = False
elif "@" not in mail or "." not in mail or mail[0] == "@":
    valid = False
elif len(number) != 10 or number.isdigit() == False or number[0] == "0":
    valid = False
elif age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
