
int(input("enter the number of students: "))

name=input("name of the student: ")

tamil=float(input(f"enter {name} tamil mark: "))
english=float(input(f"enter {name} english mark: "))
maths=float(input(f"enter {name} maths mark: "))
science=float(input(f"enter {name} science mark: "))
social=float(input(f"enter {name} social mark: "))

if tamil>=35:
    print (f"{name} was pass in tamil")
else:
    print(f"{name} was fail in tamil")

if english>=35:
     print (f"{name} was pass in english")
else:
    print(f"{name} was fail in english")

if maths>=35:
     print (f"{name} was pass in maths")
else:
    print(f"{name} was fail in maths")

if science>=35:
     print (f"{name} was pass in science")
else:
    print(f"{name} was fail in science")

if social>=35:
     print (f"{name} was pass in social")
else:
    print(f"{name} was fail in social")
    


total=int(round(tamil+english+maths+science+social))
print(f"total mark of {name}: {total}")

if total>=195:
    print(f"{name} was pass in all subject")
else:
    print(f"{name} was fail in any subject")

mark=(total/5)
print(f"percentage of {name} mark: {mark}%")

