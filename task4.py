age = int(input("enter age: "))

if age <= 0:
    print("age is not valid")
elif age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting")
