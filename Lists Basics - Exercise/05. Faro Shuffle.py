cards_names = input().split()
number_of_shuffles = int(input())
new_deck = []
half_deck = len(cards_names) // 2



for shuffles in range(number_of_shuffles):
    left_side = cards_names[0:half_deck]
    right_side = cards_names[half_deck:]
    for cards in range (half_deck):
        new_deck.append(left_side[cards])
        new_deck.append(right_side[cards])
    cards_names = new_deck
    new_deck = []
print(cards_names)

