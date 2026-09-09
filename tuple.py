[1, 2, 3] # List
(1, 2, 3) # Tuple


t = ( 1, ("Hello", True), 3)
# print(t[0:2:2])


# slicing -> list/tuple/str

# start:stop:step
# 0:length:1


nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[:]) # without start (0) and stop (len(nums))
# print(nums[3:]) # without stop (len(nums))
# print(nums[:6]) # without start (0)

# print(nums[::]) # without start (0), stop (length) and step (1)
# print(nums[::4]) # without start (0) and stop (length)
# print(nums[3::4]) # without stop (length)
# print(nums[3:8:2]) # with start, stop and step

# print(nums[::-1])
print(nums[7:2:-2])
