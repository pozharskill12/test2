time = int(input("Введи время:"))
minutes = time * 60
if time <= 24.00:
    print(minutes)
else:
    print("Время некорректно")
print(minutes * 60)