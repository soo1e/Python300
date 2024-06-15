def printmxn(str, num):
    chunk_num = int(len(str)/num)
    for x in range(chunk_num + 1):
        print(str[x * num : x * num + num])

printmxn("아이엠어보이유알어걸", 3)
