import pygame
from player import Player
from deck import Deck
import config
import time

current_player = 0
Players = [Player("Player 1", True), Player("Player 2")]
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)
turn_text = font.render(f"{Players[current_player].name}'s Turn", True, (255, 255, 255))
pair_sound = pygame.mixer.Sound("assets/sounds/pair_sound.mp3")


deck = Deck()
deck.shuffle()


def drawContents():
    config.screen.fill((0, 0, 0))
    Players[0].display((30, 10), config.screen)
    Players[1].display((config.window_x - 200, 10), config.screen)
    config.screen.blit(
        turn_text, (config.window_x // 2 - turn_text.get_width() // 2, 10)
    )
    deck.display_cards(config.screen)
    pygame.display.flip()


if __name__ == "__main__":
    cards_flipped = 0
    pair_found = False
    waiting = False

    pygame.display.set_caption("Memory Card Game")
    clock.tick(60)
    drawContents()

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not waiting:
                mouse_pos = pygame.mouse.get_pos()
                for card in deck.cards:
                    if card.rect.collidepoint(mouse_pos) and card.image != card.front:
                        card.flip()
                        drawContents()
                        cards_flipped += 1
                        break

                if cards_flipped == 2:
                    print("2 cards flipped, waiting 2 seconds")
                    waiting = True
                    time.sleep(1.5)
                    for card in deck.cards:
                        if card.image == card.front:
                            if card.pair.image == card.pair.front:
                                print(f"Pair found: {card.rank} of {card.suit}")
                                pair_found = True
                                Players[current_player].score += 1
                                cards_flipped = 0
                                break
                            card.flip()
                    if pair_found:
                        pair_sound.play()
                        deck.cards.remove(card)
                        deck.cards.remove(card.pair)
                        if len(deck.cards) <= 0:
                            winner = 2
                            if Players[0].score > Players[1].score:
                                winner = 0
                            elif Players[0].score < Players[1].score:
                                winner = 1

                            if winner == 2:
                                print(
                                    "The round was a draw! Dealing a new set of cards."
                                )
                            else:
                                print(
                                    f"{Players[winner].name} won this round! Their round win total is now: {Players[winner]}"
                                )
                                Players[winner].round_wins += 1
                                print("Dealing a new set of cards!\n")
                                deck.deal_new_set_of_cards()

                        print(
                            f"Pair found, it is still {Players[current_player].name}'s turn."
                        )
                        pair_found = False
                    else:
                        current_player = 1 if current_player == 0 else 0
                        print(
                            f"No pair found, it is now {Players[current_player].name}'s turn"
                        )
                        turn_text = font.render(
                            f"{Players[current_player].name}'s Turn",
                            True,
                            (255, 255, 255),
                        )

                    cards_flipped = 0
                    waiting = False
                    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                    drawContents()

        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    pygame.quit()
