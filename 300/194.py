data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []

for i in data:
    new_list = []
    for j in i:
        new_list.append(j * 1.00014)
    result.append(new_list)