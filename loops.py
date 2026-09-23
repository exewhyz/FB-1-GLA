numbers = [1,2,3,4,5]

# for x in numbers:
#     print(x * 0.3 + x)
    
# print(numbers[0] * 0.3 + numbers[0])
# print(numbers[1] * 0.3 + numbers[1])
# print(numbers[2] * 0.3 + numbers[2])
# print(numbers[3] * 0.3 + numbers[3])
# print(numbers[4] * 0.3 + numbers[4])

# range(stop) -> range(0,stop)
# range(start,stop) -> range(start,stop,1)
# range(start,stop,step) -> range

# for num in range(1,101):
#     if num % 2 != 0:
#         print(num)


# find max value from list

# marks = [47, 30, 67, 29, 88, 56 , 20]

# maximum = marks[0]
# for m in marks:
#     if m > maximum:
#         maximum = m

# print(maximum)

books_prices = [159, 99, 499, 199, 2499]
discount = 10
total_price = 0

for price in books_prices:
    if price > 199:
        total_price = total_price + price - 0.1 * price
    else:
        total_price = total_price + price

print(total_price)

numbers = [159, 99, 499, 199, 2499]

count = 0

for num in numbers:
    if num > 199:
        count = count + 1
print(count)