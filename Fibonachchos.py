#Числовой ряд Фибоначчи
fib1 = 1
fib2 = 1

print("Номер элемента ряда Фибоначчи:")
n = int(input())

if n < 2:
    exit()

print(fib1, end=' ')
print(fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print()
