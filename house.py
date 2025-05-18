import pygame
class HouseScreen:
    def __init__(self, screen, width, height, room_images):
        self.placed_items = []
        self.screen = screen
        self.width = width
        self.height = height
        self.room_images = room_images  # Artık oda resimleri listesi burada
        self.current_room_index = 0  # Başlangıçta 0. oda gösterilir
        self.font = pygame.font.SysFont(None, 36)

    def set_room_index(self, index):
        if 0 <= index < len(self.room_images):
            self.current_room_index = index

    def draw(self):
        # Sadece seçili oda resmini çiz
        self.screen.blit(self.room_images[self.current_room_index], (0, 0))

        # Oda bilgisi vb. metin
        text = f"Room Level: {self.current_room_index + 1}"
        render = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(render, (10, 10))
