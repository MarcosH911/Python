import pygame
from sys import exit


class Square:

    def __init__(self, position):
        self.x_surface = pygame.image.load('Data/X.png').convert()
        self.x_surface = pygame.transform.scale(self.x_surface, (200, 200))
        self.o_surface = pygame.image.load('Data/O.png').convert()
        self.o_surface = pygame.transform.scale(self.o_surface, (200, 200))
        self.blank_square_surface = pygame.image.load('Data/Blank_Square.png').convert()
        self.blank_square_surface = pygame.transform.scale(self.blank_square_surface, (200, 200))
        self.blank_square_rect = self.blank_square_surface.get_rect(topleft=position)
        self.x_rect = self.x_surface.get_rect(topleft=position)
        self.o_rect = self.o_surface.get_rect(topleft=position)

    def draw_square(self, square_type):
        if square_type == 'Blank':
            screen.blit(self.blank_square_surface, self.blank_square_rect)
        elif square_type == 'X':
            screen.blit(self.x_surface, self.x_rect)
        elif square_type == 'O':
            screen.blit(self.o_surface, self.o_rect)

    def player_input(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.blank_square_rect.collidepoint(pygame.mouse.get_pos()):
                return True


class TopScreen:
    global x_score, o_score

    def __init__(self):
        self.x_image = pygame.image.load('Data/X_2.png').convert_alpha()
        self.x_image_surface = pygame.transform.rotozoom(self.x_image, 0, 0.15)
        self.x_image_rect = self.x_image_surface.get_rect(topright=(550, 0))
        self.o_image = pygame.image.load('Data/O_2.png').convert_alpha()
        self.o_image_surface = pygame.transform.rotozoom(self.o_image, 0, 0.14)
        self.o_image_rect = self.o_image_surface.get_rect(topright=(550, 100))
        self.x_score_font = pygame.font.Font('Data/MotionControl-Bold.otf', 150)
        self.o_score_font = pygame.font.Font('Data/MotionControl-Bold.otf', 150)

        self.x_colored_image = pygame.image.load('Data/X_3.png').convert()
        self.x_turn_surface = pygame.transform.rotozoom(self.x_colored_image, 0, 0.20)
        self.x_turn_rect = self.x_turn_surface.get_rect(center=(270, 100))
        self.o_colored_image = pygame.image.load('Data/O_3.png').convert()
        self.o_turn_surface = pygame.transform.rotozoom(self.o_colored_image, 0, 0.183)
        self.o_turn_rect = self.o_turn_surface.get_rect(center=(270, 100))
        self.turn_font = pygame.font.Font('Data/MotionControl-Bold.otf', 120)
        self.turn_font_surface = self.turn_font.render('TURN', True, (0, 0, 60))
        self.turn_font_rect = self.turn_font_surface.get_rect(midleft=(0, 100))

    def draw_score(self):
        x_score_font_surface = self.x_score_font.render(str(x_score), False, (0, 0, 60))
        x_score_font_rect = x_score_font_surface.get_rect(midright=(625, 50))
        o_score_font_surface = self.o_score_font.render(str(o_score), False, (0, 0, 60))
        o_score_font_rect = o_score_font_surface.get_rect(midright=(625, 150))

        screen.blit(self.x_image_surface, self.x_image_rect)
        screen.blit(self.o_image_surface, self.o_image_rect)
        screen.blit(x_score_font_surface, x_score_font_rect)
        screen.blit(o_score_font_surface, o_score_font_rect)

    def draw_turn_x(self):
        screen.blit(self.x_turn_surface, self.x_turn_rect)
        screen.blit(self.turn_font_surface, self.turn_font_rect)

    def draw_turn_o(self):
        screen.blit(self.o_turn_surface, self.o_turn_rect)
        screen.blit(self.turn_font_surface, self.turn_font_rect)


class EndScreen:
    global x_score, o_score

    def __init__(self):

        self.x_image = pygame.image.load('Data/X_2.png').convert_alpha()
        self.x_center_image_surface = pygame.transform.rotozoom(self.x_image, 0, 0.45)
        self.x_center_image_rect = self.x_center_image_surface.get_rect(center=(320, 350))
        self.x_center_font = pygame.font.Font('Data/MotionControl-Bold.otf', 180)
        self.x_center_font_surface = self.x_center_font.render('WINS!', True, (255, 97, 95))
        self.x_center_font_rect = self.x_center_font_surface.get_rect(center=(320, 560))
        self.x_score_image_surface = pygame.transform.rotozoom(self.x_image, 0, 0.25)
        self.x_score_image_rect = self.x_score_image_surface.get_rect(center=(100, 100))
        self.x_score_font = pygame.font.Font('Data/MotionControl-Bold.otf', 250)

        self.o_image = pygame.image.load('Data/O_2.png').convert_alpha()
        self.o_center_image_surface = pygame.transform.rotozoom(self.o_image, 0, 0.40)
        self.o_center_image_rect = self.o_center_image_surface.get_rect(center=(320, 350))
        self.o_center_font = pygame.font.Font('Data/MotionControl-Bold.otf', 180)
        self.o_center_font_surface = self.o_center_font.render('WINS!', True, (62, 197, 243))
        self.o_center_font_rect = self.o_center_font_surface.get_rect(center=(320, 560))
        self.o_score_image_surface = pygame.transform.rotozoom(self.o_image, 0, 0.25)
        self.o_score_image_rect = self.o_score_image_surface.get_rect(center=(420, 100))
        self.o_score_font = pygame.font.Font('Data/MotionControl-Bold.otf', 250)

        self.x_draw_image_surface = pygame.transform.rotozoom(self.x_image, 0, 0.3)
        self.x_draw_image_rect = self.x_draw_image_surface.get_rect(midright=(310, 350))
        self.o_draw_image_surface = pygame.transform.rotozoom(self.o_image, 0, 0.29)
        self.o_draw_image_rect = self.o_draw_image_surface.get_rect(midleft=(330, 350))
        self.draw_font = pygame.font.Font('Data/MotionControl-Bold.otf', 180)
        self.draw_font_surface = self.x_score_font.render('DRAW!', True, (0, 200, 150))
        self.draw_font_rect = self.draw_font_surface.get_rect(center=(320, 560))

    def draw_x_win(self):
        x_score_font_surface = self.x_score_font.render(str(x_score), True, (0, 0, 60))
        x_score_font_rect = x_score_font_surface.get_rect(center=(240, 100))
        o_score_font_surface = self.o_score_font.render(str(o_score), True, (0, 0, 60))
        o_score_font_rect = o_score_font_surface.get_rect(center=(570, 100))

        screen.blit(self.x_center_image_surface, self.x_center_image_rect)
        screen.blit(self.x_center_font_surface, self.x_center_font_rect)
        screen.blit(self.x_score_image_surface, self.x_score_image_rect)
        screen.blit(x_score_font_surface, x_score_font_rect)
        screen.blit(self.o_score_image_surface, self.o_score_image_rect)
        screen.blit(o_score_font_surface, o_score_font_rect)

    def draw_o_win(self):
        o_score_font_surface = self.o_score_font.render(str(o_score), True, (0, 0, 60))
        o_score_font_rect = o_score_font_surface.get_rect(center=(570, 100))
        x_score_font_surface = self.x_score_font.render(str(x_score), True, (0, 0, 60))
        x_score_font_rect = x_score_font_surface.get_rect(center=(240, 100))

        screen.blit(self.o_center_image_surface, self.o_center_image_rect)
        screen.blit(self.o_center_font_surface, self.o_center_font_rect)
        screen.blit(self.o_score_image_surface, self.o_score_image_rect)
        screen.blit(o_score_font_surface, o_score_font_rect)
        screen.blit(self.x_score_image_surface, self.x_score_image_rect)
        screen.blit(x_score_font_surface, x_score_font_rect)

    def draw_draw(self):
        x_score_font_surface = self.x_score_font.render(str(x_score), True, (0, 0, 60))
        x_score_font_rect = x_score_font_surface.get_rect(center=(240, 100))
        o_score_font_surface = self.o_score_font.render(str(o_score), True, (0, 0, 60))
        o_score_font_rect = o_score_font_surface.get_rect(center=(570, 100))

        screen.blit(self.x_draw_image_surface, self.x_draw_image_rect)
        screen.blit(self.o_draw_image_surface, self.o_draw_image_rect)
        screen.blit(self.draw_font_surface, self.draw_font_rect)
        screen.blit(self.o_score_image_surface, self.o_score_image_rect)
        screen.blit(o_score_font_surface, o_score_font_rect)
        screen.blit(self.x_score_image_surface, self.x_score_image_rect)
        screen.blit(x_score_font_surface, x_score_font_rect)


def draw_play_screen():
    play_text_surface = pygame.image.load('Data/Text_Image.png')
    play_text_surface = pygame.transform.rotozoom(play_text_surface, 0, 0.25)
    play_text_rect = play_text_surface.get_rect(center=(320, 100))
    screen.blit(play_button_surface, play_button_rect)
    screen.blit(play_text_surface, play_text_rect)


def check_win_x():
    global x_win
    if squares_dict[square_1] == 'X' and squares_dict[square_2] == 'X' and squares_dict[square_3] == 'X':
        x_win = True
        return draw_line('X Line 1')
    elif squares_dict[square_4] == 'X' and squares_dict[square_5] == 'X' and squares_dict[square_6] == 'X':
        x_win = True
        return draw_line('X Line 2')
    elif squares_dict[square_7] == 'X' and squares_dict[square_8] == 'X' and squares_dict[square_9] == 'X':
        x_win = True
        return draw_line('X Line 3')
    elif squares_dict[square_1] == 'X' and squares_dict[square_4] == 'X' and squares_dict[square_7] == 'X':
        x_win = True
        return draw_line('X Column 1')
    elif squares_dict[square_2] == 'X' and squares_dict[square_5] == 'X' and squares_dict[square_8] == 'X':
        x_win = True
        return draw_line('X Column 2')
    elif squares_dict[square_3] == 'X' and squares_dict[square_6] == 'X' and squares_dict[square_9] == 'X':
        x_win = True
        return draw_line('X Column 3')
    elif squares_dict[square_1] == 'X' and squares_dict[square_5] == 'X' and squares_dict[square_9] == 'X':
        x_win = True
        return draw_line('X Diagonal 1')
    elif squares_dict[square_3] == 'X' and squares_dict[square_5] == 'X' and squares_dict[square_7] == 'X':
        x_win = True
        return draw_line('X Diagonal 2')
    else:
        return None


def check_win_o():
    global o_win
    if squares_dict[square_1] == 'O' and squares_dict[square_2] == 'O' and squares_dict[square_3] == 'O':
        o_win = True
        return draw_line('O Line 1')
    elif squares_dict[square_4] == 'O' and squares_dict[square_5] == 'O' and squares_dict[square_6] == 'O':
        o_win = True
        return draw_line('O Line 2')
    elif squares_dict[square_7] == 'O' and squares_dict[square_8] == 'O' and squares_dict[square_9] == 'O':
        o_win = True
        return draw_line('O Line 3')
    elif squares_dict[square_1] == 'O' and squares_dict[square_4] == 'O' and squares_dict[square_7] == 'O':
        o_win = True
        return draw_line('O Column 1')
    elif squares_dict[square_2] == 'O' and squares_dict[square_5] == 'O' and squares_dict[square_8] == 'O':
        o_win = True
        return draw_line('O Column 2')
    elif squares_dict[square_3] == 'O' and squares_dict[square_6] == 'O' and squares_dict[square_9] == 'O':
        o_win = True
        return draw_line('O Column 3')
    elif squares_dict[square_1] == 'O' and squares_dict[square_5] == 'O' and squares_dict[square_9] == 'O':
        o_win = True
        return draw_line('O Diagonal 1')
    elif squares_dict[square_3] == 'O' and squares_dict[square_5] == 'O' and squares_dict[square_7] == 'O':
        o_win = True
        return draw_line('O Diagonal 2')
    else:
        return None


def draw_line(mode):
    global length, game_on, win_animation
    if mode == 'X Line 1':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((320 - length, 280), (length * 2, 40)), border_radius=20)

    elif mode == 'X Line 2':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((320 - length, 500), (length * 2, 40)), border_radius=20)

    elif mode == 'X Line 3':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((320 - length, 720), (length * 2, 40)), border_radius=20)

    elif mode == 'X Column 1':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((80, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'X Column 2':
        game_on = False
        if length < 295:
            length += 7
            pygame.draw.rect(screen, (150, 0, 0), ((300, 520 - length), (40, length * 2)), border_radius=20)
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((300, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'X Column 3':
        game_on = False
        if length < 295:
            length += 7
            pygame.draw.rect(screen, (150, 0, 0), ((520, 520 - length), (40, length * 2)), border_radius=20)
        else:
            win_animation = False
        pygame.draw.rect(screen, (150, 0, 0), ((520, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'X Diagonal 1':
        game_on = False
        if length < 250:
            length += 7
        else:
            win_animation = False

        point_1 = pygame.math.Vector2(321 + length, 521 + length)
        point_2 = pygame.math.Vector2(319 - length, 519 - length)
        direction_vector = (point_2 - point_1).normalize()
        line_vector = pygame.math.Vector2(-direction_vector.y, direction_vector.x) * 20
        points = [point_1 + line_vector, point_2 + line_vector, point_2 - line_vector, point_1 - line_vector]

        pygame.draw.circle(screen, (150, 0, 0), point_1, 21)
        pygame.draw.circle(screen, (150, 0, 0), point_2, 21)
        pygame.draw.polygon(screen, (150, 0, 0), points)

    elif mode == 'X Diagonal 2':
        game_on = False
        if length < 250:
            length += 7
        else:
            win_animation = False

        point_1 = pygame.math.Vector2(321 - length, 521 + length)
        point_2 = pygame.math.Vector2(319 + length, 519 - length)
        direction_vector = (point_2 - point_1).normalize()
        line_vector = pygame.math.Vector2(-direction_vector.y, direction_vector.x) * 20
        points = [point_1 + line_vector, point_2 + line_vector, point_2 - line_vector, point_1 - line_vector]

        pygame.draw.circle(screen, (150, 0, 0), point_1, 21)
        pygame.draw.circle(screen, (150, 0, 0), point_2, 21)
        pygame.draw.polygon(screen, (150, 0, 0), points)

    elif mode == 'O Line 1':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (0, 150, 255), ((320 - length, 280), (length * 2, 40)), border_radius=20)

    elif mode == 'O Line 2':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (0, 150, 255), ((320 - length, 500), (length * 2, 40)), border_radius=20)

    elif mode == 'O Line 3':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (0, 150, 255), ((320 - length, 720), (length * 2, 40)), border_radius=20)

    elif mode == 'O Column 1':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (0, 150, 255), ((80, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'O Column 2':
        game_on = False
        if length < 295:
            length += 7
        else:
            win_animation = False
        pygame.draw.rect(screen, (0, 150, 255), ((300, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'O Column 3':
        game_on = False
        if length < 295:
            length += 7
        else:
            game_on = False
        pygame.draw.rect(screen, (0, 150, 255), ((520, 520 - length), (40, length * 2)), border_radius=20)

    elif mode == 'O Diagonal 1':
        game_on = False
        if length < 250:
            length += 7
        else:
            win_animation = False

        point_1 = pygame.math.Vector2(321 + length, 521 + length)
        point_2 = pygame.math.Vector2(319 - length, 519 - length)
        direction_vector = (point_2 - point_1).normalize()
        line_vector = pygame.math.Vector2(-direction_vector.y, direction_vector.x) * 20
        points = [point_1 + line_vector, point_2 + line_vector, point_2 - line_vector, point_1 - line_vector]

        pygame.draw.circle(screen, (0, 150, 255), point_1, 21)
        pygame.draw.circle(screen, (0, 150, 255), point_2, 21)
        pygame.draw.polygon(screen, (0, 150, 255), points)

    elif mode == 'O Diagonal 2':
        game_on = False
        if length < 250:
            length += 7
        else:
            win_animation = False

        point_1 = pygame.math.Vector2(321 - length, 521 + length)
        point_2 = pygame.math.Vector2(319 + length, 519 - length)
        direction_vector = (point_2 - point_1).normalize()
        line_vector = pygame.math.Vector2(-direction_vector.y, direction_vector.x) * 20
        points = [point_1 + line_vector, point_2 + line_vector, point_2 - line_vector, point_1 - line_vector]

        pygame.draw.circle(screen, (0, 150, 255), point_1, 21)
        pygame.draw.circle(screen, (0, 150, 255), point_2, 21)
        pygame.draw.polygon(screen, (0, 150, 255), points)


pygame.init()
screen = pygame.display.set_mode((640, 840))
screen.fill((0, 0, 60), ((0, 200), (640, 840)))
screen.fill((0, 200, 150), ((0, 0), (640, 200)))
frame_update = pygame.time.Clock()

pygame.display.set_caption('Tic-Tac-Toe')
icon_image = pygame.image.load('Data/Icon.png')
pygame.display.set_icon(icon_image)

play_again_surface = pygame.image.load('Data/Play_Again.png').convert_alpha()
play_again_rect = play_again_surface.get_rect(center=(320, 760))

play_button_surface = pygame.image.load('Data/playbutton.png')
play_button_surface = pygame.transform.rotozoom(play_button_surface, 0, 1.5)
play_button_rect = play_button_surface.get_rect(center=(320, 500))

black_screen_surface = pygame.Surface((640, 840))
black_screen_surface.fill((0, 0, 0))
black_screen_surface.set_alpha(175)
black_screen_rect = black_screen_surface.get_rect(center=(320, 420))

end_screen = EndScreen()
top_screen = TopScreen()

game_on = False
play_screen = True
win_animation = True
draw_end_screen = True
draw_line_top_screen = True
check_draw = True
x_win = False
o_win = False
x_score = 0
o_score = 0
turn = 'X'
length = 0

# Squares
square_1 = Square((0, 200))
square_2 = Square((220, 200))
square_3 = Square((440, 200))
square_4 = Square((0, 420))
square_5 = Square((220, 420))
square_6 = Square((440, 420))
square_7 = Square((0, 640))
square_8 = Square((220, 640))
square_9 = Square((440, 640))

squares_list = [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9]
squares_dict = {square_1: 'Blank', square_2: 'Blank', square_3: 'Blank',
                square_4: 'Blank', square_5: 'Blank', square_6: 'Blank',
                square_7: 'Blank', square_8: 'Blank', square_9: 'Blank'}

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_on:
            for square in squares_list:
                if square.player_input():
                    if squares_dict[square] == 'Blank':
                        if turn == 'X':
                            squares_dict[square] = 'X'
                            turn = 'O'
                        elif turn == 'O':
                            squares_dict[square] = 'O'
                            turn = 'X'
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    screen.fill((0, 0, 60), ((0, 200), (640, 840)))
                    screen.fill((0, 200, 150), ((0, 0), (640, 200)))
                    game_on = True
                    play_screen = False

                if play_again_rect.collidepoint(pygame.mouse.get_pos()):
                    squares_dict = {square_1: 'Blank', square_2: 'Blank', square_3: 'Blank',
                                    square_4: 'Blank', square_5: 'Blank', square_6: 'Blank',
                                    square_7: 'Blank', square_8: 'Blank', square_9: 'Blank'}
                    game_on = True
                    win_animation = True
                    draw_end_screen = True
                    draw_line_top_screen = True
                    length = 0

                    screen = pygame.display.set_mode((640, 840))
                    screen.fill((0, 0, 60), ((0, 200), (640, 840)))
                    screen.fill((0, 200, 150), ((0, 0), (640, 200)))

                    x_win = False
                    o_win = False

    if game_on:

        check_draw = True

        for square in squares_list:
            square.draw_square(squares_dict[square])
            if squares_dict[square] == 'Blank':
                check_draw = False

        if check_draw:
            game_on = False

        if draw_line_top_screen:
            top_screen.draw_score()
            draw_line_top_screen = False

        check_win_x()
        check_win_o()

        if game_on:
            if turn == 'X':
                top_screen.draw_turn_x()
            elif turn == 'O':
                top_screen.draw_turn_o()

    else:

        if play_screen:
            draw_play_screen()

        else:
            if win_animation:
                check_win_x()
                check_win_o()
            else:
                if draw_end_screen:
                    screen.blit(black_screen_surface, black_screen_rect)
                    screen.fill((0, 200, 150), ((0, 0), (640, 200)))

                    if x_win:
                        if x_score < 9:
                            x_score += 1
                        end_screen.draw_x_win()
                    elif o_win:
                        if o_score < 9:
                            o_score += 1
                        end_screen.draw_o_win()

                    screen.blit(play_again_surface, play_again_rect)
                    draw_end_screen = False

            if check_draw and draw_end_screen:
                screen.blit(black_screen_surface, black_screen_rect)
                screen.fill((0, 200, 150), ((0, 0), (640, 200)))
                end_screen.draw_draw()
                screen.blit(play_again_surface, play_again_rect)
                draw_end_screen = False

    pygame.display.update()
    frame_update.tick(30)
