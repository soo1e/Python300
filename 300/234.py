def pickup_even(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(pickup_even([3, 4, 5, 6, 7, 8]))
