#list1 = []
#print(type(list1))

#list2 = list()
#print(type(list2))

list3 = [20, "Mario", 30.23, "Luigi", 50]
print(list3)
print(list3[1])
print(list3[1:4])

#count
print(list3.count(20))

#index
print(list3.index(30.23))

#insert
list3.insert(3, "Shaun")
print(list3)

#pop
list3.pop(2)
print(list3)

#extend
list4 = ["Peach"]
list3.extend(list4)
print(list3)

#copy
list5 = list3.copy()
#list5 = list3[:]
print(list5)

#sort
