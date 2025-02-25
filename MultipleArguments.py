def add(*x):
    sum = 0
    for val in x:
        sum += val
    return sum

def display_car(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print(add(5,6,7))
display_car(BMW = 'S6', Mercedes = 'Z300' )