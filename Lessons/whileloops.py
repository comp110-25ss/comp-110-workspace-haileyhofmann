"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_idx: int = 0
low_card: int = int(cards[0])

while card_idx < 4:
    current_card: int = int(cards[card_idx])
    if current_card < low_card:
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)
