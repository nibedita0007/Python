#Multithreading*****************
from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("Krish")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Ankush")
            sleep(1)

obj1=A()
obj2=B()

obj1.start()
obj2.start()
