def cached_fibo(n):
    L=[0,1]
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        i=2
        while i<=n:
            a=L[i-1]+L[i-2]
            L.append(a)
            i=i+1
        return L[-1]
    
print cached_fibo(0)
print cached_fibo(1)
print cached_fibo(2)
print cached_fibo(3)
print cached_fibo(4)
print cached_fibo(5)
print cached_fibo(10)
print cached_fibo(50)
print cached_fibo(100)
