age = int(input("Enter your age: "))

if age < 0:
    print("Please Enter a valid age.")

elif age <18:
    print("You are a minor.")
elif age >=18:
    print("You are a adult.")
else:
    print("You are a senior citizen.")