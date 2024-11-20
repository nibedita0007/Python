#if_else condition

user_input=int(input("Enter a number: "))
if user_input % 2 ==0:
    print("number is even")
else:
    print("number is odd")


#elif condition

age=int(input("Enter your age: "))
if age < 18:
    print("You are too young to marry")
elif age>60:
    print("You are too old to marry")
else:
    print("we will find a perfect person for you")