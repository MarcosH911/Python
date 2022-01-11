import pygame
from sys import exit
from random import randint, choice


# Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_walk_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_walk_index]
        self.rect = self.image.get_rect(midbottom=(100, 300))
        self.player_gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.05)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.player_gravity = -20
            self.jump_sound.play()

    def apply_player_gravity(self):
        self.player_gravity += 1
        self.rect.y += self.player_gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_walk_index += all_speed/50
            if self.player_walk_index >= len(self.player_walk):
                self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]

    def update(self):
        self.player_input()
        self.apply_player_gravity()
        self.animation_state()


# Obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type):
        super().__init__()

        if obstacle_type == 'snail':
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            self.y_pos = 300

        elif obstacle_type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            self.y_pos = 190

        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright=(randint(900, 1050), self.y_pos))

    def animation_state(self):
        self.animation_index += all_speed/50
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= all_speed
        self.destroy()

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()


# Score
def display_score():
    global score

    score += (all_speed - 3.5)/100
    score_surface = game_font.render(f'Score: {int(score)}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return score


# Overall speed
def display_speed():
    speed_surface = game_font.render(f'Speed: {int(all_speed - 4)}', False, (64, 64, 64))
    speed_rect = speed_surface.get_rect(midright=(785, 30))
    screen.blit(speed_surface, speed_rect)


# Collisions
def sprite_collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        death_sound.play()
        player.sprite.player_gravity = 0
        player.sprite.rect.bottom = 300
        return False
    else:
        return True


# Ground
def ground_animation():
    global ground_index
    ground_surface_1 = pygame.image.load('graphics/ground/ground1.png').convert()
    ground_surface_2 = pygame.image.load('graphics/ground/ground2.png').convert()
    ground_surface_3 = pygame.image.load('graphics/ground/ground3.png').convert()
    ground_surface_4 = pygame.image.load('graphics/ground/ground4.png').convert()
    ground_surface_5 = pygame.image.load('graphics/ground/ground5.png').convert()
    ground_surface_6 = pygame.image.load('graphics/ground/ground6.png').convert()
    ground_surface_7 = pygame.image.load('graphics/ground/ground7.png').convert()
    ground_list = [ground_surface_1, ground_surface_2, ground_surface_3, ground_surface_4, ground_surface_5,
                   ground_surface_6, ground_surface_7]

    ground_index += all_speed/5
    if ground_index >= len(ground_list):
        ground_index = 0

    return ground_list[int(ground_index)]


# Initial values
pygame.init()
screen = pygame.display.set_mode((800, 400))
frame_update = pygame.time.Clock()
pygame.display.set_caption('Pixel runner')
icon_image = pygame.image.load('graphics/Player/player_stand.png')
icon_image = pygame.transform.scale(icon_image, (76, 76))
pygame.display.set_icon(icon_image)
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_on = False
start_time = 0
score = 0
max_score = 0
ground_index = 0
all_speed = 5

background_music = pygame.mixer.Sound('audio/music.wav')
music_volume = 0.1
death_sound = pygame.mixer.Sound('audio/Laser.ogg')
death_sound.set_volume(0.2)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Load background
sky_surface = pygame.image.load('graphics/sky.png').convert()

# Player
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# End game screen
end_title_surface = game_font.render('Pixel Runner', False, (111, 196, 169))
end_title_rect = end_title_surface.get_rect(center=(400, 35))
end_play_again_surface = game_font.render('Press ENTER to play', False, (111, 196, 169))
end_play_again_rect = end_play_again_surface.get_rect(center=(400, 380))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

# Game playing
while True:

    # Check events
    for event in pygame.event.get():

        # Check if player wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check while playing
        if game_on:

            # Generate obstacle
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'fly', 'snail', 'snail', 'snail', 'snail', 'snail'])))

        # While not playing
        else:

            # Start playing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_on = True
                start_time = pygame.time.get_ticks()

                # Restart music
                music_volume = 0.1
                background_music.stop()
                background_music.play(loops=-1)
                background_music.set_volume(music_volume)

                # Restart parameters
                score = 0
                all_speed = 5
                all_acceleration = 0

    # While playing
    if game_on:

        # Display background
        screen.blit(sky_surface, (0, 0))
        ground_surface = ground_animation()
        screen.blit(ground_surface, (0, 300))

        # Update parameters
        score = display_score()
        display_speed()
        all_speed += 0.003

        # Player
        player.draw(screen)
        player.update()

        # Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collisions
        game_on = sprite_collisions()

    # While not playing
    else:

        # End screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(end_title_surface, end_title_rect)
        screen.blit(end_play_again_surface, end_play_again_rect)

        if score > max_score:
            max_score = score
        end_score_surface = game_font.render(f'Final score: {int(score)}', False, (111, 196, 169))
        end_score_rect = end_score_surface.get_rect(center=(400, 85))

        end_max_score_surface = game_font.render(f'HIGH SCORE: {int(max_score)}', False, (255, 255, 255))
        end_max_score_rect = end_max_score_surface.get_rect(center=(400, 330))
        screen.blit(end_max_score_surface, end_max_score_rect)

        if score != 0:
            screen.blit(end_score_surface, end_score_rect)

        # Music
        if music_volume > 0.01:
            music_volume -= 0.0005
            background_music.set_volume(music_volume)

    # Update frames
    pygame.display.update()
    frame_update.tick(60)
