#if_else statement
user_input=input("Enter a number:")
if user_input % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#elif statement
age=int(input("Enter your age:"))
if age < 18:
    print('You are too young to marry.')
elif age > 60 :
    print('You are too old to marry.')
else:
    print('we will find a perfect match for you')