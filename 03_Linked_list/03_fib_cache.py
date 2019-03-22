def cache(func):
    data = {}
    def wrapper(n):
        if n in data:
            return data[n]
        else:
            res = func(n)
            data[n] = res
            return res
    return wrapper


@cache
def fib(n):
    if n <= 2: # 1 or 2
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1, 50):
    print(fib(i))