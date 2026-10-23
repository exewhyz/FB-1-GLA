nums = [1,5,2,1,3,1,5]

# print(set(nums))

alphabets = {"a","b","c","d","a"}
# alphabets = {1,2,3,5,4}
# print(alphabets)


"""
CRUD OPERATIONS
1. READ - ❌ (directly)
2. CREATE
3. UPDATE - ❌ (directly)
4. remove
"""

names = {"ayush", "akash", "piyush"}

# for n in names:
#     print(n)

# names.add("abhishek")
# names.update(["a", "b"])
# names.update(("c","d"))
# names.update({"e","f"})
# names.update("gh")
# print(names)

# for n in "gh":
#     names.add(n)

# c_names = list(names)
# for n in c_names:
#     c_names[c_names.index(n)] = n.upper()
    
# print(set(c_names))

# remove, discard, pop, clear

# names.remove("ayush")
# names.remove("z")
# names.discard("ayush")
# names.discard("z")
# print("removed value:",names.pop())
# names.clear()
# print(names)

# empty_set = set({1,2,3})
# empty_set = set([1,2,3])
# empty_set = set("abc")
# print(empty_set)
# print(type(empty_set))

# SET Operations (Union,Intersection, Difference, subset,superset,disjoint,symmetric difference)

set_a = {1,2,3,4,5}
set_b = {2,3}
set_c = {10}

# print(set_a | set_b | set_c)
# print(set_a.union(set_b).union(set_c))

# print(set_a & set_b | set_c)
# print(set_a.intersection(set_b).union(set_c))

# print(set_a - set_b)
# print(set_b - set_a)
# print(set_b - set_c)
# print(set_c - set_b)

# print(set_a.difference(set_b))

# print(set_a >= set_b) # superset
# print(set_a.issuperset(set_b))
# # print(set_b <= set_a) # subset
# print(set_b.issubset(set_a))

# if len(set_a & set_c) == 0:
#     print("both are disjoint")
# else:
#     print("both are not disjoint")

# print(set_a.isdisjoint(set_c))

# print(set_a ^ set_b)
# print(set_a.symmetric_difference(set_b))

print(frozenset("hello"))
print(frozenset([1,2,3,4,5]))
print(frozenset((1,2,3,4,5)))
print(frozenset({1,2,3,4,5}))