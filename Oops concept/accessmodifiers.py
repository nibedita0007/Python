#Access modifiers
'''class A:
    a=10    #public
    _b=20   #protected
    __c=30      #private
    print(a," ",_b," ",__c)
    def add(self):
         self.__c=self.a+self._b           # c=a+b
         print("addition: ",self.__c)

obj=A()
obj.add()
print(obj.a)
print(obj._b)
print(obj.__c)'''


class A:    #parent
    a=10
    _b=20
    __c=30
    print(a," ",_b," ",__c)

class B(A):   #child
    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)
obj=B()
obj.show()
