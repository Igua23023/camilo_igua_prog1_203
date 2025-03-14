def fib(n):
    x, b = 0, 1
    while x <= n:
        print(x, end=" ")
        x, b = b, x + b
x = int(input("Ingresa un valor : "))
fib(n)
