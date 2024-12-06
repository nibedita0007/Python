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
class father:
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
#G.show()

#Multiple inheritance