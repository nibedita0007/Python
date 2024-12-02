            #inheritance
class father:
    def Lands(self):
        print("Having 50 Ekar Lands")

class son(father):
    def Money(self):
        print("Having 10 Lakhs Money")
A=son()
A.Lands()
A.Money()