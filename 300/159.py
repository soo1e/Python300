리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for str in 리스트:
    new_str = str.split(".")[1]

    if new_str == 'h':
        print(str)
