print("Введите первое нечёткое число (три его параметра {a, x, b}, где a < x < b), разделяя пробелами:")
a = input().split()
print("Введите первое нечёткое число (три его параметра {a, x, b}, где a < x < b), разделяя пробелами:")
b = input().split()

A = []
B = []

#проверка введённых параметров первого нечёткого числа
for i in a:
     A.append(float(i))

#проверка введённых параметров второго нечёткого числа
for i in b:
    B.append(float(i))

C = [round((A[0] - B[2]), 2), round((A[1] - B[1]), 2), round((A[2] - B[0]), 2)]
print("Первое нечёткое число:", A)
print("Второе нечёткое число:", B)
print("Разность нечётких чисел:", A, "-", B)
print("Ответ:", C)
