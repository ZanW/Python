# remove one element from the list via remove(), pop() and del

list1 = ["zhang","wang","li"]

print("the original list is: ")
print(list1)

# using del
list = list1 
print("1. by using 'del'")
del list[2]
list_del = list
print("after del: "+"list_del"+"\n")

# using remove
list1 = ["zhang","wang","li"]
list = list1 
print("2. by using 'remove()'\n" + "remove the last element\n")
# list_remove = list.remove() takes exactly one argument 
# print(list_remove)
print("\nremove the first element\n")
list1 = ["zhang","wang","li"]
list = list1 
# list_remove = list.remove(2)remove only takes value not index
print(list1)
list.remove("li")
list_remove = list
print(list_remove)

# using pop()
list1 = ["zhang","wang","li"]
list = list1 
print("3. by using 'pop()'\n" + "remove the last element\n")
list_pop_last = list.pop()
print(list)
print()
print("the popped element is: "+ list_pop_last + "\n")
list1 = ["zhang","wang","li"]
print("pop the first element of the list\n")
list = list1 
list_pop_first = list.pop(0)
print(list)
print()
print("the popped first element is: "+ list_pop_first + "\n")

