# this file contain the class grid which handle the core of the game : the grid (not graphic interface)


class Grid:
    """
    This class can :
    """

    def __init__(self):
        self.main_list = [[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          ]  # 0 stands for nothing, 1 for the first payer and 2 for the second
        # player
        self.first_player_turn = True
        self.nb_tokens_played = 0

    def check_win(self):
        """
        This function checks if any of the player has won, in this function in the for loops the y and the x represent
        the coordinates in the grid
        :return: (True, 1) if the player 1 has won
                 (True, 2) if the player 2 has won
                 (False, None) if any of the player has won
        """
        win = (False, None)
        # we check the diagonals
        for y in range(3, 6):
            for x in range(4):
                if self.main_list[y][x] == self.main_list[y - 1][x + 1] == self.main_list[y - 2][x + 2] == self.main_list[y - 3][x + 3]:
                    if self.main_list[y][x] != 0:
                        win = (True, self.main_list[y][x])

        for y in range(3):
            for x in range(4):
                if self.main_list[y][x] == self.main_list[y + 1][x + 1] == self.main_list[y + 2][x + 2] == self.main_list[y + 3][x + 3]:
                    if self.main_list[y][x] != 0:
                        win = (True, self.main_list[y][x])

        # we check the lines
        for y in range(6):
            for x in range(4):
                if self.main_list[y][x] == self.main_list[y][x + 1] == self.main_list[y][x + 2] == self.main_list[y][x + 3]:
                    if self.main_list[y][x] != 0:
                        win = (True, self.main_list[y][x])

        # we check the columns
        for x in range(7):
            for y in range(3):
                if self.main_list[y][x] == self.main_list[y + 1][x] == self.main_list[y + 2][x] == self.main_list[y + 3][x]:
                    if self.main_list[y][x] != 0:
                        win = (True, self.main_list[y][x])

        return win

    def play(self, x):
        """

        :param x:
        :return: True if the player has played, False if not
        """
        last_case_empty = (100, 100)
        for j in range(len(self.main_list)):
            if self.main_list[j][x] == 0:
                last_case_empty = (x, j)

        if last_case_empty != (100, 100) and self.first_player_turn is True:
            self.main_list[last_case_empty[1]][last_case_empty[0]] = 1
            self.first_player_turn = False
            return True, 1, last_case_empty[1]

        elif last_case_empty != (100, 100) and self.first_player_turn is False:
            self.main_list[last_case_empty[1]][last_case_empty[0]] = 2
            self.first_player_turn = True
            return True, 2, last_case_empty[1]
