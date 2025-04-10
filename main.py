import pygame
from player import Player
from deck import Deck
import config
import time

current_player = 0
Players = [Player("Player 1", True), Player("Player 2")]
pygame.init()
clock = pygame.time.Clock()
running = True

deck = Deck()
deck.shuffle()


if __name__ == "__main__":
    cards_flipped = 0
    while running:
        # Drawing
        config.screen.fill((0, 0, 0))
        deck.display_cards(config.screen)
        pygame.display.set_caption("Card Game")
        Players[0].display((30, 10), config.screen)
        Players[1].display((config.window_x - 200, 10), config.screen)

        # Event handling
        keys = pygame.key.get_pressed()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for card in deck.cards:
                    if card.rect.collidepoint(mouse_pos):
                        card.flip()
                        cards_flipped += 1
                        break

        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        if cards_flipped == 2:
            print("2 cards flipped, waiting 2 seconds")
            time.sleep(3)
            pair_found = False
            for card in deck.cards:
                if card.image == card.front:
                    if card.pair.image == card.front:
                        print(f"Pair found: {card.rank} of {card.suit}")
                        Players[current_player].score += 1
                        deck.cards.remove(card)
                        deck.cards.remove(card.pair)
                        cards_flipped = 0
                        break
                    card.flip()
            if pair_found:
                print(f"Pair found, it is still {Players[current_player].name}'s turn.")
            else:
                current_player = 1 if current_player == 0 else 0
                print(f"No pair found, it is now {Players[current_player].name}'s turn")
            cards_flipped = 0

        pygame.display.flip()

    pygame.quit()
