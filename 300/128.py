# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라.

new_str = input("주민등록번호 :")
new_str2 = new_str[8:10]
new_int = int(new_str2)
print(new_str2)

if 0<= new_int <= 8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")