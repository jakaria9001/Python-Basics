
# print ('Hello World')
# my_string = "jakaria"
# k = [print(i) for i in my_string if i not in "aeiou"]
# print(k)

# my_string = "hello world"
# k = [(i.upper(), len(i)) for i in my_string]
# print(k)

# d = {"john":40, "peter":45}
# print(d)
# # d.delete("john")
# del d["john"]
# print(d)

def myfunc(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True

print(myfunc(21))