import random


class SeaBattle:
    def __init__(self):
        self.bot_board_without_ship = None
        self.bot_board_with_ship = None
        self.player_board = None
        self.create_boards()

    # CREATING AND FILLING DEFAULT BOARDS
    def create_boards(self):
        player_board = [['-' for _ in range(12)] for _ in range(12)]
        bot_board_with_ship = [['-' for _ in range(12)] for _ in range(12)]
        bot_board_without_ship = [['-' for _ in range(12)] for _ in range(12)]

        player_board[0][0] = bot_board_with_ship[0][0] = bot_board_without_ship[0][0] = '/'
        player_board[0][11] = bot_board_with_ship[0][11] = bot_board_without_ship[0][11] = '/'

        player_board[11][0] = bot_board_without_ship[11][0] = bot_board_with_ship[11][0] = '/'
        player_board[11][11] = bot_board_without_ship[11][11] = bot_board_with_ship[11][11] = ' /'

        for i in range(1, 11):
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            player_board[11][i] = bot_board_without_ship[11][i] = bot_board_with_ship[11][i] = '/'
            player_board[i][11] = ' /'
            player_board[0][i] = bot_board_with_ship[0][i] = bot_board_without_ship[0][i] = i
            player_board[i][0] = bot_board_without_ship[i][0] = bot_board_with_ship[i][0] = letters[i - 1]
            bot_board_without_ship[i][11] = bot_board_with_ship[i][11] = ' /'

        self.player_board = player_board
        self.bot_board_with_ship = bot_board_with_ship
        self.bot_board_without_ship = bot_board_without_ship

        self.fill_with_ships(self.bot_board_with_ship)
        self.fill_with_ships(self.player_board)
        self.print_boards(self.player_board, self.bot_board_without_ship, self.bot_board_with_ship)

    # PRINT BOARDS
    @staticmethod
    def print_boards(player, bot_without_ship, bot_with_ship):
        print('Your field                Bot field without ships   Bot field with ships')
        for i in range(len(player)):
            for j in range(len(player[i])):
                print(player[i][j], end=' ')
            print(' ', end='')
            for k in range(len(bot_without_ship[i])):
                print(bot_without_ship[i][k], end=' ')
            print(' ', end='')
            for p in range(len(bot_with_ship[i])):
                print(bot_with_ship[i][p], end=' ')
            print()

    # FILLING WITH SHIPS
    def fill_with_ships(self, matrix):
        # SINGLE-DECK
        count_of_cells = 4
        while count_of_cells > 0:
            temp_row_index = random.randint(1, 10)
            temp_col_index = random.randint(1, 10)
            if self.is_fit_for_one(temp_row_index, temp_col_index, matrix):
                matrix[temp_row_index][temp_col_index] = '#'
                count_of_cells -= 1

        # DOUBLE-DECK
        count_of_cells = 6
        while count_of_cells > 0:
            temp_row_index = random.randint(1, 10)
            temp_col_index = random.randint(1, 10)
            while True:
                choice_of_direction = random.randint(1, 4)
                # 1 - right, 2 - down, 3 - left, 4 - up

                if matrix[temp_row_index][temp_col_index] == '#':
                    break

                match choice_of_direction:
                    case 1:
                        if self.is_fit_for_two_right(temp_row_index, temp_col_index, matrix):
                            matrix[temp_row_index][temp_col_index] = matrix[temp_row_index][temp_col_index + 1] = '#'
                            count_of_cells -= 2
                            break
                    case 2:
                        if self.is_fit_for_two_down(temp_row_index, temp_col_index, matrix):
                            matrix[temp_row_index][temp_col_index] = matrix[temp_row_index + 1][temp_col_index] = '#'
                            count_of_cells -= 2
                            break
                    case 3:
                        if self.is_fit_for_two_left(temp_row_index, temp_col_index, matrix):
                            matrix[temp_row_index][temp_col_index] = matrix[temp_row_index][temp_col_index - 1] = '#'
                            count_of_cells -= 2
                            break
                    case 4:
                        if self.is_fit_for_two_up(temp_row_index, temp_col_index, matrix):
                            matrix[temp_row_index][temp_col_index] = matrix[temp_row_index - 1][temp_col_index] = '#'
                            count_of_cells -= 2
                            break
                break

        # THREE-DECK

    # CHECKS IF THE GIVEN PLACE IS SUITABLE FOR A SINGLE-DECK SHIP
    @staticmethod
    def is_fit_for_one(row, col, matrix):
        if matrix[row][col] == '-' and matrix[row - 1][col - 1] != '#' and matrix[row - 1][col] != '#' and \
                matrix[row - 1][col + 1] != '#' and matrix[row][col - 1] != '#' and matrix[row][col + 1] != '#' and \
                matrix[row + 1][col - 1] != '#' and matrix[row + 1][col] != '#' and matrix[row + 1][col + 1] != '#':
            return True
        return False

    @staticmethod
    def is_fit_for_two_right(row, col, matrix):
        if matrix[row][col] == '-' and matrix[row][col + 1] == '-' and matrix[row - 1][col - 1] != '#' and \
                matrix[row][col - 1] != '#' and matrix[row + 1][col - 1] != '#' and matrix[row + 1][col] != '#' and \
                matrix[row - 1][col] != '#' and matrix[row - 1][col + 1] != '#' and matrix[row + 1][col + 1] != '#' \
                and matrix[row - 1][col + 2] != '#' and matrix[row][col + 2] != '#' and matrix[row + 1][col + 2] != '#':
            return True
        return False

    def is_fit_for_two_left(self, row, col, matrix):
        return self.is_fit_for_two_right(row, col - 1, matrix)

    @staticmethod
    def is_fit_for_two_down(row, col, matrix):
        if matrix[row][col] == '-' and matrix[row + 1][col] == '-' and matrix[row - 1][col - 1] != '#' and \
                matrix[row - 1][col] != '#' and matrix[row - 1][col + 1] != '#' and matrix[row][col - 1] != '#' and \
                matrix[row][col + 1] != '#' and matrix[row + 1][col - 1] != '#' and matrix[row + 1][col + 1] != '#' \
                and matrix[row + 2][col - 1] != '#' and matrix[row + 2][col] != '#' and matrix[row + 2][col + 1] != '#':
            return True
        return False

    def is_fit_for_two_up(self, row, col, matrix):
        return self.is_fit_for_two_down(row - 1, col, matrix)


if __name__ == '__main__':
    game = SeaBattle()
