def calculate_structure_sum (a):
    summa = []
    if isinstance(a, int):
        summa.append(a)
    elif isinstance(a, str):
        summa.append(int(len(a)))
    elif isinstance(a, (list, tuple, set)):
        for i in a:
            summa.append(calculate_structure_sum(i))
    elif isinstance(a, dict):
        for j in list(a.items()):
            summa.append(calculate_structure_sum(j))
    return sum(summa)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)