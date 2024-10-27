fibo = ()


def fibonacci_last_term(upto):
    if upto <= 0:
        return "Input should be a positive integer."
    elif upto == 1:
        return 0
    elif upto == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, upto):
        a, b = b, a + b
    return b

for i in range(1, 11):
    fibo = fibo + (fibonacci_last_term(i),)
    
print(fibo)