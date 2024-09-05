def get_matrix (n, m, value):
    matrix = []
    matrixdop = []
    for i in range (int(m)):
        matrixdop.append(value)
    for j in range (int(n)):
        matrix.append(matrixdop)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
