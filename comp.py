# nums=[]

# for n in range(1,10):
#     nums.append(n*2)
    
# [statement for val in iterable]
# iterable - str, list, tuple, set

# print([n*2 for n in range(1,10)])

# even = []
# for n in range(1,10):
#     if n% 2 == 0:
#         even.append(n)
        
# [statement for val in iterable if condition]
# print([n for n in range(1,10) if n % 2 == 0])


# even_nums = []
# odd_nums = []
# for n in range(1,10):
#     if n% 2 == 0:
#         even_nums.append(n)
#     else:
#         odd_nums.append(n)
# [statement1 if condition else statement2 for val in iterable]
# print([n*2  if n % 2 == 0 else n *3  for n in range(1,10)])

# e = []
# o = []
# [e.append(n) if n % 2 == 0 else o.append(n) for n in range(1,9)]
# print(e)
# print(o)

# cords = []
# for i in range(1,3):
#     for j in range(2,4):
#         cords.append((i,j))
# print(cords)

# [statement for i in iterable1 for j in iterable2]
# print([(i,j) for i in range(1,3) for j in range(2,4)])
# print([{i : j} for i in range(1,3) for j in range(2,4)])

# { key : value for loop}
# print({ i : j for i in range(1,3) for j in range(2,4)})

# print({
#     1 : 2,
#     1 : 3,
#     2: 2,
#     2 : 3
# })

l1 = ["one", "two", "three"]
l2 = [1,2,3]

# print({ k : v for k in l1 for v in l2  })
print({ k.upper() : v for k,v in zip(l1,l2)})

# { "one" : 1 , "one" : 2, "one" : 3, "two" : 1, ....}
l3 = ["i","ii","iii"]

# print(list(zip(l1,l2,l3)))
print(dict(zip(l1,l2)))