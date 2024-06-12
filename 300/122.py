input = int(input("score: "))
if 0 <= input <= 20:
    grade = "E"
elif 21 <= input <= 40:
    grade = "D"
elif 41 <= input <= 60:
    grade = "C"
elif 61 <= input <= 80:
    grade = "B"
elif 81 <= input <= 100:
    grade = "A"
else:
    grade = "error"

print("grade is", grade)