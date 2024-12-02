a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
try:
    c=a/b
    print("Result: ",c)
except:
   print("can't divided by zero")

print("Error handling")