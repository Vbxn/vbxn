board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
board_width = 3


def show_board():  # вывод поля в консоль
    for i in range(board_width):
        print(board[i * 3], board[1 + i * 3], board[2 + i * 3])


def game_turn(target_choice, player):  # определение хода
    if target_choice > 9 or target_choice < 1 or board[target_choice - 1] in ("X", "O"):
        return False

    else:
        board[target_choice-1] = player
        return True


def victory_check():  # проверка состояния игры на наличие выигрышной комбинации

    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Победные комбинации:
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # горизонтально, вертикально,
                    (0, 4, 8), (2, 4, 6))             # диагонально.

    for win in combinations:
        if board[win[0]] == board[win[1]] == board[win[2]]:
            return board[win[0]]
    return False


def game_process():
    player = "X"
    turn = 1
    show_board()

    while turn < 10 and not victory_check():
        while True:
            target_choice = input(f'Ход игрока {player}. Введите номер клетки: ')
            if target_choice.isdigit():  # Проверяем, является ли ввод числом
                target_choice = int(target_choice)
                break
            else:
                print("Неверный ввод. Пожалуйста, введите цифру.")

        if game_turn(target_choice, player):
            print("Ход успешен")

            player = "O" if player == "X" else "X"

            show_board()
            turn += 1
        else:
            print("Ход невозможен, попробуйте снова.")

    print(f"Победа за {victory_check()}" if victory_check() else "Ничья")


print("Добро пожаловать в крестики-нолики!")
game_process()