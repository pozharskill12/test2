figure = input('Тип фигуры:\n')
x1,y1 = int(input('Позиция фигуры в данный момент:\n' )), int(input())

x2,y2 = int(input('Допустимый ход:\n')), int(input())


def Chess(unit):
    if unit == 'пешка': #пешка 
        return abs(y1 - y2) <= 1 and x1 == x2

    if unit == 'король': #Король
        return -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1

    if unit == 'тура': #Тура
        return x1 == x2 or y1 == y2  

    if unit == 'слон': #Слон
        return  abs(x1 - x2) == abs(y1 - y2) 

    if unit == 'конь': #Конь
        return 1 <= abs(x1 - x2) <= 2  and 1 <= abs(y1 - y2) <= 2

    if unit == 'ферзь': #Ферзь
        return abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2   

    raise ValueError('Че ты сказал? : {}'.format(unit))

print(Chess(figure))
