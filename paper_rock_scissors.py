import random;

#print(random.randrange(0,2));
#print(random.randint(0,2));

def name_to_number(name):
    number = "";
    if(name == "камень"):
        number = 0;
    elif(name == "бумага"):
        number = 1;
    elif(name == "ножницы"):
        number = 2;
    else:
        print("Вы ошиблись в своём выборе, такого элемента не существует.");
        number = "";
    return number;

def number_to_name(number):
    nmae = "";
    if(number == 0):
        name = "камень";
    elif(number == 1):
        name = "бумага";
    elif(number == 2):
        name = "ножницы";
    else:
        name = "";
    return name;

def rock_scissors_paper(player1_choice):
    player2_choice = number_to_name(random.randrange(0,3));
    print("Выбор игрока 1: {0:s}\nВыбор игрока 2: {1:s}".format(player1_choice, player2_choice));
    print( "Ничья!" if (((name_to_number(player2_choice)-name_to_number(player1_choice)) % 3) == 0) else ("Игрок 2 выиграл!" if (((name_to_number(player2_choice)-name_to_number(player1_choice)) % 3) == 1) else "Игрок 1 выиграл!" ));
    print("\n");
    '''
    ch = int(input("1. Попробовать снова.\n0. Выход.\n"));
    if(ch == 0):
        print("Всего доброго!");
    elif(ch == 1):
        rock_scissors_paper(number_to_name(random.randrange(0,3)));'''
    rock_scissors_paper(number_to_name(random.randrange(0,3)));
    
rock_scissors_paper(number_to_name(random.randrange(0,3)));
