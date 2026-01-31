n = input("Enter Full Name: ")
e = input("Enter Email ID: ")
m = input("Enter Mobile Number: ")
a = int(input("Enter Age: "))

p = False
if len(n) > 0 and n.count(" ") >= 1 and n[0] != " " and n[-1] != " ":
    p = True

q = False
if "@" in e and "." in e and e[0] != "@":
    q = True

r = False
if len(m) == 10 and m.isdigit() and m[0] != "0":
    r = True

s = False
if a >= 18 and a <= 60:
    s = True

if p and q and r and s:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
