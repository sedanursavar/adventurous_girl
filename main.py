import pygame
import sys
import os
import random
from character_animation import CharacterAnimation
from menu import Menu

pygame.init()

WIDTH, HEIGHT = 576, 324
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animasyonlu Oyun")

FPS = 60
clock = pygame.time.Clock()

bg_image = pygame.image.load(r"C:\Users\seda.savar\Desktop\adventurous_girl\images\background.png").convert()
bg_width = bg_image.get_width()

scroll_speed = 3
ground_y = HEIGHT - 50

obstacle_folder = r"C:\Users\seda.savar\Desktop\adventurous_girl\images\obstacles"
obstacle_files = [f for f in os.listdir(obstacle_folder) if f.lower().endswith('.png')]

obstacle_images = []
for file in obstacle_files:
    path = os.path.join(obstacle_folder, file)
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        scale_width = int(WIDTH * 0.07)
        scale_ratio = scale_width / img.get_width()
        scale_height = int(img.get_height() * scale_ratio)
        img = pygame.transform.scale(img, (scale_width, scale_height))
        obstacle_images.append(img)

class Obstacle:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.speed = scroll_speed
        self.width = image.get_width()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, move):
        if move:
            self.x -= self.speed
            self.rect.topleft = (self.x, self.y)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def off_screen(self):
        return self.x < -self.width

anim_folder = r"C:\Users\seda.savar\Desktop\adventurous_girl\images\character-animations"
character_anim = CharacterAnimation(anim_folder, animation_speed=0.15, background_width=WIDTH)

menu = Menu(WIN, WIDTH, HEIGHT)

# Oda görselleri
room_image_paths = [
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room0.png",
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room1.png",
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room2.png",
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room3.png",
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room4.png",
    r"C:\Users\seda.savar\Desktop\adventurous_girl\images\XD\room5.png",
]

room_images = []
for path in room_image_paths:
    if os.path.exists(path):
        img = pygame.image.load(path).convert()
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        room_images.append(img)

current_room_index = 0  # Başlangıçta ilk oda

x1, x2 = 0, bg_width
obstacles = []
spawn_timer = 0
spawn_interval = 90

player_x = 100
player_y = ground_y - (character_anim.get_image().get_height() if character_anim.get_image() else 0)

vel_y = 0
gravity = 0.8
max_jumps = 2
jump_count = 0
jump_pressed = [False]

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.handle_events(event, jump_pressed)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            menu.toggle_pause(jump_pressed)

    keys = pygame.key.get_pressed()

    if menu.state == "playing":
        moving = keys[pygame.K_RIGHT]
        vel_x = 5 if moving else 0

        if keys[pygame.K_SPACE]:
            if not jump_pressed[0] and jump_count < max_jumps:
                vel_y = -15
                jump_count += 1
                character_anim.set_animation("jump")
            jump_pressed[0] = True
        else:
            jump_pressed[0] = False

        if jump_count > 0:
            vel_y += gravity
            player_y += vel_y
            ground_level = ground_y - (character_anim.get_image().get_height() if character_anim.get_image() else 0)
            if player_y >= ground_level:
                player_y = ground_level
                jump_count = 0
                vel_y = 0

        player_x += vel_x
        max_player_x = WIDTH // 2
        if player_x > max_player_x:
            player_x = max_player_x

        if jump_count > 0:
            character_anim.set_animation("jump")
        elif moving:
            character_anim.set_animation("run")
        elif keys[pygame.K_a]:
            character_anim.set_animation("melee")
        else:
            character_anim.set_animation("idle")

        character_anim.update()

        player_rect = character_anim.get_image().get_rect(topleft=(player_x, player_y))
        player_rect = player_rect.inflate(-10, -10)

        for obs in obstacles[:]:
            obs.update(moving)
            obs_rect = obs.rect.inflate(-10, -10)
            if player_rect.colliderect(obs_rect):
                menu.state = "game_over"
                menu.update_high_score()
                obstacles.clear()
                spawn_timer = 0
                player_x = 100
                player_y = ground_y - (character_anim.get_image().get_height() if character_anim.get_image() else 0)
                jump_count = 0
                vel_y = 0
                break
            if obs.off_screen():
                obstacles.remove(obs)

        if moving:
            x1 -= scroll_speed
            x2 -= scroll_speed

            if x1 <= -bg_width:
                x1 = x2 + bg_width
            if x2 <= -bg_width:
                x2 = x1 + bg_width

            spawn_timer += 1
            if spawn_timer >= spawn_interval and len(obstacle_images) > 0:
                spawn_timer = 0
                obstacle_img = random.choice(obstacle_images)
                y_pos = ground_y - obstacle_img.get_height()
                new_obstacle = Obstacle(obstacle_img, WIDTH + 150, y_pos)
                obstacles.append(new_obstacle)

        menu.increase_score()

        # Skor arttıkça oda değişimi
        next_room_index = menu.score // 20
        if next_room_index != current_room_index and next_room_index < len(room_images):
            current_room_index = next_room_index
            menu.state = "house"

        WIN.blit(bg_image, (x1, 0))
        WIN.blit(bg_image, (x2, 0))

        for obs in obstacles:
            obs.draw(WIN)

        WIN.blit(character_anim.get_image(), (player_x, player_y))

    elif menu.state == "house":
        # Ev ekranı olarak sadece ilgili oda görselini çiz
        WIN.blit(room_images[current_room_index], (0,0))

        # Bilgi metni
        font = pygame.font.SysFont(None, 36)
        text = font.render("Evdeyiz - Geri dönmek için ESC", True, (255,255,255))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        WIN.blit(text, rect)

        if keys[pygame.K_ESCAPE]:
            menu.state = "playing"

    elif menu.state == "paused":
        menu.draw()

    else:
        menu.draw()

    pygame.display.update()

pygame.quit()
sys.exit()
