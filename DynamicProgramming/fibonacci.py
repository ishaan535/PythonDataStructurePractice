counter = 0
cached = {}
def fibonacci(n):
    if n in cached:
        return cached[n]
    global counter
    counter += 1
    if n<2:
        return n
    else:
        cached[n] = fibonacci(n-1)  + fibonacci(n-2)
        return cached[n]

print(fibonacci(13))
print(counter)