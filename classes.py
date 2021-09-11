# More on Python
# class Sales:
#     def __init__(self, id):
#         self.id = id

# id = 100

# val = Sales(123)
# print(val.id)

# class A:
#     def __init__(self, i = 0):
#         self.i = i

# class B(A):
#     def __init__(self, j = 0):
#         self.j = j

# def main():
#     b = B()
#     print(b.i)
#     print(b.j)

# main()

def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)