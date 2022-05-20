#Игра кресики нолики на 2-ух игроков, ходы осуществляются поочерёдно.

board = list(range(1,9+1))

def draw_board(board):#Ф-ия рисования игрового поля
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def take_input(player_token):#Ф-ия получения пользовательского выбора
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели номер ячейки?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")

def check_win(board):#Ф-ия проверки победы. 
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))#выигрышные комбинации
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False#По умолчанию пока играем никто ещё не выйграл:)
    while not win:#Если победы до сих пор не случилось рисуем доску
        draw_board(board)#Рисуем доску
        if counter % 2 == 0:#Счётчик очерёдности
            take_input("X")#Предлагаем сходить игроку ходящему Х
        else:
            take_input("O")#Предлагаем сходить игроку ходящему О
        counter += 1#После очередного хода увеличиваем счётчик
        if counter > 4:#Проверка на минимально возможное число ходов для победы, чтобы не вызывать функцию проверки победы бесполезно
            tmp = check_win(board)#Вызов ф-ии проверки победы
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:#При полном заполнении в случае невыигрыша одного из игроков случается ничья
            print ("Ничья!")#Извещение о ничьей
            break
    draw_board(board)
   
main(board)