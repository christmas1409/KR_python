n = int(input("Введите количество колец: "))


def hanoi(n, x, y, z):
    if n > 0:
        hanoi(n - 1, x, z, y)
        print("Переместить кольцо c", x, "на", z)
        hanoi(n - 1, y, x, z)


hanoi(n, "1", "2", "3")
