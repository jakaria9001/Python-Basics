# Print the Primes! (use Python3)

def main():
    n = int(input())
    for x in range(2,n+1):
        flag = 1
        sq = int(x**0.5)
        for i in range(2,sq+1):
            if x%i==0:
                flag = 0
                break
        if flag == 1: 
            print(x)
            
    return 0

if __name__ == '__main__':
    main()