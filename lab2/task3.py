import math
hall = int(input("Введите количество:"))
hall2 = int(input("Введите количество:"))
hall3 = int(input("Введите количество:"))
hall4 = int(input("Введите количество:"))
allHall = hall / 3 + hall2 / 3 + hall3 / 3 + hall4 / 3
print(math.ceil(allHall))