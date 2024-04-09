# Zdefiniowanie tablicy i pierwszych dwóch elementów
fib = []
fib.append(1)
fib.append(1)

# funkcja rekurencyjna ciągu fibonacciego
def Fibonacci(num):
    if num <= 0:
        return -1
    elif num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

if __name__ == "__main__":
    element = int(input("Który element ciągu chcesz wyświetlić? "))
    print(f"{element}. elementem ciągu jest liczba {Fibonacci(element)}")
