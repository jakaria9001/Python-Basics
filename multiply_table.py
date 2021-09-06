#Multiplication Table (use Python3): 

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    inp = int(input())
    for i in range(1,11):
        # print(inp+"*"+i+"="+inp*i)
        print("{} * {} = {}".format(inp,i,i*inp))
        # print(f"Hello {inp} * {i} = {inp*i}")
    return 0

if __name__ == '__main__':
    main()