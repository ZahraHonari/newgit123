import fibo

def total(n):
    t = 0
    for i in range (10) :
        t += i
    
    return t

if __name__ == "__main__":
    print(total(10))
    print(fibo.fibo(12))