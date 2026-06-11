thislist = ["apple", "banana", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



thislist = ["apple", "banana", "cherry"]
print(thislist[1])



thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# ADDING LIST ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To insert a list item at a specified index, use the insert() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# REMOVE A LIST ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# REMOVE SPECIFIC INDEX 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# REMOVE THE LOIT COMPLETELY

thislist = ["apple", "banana", "cherry"]
del thislist


# CLEAR THE LIST

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)