#for loop
user_input=int(input("Enter a number:"))
for number in range(1,11):
    print(user_input * number)


#while loop
password="ABCDEF"
input_password=input("Enter a password")
while password != input_password:
    input_password=input("Enter password")
else:
    print("unlocked !!")

