cache={}                                # start cache as an empty dictionary

def cached_execution(cache, proc, proc_input):
    if proc_input in cache:
        print "Second time:"             # second execution (should only print out the result)
        return cache[proc_input]
    else:
        cache[proc_input]=proc(proc_input)
        return cache[proc_input]

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

print cached_execution(cache, factorial, 50)
print cached_execution(cache, factorial, 50)

cache = {} 

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))
               
print cached_execution(cache, cached_fibo,100)
