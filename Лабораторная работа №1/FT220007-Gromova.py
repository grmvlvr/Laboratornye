import math

a, b = float(input ("Введи число:")), float(input ("Введи число:"))

print("Сумма:", a + b,"\n","Разность:", a - b,"\n","Произведение:", a * b,"\n","Среднее арифметическое:", (a+b)/2,"\n","Разность максимального и минимального числа по модулю:", max(abs(a),abs(b)) - min(abs(a),abs(b)),"\n",'Частное', round(a/b,2))
