#!usr/bin/python3

is_student = True  
is_employed = False 

if is_student and is_employed:
    print("You are a working student.")
elif is_student and not is_employed:
    print("You are a student.")
elif not is_student and is_employed:
    print("You are employed but not a student.")
    
age = int(input("Please enter your age: "))
if age >= 18:
    has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()
    if has_license == "yes":
        print("You are allowed to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")
