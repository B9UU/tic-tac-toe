# saving user inpute
data = {
    1:'',
    2:'',
    3:'',
    4:'',
    5:'',
    6:'',
    7:'',
    8:'',
    9:'',
    
}
#game board
def gameboard():
    layer = f'''
{data.get(1)} | {data.get(2)} | {data.get(3)}
---------
{data.get(4)} | {data.get(5)} | {data.get(6)}
---------
{data.get(7)} | {data.get(8)} | {data.get(9)}'''
    print(layer)
def check_the_game():
    global gameon
    for i in range(1,10):
        dd = 0
        if data[i] == '':
            dd += 1
            continue
        if dd != 9:
            return True
        else:
            return False
            
def something(number,player):
    nn = True
    while nn:
        if data[number] !='':
            print('youre pick all ready in the table')
            number = int(input('Pick a number from 1-9 for youre next mouve: '))
        elif type(number) is not int:
            print('Not a number')
            number = int(input('Pick a number from 1-9 for youre next mouve: '))
        else:    
            data[number] = player
            whowins(data,player)
            nn = False


def whowins(da, play):
    global gameon
    if check_the_game() is False:
        print('ta3adol azbi')
        gameboard()
        gameon = False
    elif da[1] == play and da[2] == play and da[3] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[4] == play and da[5] == play and da[6] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[7] == play and da[8] == play and da[9] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[1] == play and da[4] == play and da[7] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[2] == play and da[5] == play and da[8] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[3] == play and da[6] == play and da[9] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[1] == play and da[5] == play and da[9] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False
    elif da[3] == play and da[5] == play and da[7] == play:
        print(f'{play} Wins')
        gameboard()
        gameon = False

gameon = True
while gameon:
    
    gameboard()
    o_player = message = int(input('O player Pick a number from 1-9 for youre next mouve: '))
    
    dd= something(o_player,'O')
    if gameon:
        gameboard()
        x_player = message = int(input('X player Pick a number from 1-9 for youre next mouve: '))
        dd= something(x_player,'X')
    

