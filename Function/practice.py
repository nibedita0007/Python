# x=float(input("Enter a number: "))
# print(x)
# print(type(x))
                                                               
# student=[10,20,45,38,20]                                
# print(student)
# print(type(student))


# student=(10,25,36,40,20)
# print(student)
# print(type(student))

# student={"xyz":40,"abcd":60,"efg":70}
# print(student)
# print(type(student))

'''user_input=int(input("enter a number: "))
for number in range(1,11):
     print(user_input * number)'''

'''def calculator(a,b):
     print("addition:",a+b)
     print("substraction:",a-b)
     print("multi:",a*b)
     print("div:",a/b)

calculator(8,4)
calculator(10,2)'''

#name="soumava"
#print(len(name))

'''student=["Lina","Priya","Taniya","Ayan","xyz"]
del student[4]
print(student)
print(type(student))'''



'''def college(name):
     print("good morning",name)

college("soumava")'''


'''for i in range(5):
     for j in range(5):
          print(" ",end=" ")
     for j in range(i,5):
          print("*",end="")
     print()

class college:
     age=10
     print(age)'''


'''rows=5
for i in range(rows):              #i=0             i=1
     for j in range(rows-i-1):    # 5-0-1=4        5-1-1=3
          print(" ",end="")
     for k in range(1 * i + 1):    #1*0+1=1       1*1+1=2
          print("* " ,end="")
     print()'''


'''num=11        
if num >1:
     for i in range(2,num):
          if num % i ==0:
               print("This is not a prime")
               break
     else:
          print("This is a prime")
else:
     print("This is not prime")'''


#fibonacci series
def fibonacci_series(n):
     a=0
     b=1
     for i in range(n):
          print(a,end=" ")
          a,b=b,a+b
fibonacci_series(10)



     







