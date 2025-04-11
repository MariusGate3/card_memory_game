import pygame


class Player:
    def __init__(self, name: str, turn: bool = False):
        self.name = name
        self.score = 0
        self.round_wins = 0
        self.turn = turn

    def display(self, pos, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, pos)

        text_score = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_score, (pos[0], pos[1] + 30))

        round_score = font.render(
            f"Round wins: {self.round_wins}", True, (255, 255, 255)
        )
        screen.blit(round_score, (pos[0], pos[1] + 60))
