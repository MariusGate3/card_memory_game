import pygame
import os

pygame.mixer.init()
game_dir = os.path.dirname(__file__)
card_flip_sound = pygame.mixer.Sound("assets/sounds/card_flip2.mp3")


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.front = pygame.image.load(
            os.path.join(game_dir, "assets", "images", f"{suit}_{rank}.png")
        )
        self.back = pygame.image.load(
            os.path.join(game_dir, "assets", "images", "back_light.png")
        )

        self.back = self.adjust_size(self.back, 2.5)
        self.front = self.adjust_size(self.front, 2.5)
        self.image = self.back
        self.rect = self.image.get_rect()
        self.pair = None
        self.x = None
        self.y = None

    def adjust_size(self, surface, sizing_factor: int):

        return pygame.transform.smoothscale(
            surface,
            (
                surface.get_width() // sizing_factor,
                surface.get_height() // sizing_factor,
            ),
        )

    def flip(self):

        card_flip_sound.play()
        if self.image == self.back:
            self.image = self.front
        else:
            self.image = self.back
        print(
            f"{self.rank} of {self.suit} flipped to {'front' if self.image == self.front else 'back'}"
        )

    def set_pair(self, pair):
        self.pair = pair

    def display(self, screen):
        screen.blit(self.image, self.rect)
