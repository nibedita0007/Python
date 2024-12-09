            #inheritance
'''class father:
    def Lands(self):
        print("Having 50 Ekar Lands")

class son(father):
    def Money(self):
        print("Having 10 Lakhs Money")
A=son()
A.Lands()
A.Money()'''

#Multi-level inheritance
'''class father:
    surname="Singh"
class son(father):
    def show(self):
        print("Mario ",self.surname)
class Gson(son):
    def disp(self):
        print("Luigi ",self.surname)

s=son()
s.show()

G=Gson()
G.disp()
G.show()'''

#Multiple inheritance
'''class student1:
    def m1(self):
        print("This is the parent class1")
class student2:
    def m2(self):
        print("This is the parent class2")
class student3:
    def m3(self):
        print("This is the parent class3")
#.........
#.........
#.........
class child(student1,student2,student3):
    def m(self):
        print("This is a child class")

obj=child()
obj.m()
obj.m3()'''

#hierarchical inheritance
class father:
    surname="Singh"
    def show(self):
        print("My surname is ",self.surname)

class son(father):
    def disp(self):
        print("My name is Luigi ",self.surname)

class son2(father):
    def disp(self):
        print("My name is Ankush ",self.surname)


s1=son()
s1.disp()

s2=son2()
s2.disp()

#Hybrid inheritance
class A:
    a=10
    print(type(a))
class B(A):
    b=2.54
    print(type(b))  
class C(A):
    c="Soumava"
    print(type(c))      #Hierarchical inheritace
class D(C):
    d=[1,2,3]
    print(type(d))
class E(D):
    e=(50,44,38)
    print(type(e))      #multi-level inheritance




















#encapsulation
class A:
    _a=10
    __b=20
    def show(self):
        print("a= ",self._a)
        print("a= ",self.__b)

obj=A()
obj.show()
print("outside of class ",obj._a)
#print("outside of class ",obj.__b)

