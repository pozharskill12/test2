def choiceGun ():
    gun = {"vdR":{"speed":2, "distation":1200}, "pM":{"speed": 3, "distation":200}, "ak47":{"speed": 5, "distation":400}}

    quest1 = input("Какое оружие вы предпочитатете?  : ")
    if quest1 == "Dragunova" or quest1 =="Драгунова":
        myChoiceGun = gun["vdR"]
    elif  quest1 == "Makarova" or quest1 == "Макарова":
        myChoiceGun = gun["pM"]
    elif quest1 == "ak47" or quest1 == "Калаш":
        myChoiceGun = gun["ak47"]
    else:
        quest2 = input("Выбери из предлагаемого\n 1. Драгунова\n 2. Макарова\n 3.ак47\n")
        
    if quest2 == "Dragunova" or quest2 =="Драгунова" or quest2 == "1":
            myChoiceGun = gun["vdR"]
    elif  quest2 == "Makarova" or quest2 == "Макарова" or quest2 == "2":
            myChoiceGun = gun["pM"]
    elif quest2 == "ak47" or quest2 == "Калаш" or quest2 == "3":
            myChoiceGun = gun["ak47"]

    return myChoiceGun




def deathGun (longShot):
    
    myChoice = choiceGun()
    print("Ваше оружее поразит врага через " + str(myChoice['speed'] / longShot )+ " секунд")
    

deathGun(200)