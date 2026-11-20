"""
1. module (file) -> group of statements/expressions
2. package (folder) -> group of modules
3. library (root folder) -> group of packages
"""
# import utils

# print(utils.add(2,4))
# print(utils.add(4,7))
# print(type(utils).__name__)
# print(utils.PI)
# print(utils.PI)

# from utils import PI as p ,add

# print(p)
# print(add(8,5))
# print(sum([2,3,4]))

# from utils import *
# print("inside mods")

# print(PI)
# print(add(43,2))

# from package_name.module_name import property

# from products.get_products import getproducts
# getproducts()

# from package_name import module_name

from products import get_products
get_products.getproducts()