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

f1 = open("fb.txt", "a")
f1.write("\nhello")
f1.write(" world")
f1.close()