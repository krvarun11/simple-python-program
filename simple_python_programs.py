#ppython program to check user id and password
user_id= input("enter user id")
password= input("enter the password")

if user_id=="111" and password=="222":    
    print("welcome")
else:
    print("error ! user id and password do not match")

# simple program to take the user details
name = input("enter name:")
phone_number=input("enter your phone number:")
age= input("enter your age:")
print(name)
print(phone_number)
print(age)
print("your name is {} and age {} ".format(name,age))
print(f"your name is {name} and age {age}")
print("your name is ",name)
print(type(name))
print(type(phone_number))
print(type(age))
