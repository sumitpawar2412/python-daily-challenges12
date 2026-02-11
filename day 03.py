N=int(input("enter the number of students:"))
names=[]
marks=[]
for i in range(N):
    a=int(input(f"enter the student marks {i}:"))
    b=input(f"enter the student name {i}:")
    marks.append(a)
    names.append(b)
valid=0
fail=0
for i in range(N):
    m=marks[i]
    name=names[i]
    if len(name)%2==0:
        m=m+2
    else:
        m=m-2
    if m<0 or m>100:
        print(str(m)+" -> Invalid")
    else:
        valid+=1
        if m>=90:
            print(str(m)+" -> Excellent")
        elif m>=75:
            print(str(m)+" -> Very Good")
        elif m>=60:
            print(str(m)+" -> Good")
        elif m>=40:
            print(str(m)+" -> Average")
        else:
            print(str(m)+" -> Fail")
            fail+=1
print("Total Valid Students:",valid)
print("Total Failed Students:",fail)
