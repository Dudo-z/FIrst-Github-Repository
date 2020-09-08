list1 = list(range(5))
list2 = list1
list3 = list1[:]
list1.append(8)
list2.append(11)
list3.append(10)
print(list1)
print(list2)
print(list3)
