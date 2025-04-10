from card import Card
import random
import config


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["hearts", "diamonds", "clubs", "spades"]
        self.ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        self.gap = 30
        self.init_new_deck()
        self.cards_width = self.cards[0].rect.width
        self.cards_height = self.cards[0].rect.height
        self.cards_per_row = (config.window_x - self.gap) // (
            self.cards_width + self.gap
        )
        self.cards_per_col = (config.window_y - self.gap) // (
            self.cards_height + self.gap
        )

        self.displayed_cards_count = self.cards_per_row * self.cards_per_col

        self.init_card_doubles()

    def shuffle(self):
        random.shuffle(self.cards)

    def init_new_deck(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def init_card_doubles(self):
        self.shuffle()
        card_doubles = []
        for i in range(self.displayed_cards_count // 2):
            card1 = self.cards[i]
            card2 = Card(card1.suit, card1.rank)
            card1.set_pair(card2)
            card2.set_pair(card1)
            card_doubles.append(card1)
            card_doubles.append(card2)
        self.cards = card_doubles
        self.shuffle()

    def display_cards(self, screen):
        row = 0
        space_top = 0

        start_x = (
            config.window_x
            - (self.cards_per_row * (self.cards_width + self.gap) - self.gap)
        ) // 2

        start_y = config.window_y - (
            self.cards_per_col * (self.cards_height + self.gap) - self.gap
        )
        height = space_top + start_y

        for i in range(len(self.cards)):
            if (
                start_x + row * (self.cards_width + self.gap)
                > config.window_x - self.cards_width
            ):
                height += self.cards_height + self.gap
                row = 0

            if height + self.cards_height > config.window_y - self.cards_height:
                break

            self.cards[i].display(
                start_x + (row * (self.cards_width + self.gap)),
                height + self.gap,
                screen,
            )
            i += 1
            row += 1
