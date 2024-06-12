ExRate = {"달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171}

Ex = input("입력 : ")
num, currency = Ex.split()
print(float(num) * ExRate[currency], "원")