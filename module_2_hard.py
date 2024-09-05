n = int(input("Введите число от 3 до 20 включительно:"))
password = []
if 3 <= n <= 20:
    for i in range (1, int(n)):
        for j in range (1, int(n)):
            x = i + j
            if n % x ==0 and j > i:
                password.append(i)
                password.append(j)
    print(password)
else:
    print ("Число не входит в заданный промежуток")