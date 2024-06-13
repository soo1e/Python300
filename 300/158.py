리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for str in 리스트:
    str_new = str.split(".")
    print(str_new[0])