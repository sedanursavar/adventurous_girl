import pygame

pygame.font.init()

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 36)
        self.score = 0
        self.high_score = 0
        self.state = "menu"  # menu, playing, game_over, paused

        self.restart_rect = pygame.Rect(self.width//2 - 100, self.height//2 + 50, 200, 50)

        # Menü arka planını yükle
        try:
            self.bg_image = pygame.image.load(
                r"C:\Users\seda.savar\Desktop\programlama_dilleri\main_menu_background_under_buttons.png"
            ).convert()
            # Gerekirse boyutlandır
            self.bg_image = pygame.transform.scale(self.bg_image, (self.width, self.height))
        except Exception as e:
            print(f"Menü arka planı yüklenemedi: {e}")
            self.bg_image = None

    def draw_text_center(self, text, y, font=None, color=(255,255,255)):
        if not font:
            font = self.font
        render = font.render(text, True, color)
        rect = render.get_rect(center=(self.width//2, y))
        self.screen.blit(render, rect)

    def draw_menu(self):
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill((128, 0, 128))
        self.draw_text_center("ADVENTUROUS GIRL", self.height//3)
        self.draw_text_center("Başlamak için Enter'a basın", self.height//2, self.small_font)
        self.draw_text_center(f"En Yüksek Skor: {self.high_score}", self.height//2 + 100, self.small_font)

    def draw_game_over(self):
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill((0, 0, 128))
        self.draw_text_center("Oyun Bitti!", self.height // 3)
        self.draw_text_center(f"Skorunuz: {self.score}", self.height // 2, self.small_font)
        self.draw_text_center(f"En Yüksek Skor: {self.high_score}", self.height // 2 + 50, self.small_font)

        # Restart butonunu aşağı taşıyoruz
        self.restart_rect.top = self.height // 2 + 90

        pygame.draw.rect(self.screen, (200, 200, 200), self.restart_rect)
        self.draw_text_center("Yeniden Başla", self.restart_rect.centery, self.small_font, (0, 0, 0))

    def draw_pause(self):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0,0))

        self.draw_text_center("Oyun Duraklatıldı", self.height//3)
        self.draw_text_center("Devam etmek için P tuşuna basın", self.height//2, self.small_font)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def handle_events(self, event, jump_pressed_ref=None):
        if self.state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.state = "playing"
                self.score = 0
        elif self.state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restart_rect.collidepoint(event.pos):
                    self.state = "playing"
                    self.score = 0
        elif self.state == "paused":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.state = "playing"
                if jump_pressed_ref is not None:
                    jump_pressed_ref[0] = False

    def toggle_pause(self, jump_pressed_ref=None):
        if self.state == "playing":
            self.state = "paused"
            if jump_pressed_ref is not None:
                jump_pressed_ref[0] = False
        elif self.state == "paused":
            self.state = "playing"
            if jump_pressed_ref is not None:
                jump_pressed_ref[0] = False

    def increase_score(self):
        if self.state == "playing":
            self.score += 1

    def draw(self):
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game_over":
            self.draw_game_over()
        elif self.state == "paused":
            self.draw_pause()
