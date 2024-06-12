fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

new_list = (list(fruit.keys()))
season = input("제가 좋아하는 계절은 : ")
if season in new_list:
    print("정답입니다.")
else:
    print("오답입니다.")
