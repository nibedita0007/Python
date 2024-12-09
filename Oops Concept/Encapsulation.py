class A:
    def __init__(self):
        self.__a = None 
        self.__b = None 

    def show(self, x, y):
        self.__a = x
        self.__b = y
        print(f"{self.__a}, {self.__b}")

obj = A()
obj.show(10, 20)
