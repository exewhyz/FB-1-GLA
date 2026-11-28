# def add_nums(**nums):
#     return nums

# print(add_nums(f=1,s=2))


# def event_plan(event_name,date,*contri,**leader_details):
#     return {
#         "ev_name": event_name,
#         "ev_date": date,
#         "contribution_amt" : f"Rs. {sum(contri)}",
#         "leader_details" : leader_details
#     }
    
# print(event_plan("test", "29-11-2026",100, 500, 40, 99, lead_name="Aniket", lead_email="aniket@test.com"  ))
# print(event_plan("test2", "30-11-2026",100, 500, 40, lead_name="Aniket", lead_email="aniket@test.com", lead_mob=9876543210 ))


# def add(a:str,b:str):
#     return a+b

# print(add(1,2))
# name="Aniket"
# print(*name,sep="-")

# add = lambda a,b: a + b

# add()

# print((lambda a,b: a + b)(1,3))




# def get_second_value(d):
#     return d[1]

emps = [ ("Emp3", 19000), ("Emp1", 15000), ("Emp2", 700000)] 
emps.sort(key=lambda d : d[1])
print(emps)

# from functools import reduce
# def xyz(*nums, op):
#     return op(nums)
# def sub(nums):
#     return reduce(lambda x,y : x - y, nums)
# def mul(nums):
#     return reduce(lambda x,y : x * y, nums)
# # print(xyz(5,4, lambda nums : sum(nums)))
# print(xyz(5,4,3,7,9,0, op=sub))