def get_matrix (n, m, value):
    matrix = []
    matrixdop = []
    for i in (0, int(n)):
        matrixdop.append(value)
        for j in range(0, int(m)):
            matrix.append(matrixdop)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
