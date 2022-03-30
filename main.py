# this is the main file using all the other files to make the game
import pygame
from grid import Grid

pygame.init()

# we create the Grid object
grid = Grid()

# we set the variables
game_ended = False
pygame.display.set_caption("Connect 4")
screen = pygame.display.set_mode((720, 480))
screen.fill((100, 155, 136))
icon = pygame.image.load("puissance4_icone-_2_.ico")
pygame.display.set_icon(icon)

# we show some text : which player is which and who has to play
arial_font = pygame.font.SysFont("arial", 30)

player_a_text = arial_font.render("Player 1 : ", True, (0, 0, 0))
pygame.draw.rect(screen, (255, 255, 0), (675, 160, 35, 20))
screen.blit(player_a_text, (565, 150))

player_b_text = arial_font.render("Player 2 : ", True, (0, 0, 0))
pygame.draw.rect(screen, (255, 0, 0), (675, 210, 35, 20))
screen.blit(player_b_text, (565, 200))

player_2 = arial_font.render("2", True, (0, 0, 0))
player_1 = arial_font.render("1", True, (0, 0, 0))
screen.blit(player_1, (190, 30))

player_turn = arial_font.render("Player turn : ", True, (0, 0, 0))
screen.blit(player_turn, (50, 30))

# we draw the board
pygame.draw.rect(screen, (16, 52, 166), (100, 100, 450, 350))

# we change the corners
pygame.draw.rect(screen, (100, 155, 136), (100, 100, 30, 30))
pygame.draw.circle(screen, (16, 52, 166), (130, 130), 30)

pygame.draw.rect(screen, (100, 155, 136), (520, 100, 30, 30))
pygame.draw.circle(screen, (16, 52, 166), (520, 130), 30)

# we draw the circle (holes in the grid)
for i in range(140, 440, 55):
    for j in range(143, 543, 60):
        pygame.draw.circle(screen, (100, 155, 136), (j, i), 21)

# we launch the mainloop
while True:
    # we only refresh the screen here
    pygame.display.flip()
    for event in pygame.event.get():

        # if the user quit
        if event.type == pygame.QUIT:
            game_ended = True
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_ended is False:

                pos = pygame.mouse.get_pos()
                # we count the column starting on the left one
                # if the click is in the first column
                # only this condition is commented because they are all the same
                if 164 > pos[0] > 122:
                    # we try to edit the grid
                    played = grid.play(0)
                    if played is not None:
                        # if the grid is edited we change the player who has to play
                        pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                        screen.blit(player_2, (190, 30))

                        # if the player 1 has played we draw the yellow token
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (143, played[2]*55+140), 21)

                        # else we draw the red token
                        elif played[0] is True and played[1] == 2:

                            pygame.draw.circle(screen, (255, 0, 0), (143, played[2]*55+140), 21)

                        # we check if any of the player has won
                        grid_checked = grid.check_win()

                        # if a player has won we stop the game and wait for the user to quit the game
                        if grid_checked[0] is True:
                            game_ended = True

                            # we show which player has won
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the second column
                elif 224 > pos[0] > 182:
                    played = grid.play(1)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (203, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (203, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the third column
                elif 284 > pos[0] > 242:
                    played = grid.play(2)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (263, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (263, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the forth column
                elif 344 > pos[0] > 302:
                    played = grid.play(3)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (323, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (323, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the fifth column
                elif 404 > pos[0] > 362:
                    played = grid.play(4)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (383, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (383, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the sixth column
                elif 464 > pos[0] > 422:
                    played = grid.play(5)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (443, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (443, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

                # if the click is in the seventh column
                elif 524 > pos[0] > 482:
                    played = grid.play(6)
                    if played is not None:
                        if played[0] is True and played[1] == 1:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_2, (190, 30))
                            pygame.draw.circle(screen, (255, 255, 0), (503, played[2] * 55 + 140), 21)

                        elif played[0] is True and played[1] == 2:
                            pygame.draw.rect(screen, (100, 155, 136), (190, 30, 50, 50))
                            screen.blit(player_1, (190, 30))
                            pygame.draw.circle(screen, (255, 0, 0), (503, played[2] * 55 + 140), 21)

                        grid_checked = grid.check_win()
                        if grid_checked[0] is True:
                            game_ended = True
                            win_text = arial_font.render("Player {0} won !".format(grid_checked[1]), True,
                                                         (0, 0, 0))
                            screen.blit(win_text, (250, 25))

