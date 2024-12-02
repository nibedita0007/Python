#for loop

# user_input=int(input("Enter a number: "))
# for number in range(1,11):
    # print(user_input * number)


#while loop

# password="ABCDEF"
# input_password=input("Enter a password: ")
# while password != input_password:
#     input_password=input("Enter a password: ")
# else:
#     print("Unlocked !!")


#if_else condition

# age=int(input("Enter your age: "))
# if(age>5):
#     print("You are eligible for study")
# else:
#     print("Not eligible")


#elif condition
                                                     
'''age=int(input("Enter your age: "))
if(age<18):
    print("you are too young to marry")
elif(age>60):
    print("you are too old to marry")
else:
    print("We are find a perfect person")'''



#palindrome number check
num=int(input("Enter a number: "))
str_num=str(num)
if str_num == str_num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not palindrome")


