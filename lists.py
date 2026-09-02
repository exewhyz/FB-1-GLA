nums = [1,2,3,4,5]
# -len(nums)
# -len(nums) + 1
# -len(nums) + 2
# -len(nums) + 3

a = []
# b = ["Aniket", 20, True, 2 + 3j, [1,3, [6,3,[]]], [2,5], 3.14]

# print("Type:",type(nums))
# print("Length:", len(nums))

start_index = 0 or -len(nums)
last_index = len(nums) - 1  or -1

"""
CRUD operations
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""

#READ
# n = [3,1,4,["Aniket",["Noida"], True]]
# print(n[3][1][0])
# x = [3,1,4,["Aniket",["Noida"], True],["hello"]]
# print(x[4][0])

#CREATE
"""
List Methods for create (modifies original list)
1. append(value) -> None => Inserts value at end
2. insert(index, value) -> None => Inserts value at given index
3. extend([multiple values]) -> None => Inserts multiple values at end
"""
names = ["Aniket", "Himanshu", "Gulshan"]

names.append("Chirag")
names.append("Anish")
# names.append(1,2) #WRONG
# names.append([1,2])
# names.extend([1,2,3,4,5])
names.insert(2,"New Data")
# print("Appended",names)
# print("Inserted",names)

# UPDATE

# x = [ "one", "two",[3, 4], "three"]
# x[2][0] = "new value"
# print(x)

# DELETE/REMOVE

# del keyword => deletes value at given index
# pop(index = -1) -> deleted value => list method => deletes value at given index
# remove(value) -> None =>  list method => deletes first matched value

n = [1,2,1,1,3,4,2,5]

# print("before remove",n)
# del n[4]
# print("deleted value:",n.pop(4))
# n.remove(2)
# print("after remove",n)

# INDEX => list method

# index(value,start = 0,stop=len(list)) ->int
# index of first matched value

# m = ["hello", "hi", "bye","hi"]

# index_of_value = m.index("hi",2,3)
# print("Index:", index_of_value)

c = [1,2,[3,4]]

# idx = c.index([3,4])
# print((c[idx].index(3)))


var = [[1,3,4]]
# idx = c.index(var[0])
# print((c[idx].index(3)))

"""
you have a list containing multiple list.
Find the index of value that is 5 which is present inside first list.
"""

p = [[1,3,5,2], [3,1,2,5] , [5,2,1,3]]

print(p[1].index(5))