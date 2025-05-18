import pygame

class HouseScreen:
    def __init__(self, screen, width, height, assets):
        self.screen = screen
        self.width = width
        self.height = height
        self.assets = assets  # dict içinde arka plan, ödül img leri vs
        self.font = pygame.font.SysFont(None, 36)

        self.rewards_placed = []

    def draw_text_center(self, text, y, font=None, color=(255,255,255)):
        if not font:
            font = self.font
        render = font.render(text, True, color)
        rect = render.get_rect(center=(self.width//2, y))
        self.screen.blit(render, rect)

    def draw(self):
        # Arka plan
        self.screen.blit(self.assets["bg"], (0, 0))

        # Ödülleri çiz
        for reward in self.rewards_placed:
            self.screen.blit(reward["img"], reward["pos"])

        # Geri dönme uyarısı
        self.draw_text_center("Evdeyiz - Geri dönmek için ESC", self.height - 40)

    def add_reward(self, reward):
        self.rewards_placed.append(reward)

    def reset(self):
        self.rewards_placed.clear()
