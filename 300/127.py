input = input("주민등록번호 : ")
new_int = int(input[7])
print(new_int)
if new_int in [1, 3]:
    print("남자")
elif new_int in [2, 4]:
    print("여자")
else:
    print("누구세요")