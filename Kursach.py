def raschet(a, b):
    A = []  # создать пустой список A
    B = []  # создать пустой список В

    for i in a:
        A.append(float(i))

    for i in b:
        B.append(float(i))

    C = round((A[0] - B[2]), 2), round((A[1] - B[1]), 2), round((A[2] - B[0]), 2)  
    return C


a = input("Введите первое нечёткое число (три его параметра {a, x, b}, где a < x < b), разделяя пробелами: ").split()
b = input("Введите второе нечёткое число (три его параметра {a, x, b}, где a < x < b), разделяя пробелами: ").split()
print("Результат:", raschet(a, b))
