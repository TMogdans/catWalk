import pygame
from spritesheet import SpriteSheet


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, effect_type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if effect_type == 'jump':
            piece_ss = SpriteSheet('assets/character/jump.png')
            self.frames = piece_ss.load_strip([0, 0, 34, 32], 6, -1)
        if effect_type == 'land':
            piece_ss = SpriteSheet('assets/character/land.png')
            self.frames = piece_ss.load_strip([0, 0, 104, 12], 5, -1)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift
