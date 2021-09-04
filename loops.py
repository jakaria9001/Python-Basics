#take an array as input and print the sum
# snake_case in python

input_list = input()
print(input_list)
print(type(input_list)) # input is string by default
input_list = input_list.split(' ')
sum = 0
new_list = []
for num in input_list:
    sum += int(num)
    new_list.append(int(num))
print(sum)
print(new_list)