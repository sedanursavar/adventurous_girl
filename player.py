import pygame

class Player:
    def __init__(self, x, y, animation):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.gravity = 0.8
        self.is_jumping = False
        self.is_running = False
        self.is_attacking = False

        self.anim = animation  # CharacterAnimation objesi
        self.current_animation = 'run'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = None
        self.rect = pygame.Rect(self.x, self.y, self.anim.frame_width, self.anim.frame_height)

    def handle_input(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vel_y = -15
            self.is_jumping = True

        if keys[pygame.K_RIGHT]:
            self.is_running = True
        else:
            self.is_running = False

        # Basit saldırı tuşu örneği: A tuşu
        if keys[pygame.K_a]:
            self.is_attacking = True
        else:
            self.is_attacking = False

    def update(self):
        # Yerçekimi ve zıplama
        self.vel_y += self.gravity
        self.y += self.vel_y

        # Zemin kontrolü (örnek zemin yüksekliği 264)
        if self.y >= 264:
            self.y = 264
            self.is_jumping = False
            self.vel_y = 0

        # Animasyon durumu belirle
        if self.is_attacking:
            self.current_animation = 'attack'
        elif self.is_jumping:
            self.current_animation = 'jump'
        elif self.is_running:
            self.current_animation = 'run'
        else:
            self.current_animation = 'run'  # idle yoksa koşma animasyonu

        # Animasyon kare ilerlet
        frames = getattr(self.anim, f"{self.current_animation}_frames")
        self.frame_index += self.animation_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0
            # Saldırı animasyonu bittiyse saldırıyı kapatabiliriz
            if self.current_animation == 'attack':
                self.is_attacking = False

        self.image = frames[int(self.frame_index)]
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
