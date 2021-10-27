iterinput = input("Введите знак +, -, /, *:")
number1 = float(input("number1 =" ))
number2 = float(input("number1 ="))
if iterinput == "+":
    print(number1 + number2)
if iterinput == "/":
    print(number1 // number2)
if iterinput == "*":
    print(number1 * number2)
if iterinput == "-":
    print(number1 - number2)
else:
    print("Неверный ввод")