x = int(input("Введите число (от 0 до 255): "))
count = int(input("Введите количество прогонов: "))    #сколько раз полностью преобразовать вектор
if x < 0 | x > 255: 
    print("Неправильное число")
else:
    vec = [['111', '110', '101', '100', '011', '010', '001', '000'],  ['0', '0', '0', '0', '0', '0', '0', '0']]
    for i in reversed(range(8)):
        vec[1][i] = str(x % 2)
        x = x // 2


    y = []  
    z = [] 


    y.append(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])


    for k in range(count):
		for i in range(len(y[0])):
			if i == 0:
				string = "0" + y[k][i] + y[k][i + 1]; 
			elif i == (len(y[0]) - 1):
				string  =  y[k][i - 1] + y[k][i] + "0"; 
			else:
				string  =  y[k][i - 1] + y[k][i] + y[k][i + 1]
			for j in range(8):
				if string == vec[0][j]:
					z.append(vec[1][j]);


        y.append(list(z))
        z.zlear()
    

    for i in range(count + 1):
        print(*y[i])
