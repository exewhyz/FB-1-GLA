# open("file_path", mode="r", encoding="utf-8")

# fl = open("utils.py")
# data = fl.read()
# print(data)
# fl.close()

# file = open("hello.txt")
# d = file.read()
# file.close()
# print(d)

# f = open("test.txt", "x")

# f1 = open("fb.txt", "w")
# f1.write("hello")
# f1.write(" world")

# f1 = open("fb.txt", "a")
# f1.write("\nhello")
# f1.write(" world")
# f1.close()


# with open("fb.txt", "a") as file:
#     file.write("\nWritten using new syntax")

# read(size=-1) -> str
# write(str) -> int

"""
seek()
tell()
truncate()
"""

# with open("fb.txt", "r") as file:
#     print(file.read(5))
#     print(file.tell())
#     file.seek(3)
#     # file.seek(3)
#     print(file.tell())
#     print(file.read(5))
    
# with open("fb.txt", "r+") as file:
#     # file.read(5)
#     # file.seek(4)
#     file.truncate(8)
    
    
"""
modes
1. r -> read
2. w -> write
3. a -> append
4. b -> binary
5. x -> create
6. t -> text
7. rb -> read binary
8. wb -> write binary
9. ab -> append binary
10. r+ -> read and write
11. +w -> Read and write
12. +a -> read and append
"""

with open("fb.txt", "r") as file:
    # lines = []
    # for line in file:
    #     lines.append(line.strip())
    # print(lines[0])
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    print(file.readlines())
