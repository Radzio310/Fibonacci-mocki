fib = []
fib.append(1)
fib.append(1)

def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

element = int(input("Który element ciągu chcesz wyświetlić? "))
print(f"{element}. elementem ciągu jest liczba {Fibonacci(element)}")
