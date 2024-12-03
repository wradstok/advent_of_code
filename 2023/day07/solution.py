from __future__ import annotations

from enum import IntEnum
from collections import Counter
from dataclasses import dataclass


class Label(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


@dataclass
class Hand:
    cards: str
    bid: int

    @property
    def label(self) -> Label:
        num_jokers = self.cards.count("J")
        others = [card for card in self.cards if card != "J"]
        counts = Counter(others)

        match len(counts):
            case 0:
                return Label.FIVE_OF_A_KIND
            case 1:
                return Label.FIVE_OF_A_KIND
            case 2:
                if max(counts.values()) == 4 - num_jokers:
                    return Label.FOUR_OF_A_KIND
                return Label.FULL_HOUSE
            case 3:
                if max(counts.values()) == 3 - num_jokers:
                    return Label.THREE_OF_A_KIND
                return Label.TWO_PAIRS
            case 4:
                return Label.ONE_PAIR
            case 5:
                return Label.HIGH_CARD
        raise ValueError("Invalid hand")

    def __lt__(self, other: Hand) -> bool:
        if self.label != other.label:
            return self.label < other.label

        for i, j in zip(self.cards, other.cards):
            if order.index(i) == order.index(j):
                continue
            return order.index(i) > order.index(j)

        raise ValueError("Invalid hand")


with open("2023/day07/input.txt") as f:
    hands = []
    for line in f.read().splitlines():
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid)))


hands.sort()
winnings = 0
for i, hand in enumerate(hands):
    winnings += hand.bid * (i + 1)
print(winnings)
