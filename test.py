# player's class
class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    

# saving player inpute
saving_inpute = dict()
def who_wins(play):

    if saving_inpute.get(1) == play and saving_inpute.get(2) == play and saving_inpute.get(3) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(4) == play and saving_inpute.get(5) == play and saving_inpute.get(6) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(7) == play and saving_inpute.get(8) == play and saving_inpute.get(9) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(1) == play and saving_inpute.get(4) == play and saving_inpute.get(7) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(2) == play and saving_inpute.get(5) == play and saving_inpute.get(8) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(3) == play and saving_inpute.get(6) == play and saving_inpute.get(9) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(1) == play and saving_inpute.get(5) == play and saving_inpute.get(9) == play:
        print(f'{play} Wins')
        return False
    elif saving_inpute.get(3) == play and saving_inpute.get(5) == play and saving_inpute.get(7) == play:
        print(f'{play} Wins')
        return False
    elif len(saving_inpute) == 9:
        print('ta3adol')
        return False
    else:
        return True

# player inpute
def player_inpute(mouve,player):
    nn = True
    while nn:
        if saving_inpute.get(mouve) is not None:
            print('youre choice all ready in the table')
            mouve = int(input(f'{player} Turn Pick a number from 1-9 for youre next mouve: '))
        elif type(mouve) is not int:
            print('Not a number')
            mouve = int(input(f'{player} Turn Pick a number from 1-9 for youre next mouve: '))
        elif mouve > 9 or mouve < 1:
            print('please picj a number from 1-9')
            mouve = int(input(f'{player} Turn Pick a number from 1-9 for youre next mouve: '))
        else:    
            saving_inpute[mouve] = player
            nn = False
            return who_wins(player)
            
def gameboard():
    layer = f'''
{saving_inpute.get(1,'')} | {saving_inpute.get(2,'')} | {saving_inpute.get(3,'')}
---------
{saving_inpute.get(4,'')} | {saving_inpute.get(5,'')} | {saving_inpute.get(6,'')}
---------
{saving_inpute.get(7,'')} | {saving_inpute.get(8,'')} | {saving_inpute.get(9,'')}'''
    print(layer)


currentplayer = 'X'
gameon = True
while gameon:
    gameboard()
    mouve = int(input(f'{currentplayer} Turn Pick a number from 1-9 for youre next mouve: '))
    gameon = player_inpute(mouve,currentplayer)
    if not gameon:
        gameboard()
    if currentplayer == 'X':
        currentplayer = 'O'
    else:
        currentplayer = "X"


