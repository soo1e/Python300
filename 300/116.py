time = input("현재시간:")
time_new = int(time[-2:])

if time_new == 0:
    print("정각 입니다.")
else:
    print("정각이 아닙니다")
