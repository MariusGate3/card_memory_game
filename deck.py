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
        self.margin_top = 400
        self.margin_side = 400
        self.init_new_deck()
        self.cards_width = self.cards[0].rect.width
        self.cards_height = self.cards[0].rect.height
        self.cards_per_row = (config.window_x - 2 * self.margin_side + self.gap) // (
            self.cards_width + self.gap
        )
        self.cards_per_col = (config.window_y - self.margin_top + self.gap) // (
            self.cards_height + self.gap
        )

        self.displayed_cards_count = (
            (self.cards_per_row * self.cards_per_col) // 2
        ) * 2

        self.init_card_doubles()
        self.set_card_positions()

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

    def set_card_positions(self):
        row = 0
        col = 0

        start_x = (
            config.window_x
            - (self.cards_per_row * (self.cards_width + self.gap) - self.gap)
        ) // 2

        total_grid_height = (
            self.cards_per_col * (self.cards_height + self.gap) - self.gap
        )
        start_y = (config.window_y - total_grid_height) // 2

        for i, card in enumerate(self.cards):
            x = start_x + col * (self.cards_width + self.gap)
            y = start_y + row * (self.cards_height + self.gap)
            self.cards[i].x = x
            self.cards[i].y = y
            self.cards[i].rect.topleft = (self.cards[i].x, self.cards[i].y)

            col += 1

            if col == self.cards_per_row:
                col = 0
                row += 1

    def deal_new_set_of_cards(self):
        self.init_new_deck()
        self.init_card_doubles()
        self.set_card_positions()

    def display_cards(self, screen):
        for card in self.cards:
            card.display(screen)
