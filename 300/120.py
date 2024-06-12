fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

fruit_new = list(fruit.values())
ans = input("좋아하는 과일은? ")
if ans in fruit_new:
    print("정답입니다.")
else:
    print("오답입니다.")