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
print("Inserted",names)