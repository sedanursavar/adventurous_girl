import pygame
import os
from collections import defaultdict

class CharacterAnimation:
    def __init__(self, folder_path, animation_speed=0.15, background_width=576):

        self.animations = defaultdict(list)
        self.animation_speed = animation_speed
        self.current_animation = None
        self.frame_index = 0
        self.image = None
        self.background_width = background_width

        self.load_animations(folder_path)

    def load_animations(self, folder_path):
        files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]

        scale_width = int(self.background_width * 0.1)  # Arka planın %10'u

        for file in sorted(files):
            name_only = os.path.splitext(file)[0]
            anim_name = ''.join([c for c in name_only if c.isalpha()]).lower()

            path = os.path.join(folder_path, file)
            image = pygame.image.load(path).convert_alpha()

            # Ölçeklendirme
            scale_ratio = scale_width / image.get_width()
            scale_height = int(image.get_height() * scale_ratio)
            image = pygame.transform.scale(image, (scale_width, scale_height))

            self.animations[anim_name].append(image)

        if self.animations:
            self.current_animation = list(self.animations.keys())[0]
            self.image = self.animations[self.current_animation][0]

    def set_animation(self, anim_name):
        anim_name = anim_name.lower()
        if anim_name != self.current_animation and anim_name in self.animations:
            self.current_animation = anim_name
            self.frame_index = 0

    def update(self):
        if not self.current_animation:
            return

        frames = self.animations[self.current_animation]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0
        self.image = frames[int(self.frame_index)]

    def get_image(self):
        return self.image
