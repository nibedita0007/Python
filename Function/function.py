#pre-defined function

'''x="student"
print(len(x))
print(type(x))'''



#user-defined function

'''a=4
b=2
print("addition: ",4+2)
print("substraction: ",4-2)
print("multiplication: ",4*2)
print("div: "4/2)

a=40
b=2
print("addition: ",40+2)
print("substraction: ",40-2)
print("multiplication: ",40*2)
print("div: "40/2)

.......................
......................'''

'''def calculator(a,b):
    print("addition: ",a+b)
    print("substraction: ",a-b)
    print("multiplication: ",a*b)
    print("div: ",a/b)

calculator(10,5)
# calculator(50,10)'''


'''def greet():
    print("good morning")

msg=greet()
print(msg)     #none


def greet(name):
    print("good morning ",name)

greet("Ankit","kumar")


#positinal arguments

def greet(firstname,lastname):
    print("good morning",firstname,lastname)

greet("Ankit","kumar")'''


#keyword arguments

'''def greet(firstname,lastname):
    print("good morning",firstname,lastname)

greet(lastname="Roy",firstname="Soumava")'''

#default argument

def greet(firstname="ABCD"):
    print("good morning",firstname)

greet("Soumava")
