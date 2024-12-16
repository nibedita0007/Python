#print(5+5)
#print("Soumava"+" "+"Roy")


'''print(len("Krish"))
print(len(("Ankush","Krish")))'''

#method overloading
class A:
    def show(self):
        print("welcome")
    def show(self,firstname=''):
        print("welcome",firstname)
    def show(self,firstname='',lastname=''):
        print("welcome",firstname,lastname)
obj1=A()
obj1.show()
obj1.show('Soumava')
obj1.show('Soumava','Roy')

#method overriding
