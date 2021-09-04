

i=0
while(i<10):
    print(i)
    i+=1
    
print(list(range(0,10,2)))

print(list(range(10)))# from 0 to 9, increment is 1 defaulkt
print(list(range(1,10))) # 1 to 9, default incr 1
print(list(range(10,1,-2))) # 10 to 2 decrement by 2

descending_list = list(range(10,-5,-3))
print(descending_list)
print(descending_list[-2])
#reversing a list
descending_list.reverse()
print(descending_list)

#List comprehension:

square_naive = []
for x in range(1,11):
    square_naive.append(x**x)
print(square_naive)
def x():
    return 1;
x()