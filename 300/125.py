phone = input("휴대전화 번호 입력 : ")
first = phone[0:3]

if first == '011':
    user = "SKT"
elif first == '016':
    user = "KT"
elif first == '019':
    user = "LGU"
else:
    user = "알수없는"

print("당신은", user, "사용자입니다.")