my_list = ["가", "나", "다", "라"]

for i in [0,1,2]:
    print(my_list[i], my_list[i+1])

print("---------------")

for i in range( len(my_list) - 1 ) :
    print(my_list[i], my_list[i+1])
