def main():
    fibonacci = []
    n = int(input())
    while n < 0:
        n = int(input())
    
    if n == 0:
        print(fibonacci)
    
    elif n == 1:
        fibonacci = [0]
        print(fibonacci)
    
    else:
        fibonacci = [0,1]
        for i in range(n-2):
            num_siguiente = fibonacci[i] + fibonacci[i+1]
            fibonacci.append(num_siguiente)
        print(fibonacci)    

if __name__=='__main__':
    main()
