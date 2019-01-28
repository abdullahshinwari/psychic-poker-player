from psychic_poker_functions import royal_flush, flush, four_of_a_kind, three_of_a_kind, one_pair, full_house, two_pairs,\
    high_card, straight

cards = input(" Enter 5 hand cards and 5 deck cards with space between them. e.g: 9S 8D TH AH JH 4H 9H AC QD AS ")

cards.strip()
all_cards = list()
cards = cards.split(" ")
all_cards.extend(cards)
hand_cards = ''
deck_cards = ''
for index, card in enumerate(all_cards):
    if index <= 4:
        hand_cards = hand_cards + ' ' + card
    else:
        deck_cards = deck_cards + ' ' + card


def poker(hand):
    try:
        best = royal_flush(hand)
        if best["hand"] == "royal":
            return 'Royal Flush'

        elif best["hand"] == "not found":
            best = four_of_a_kind(hand)

        if best["hand"] == "four":
            return 'Four of a kind'
        elif best["hand"] == "not found":
            best = full_house(hand)

        if best["hand"] == "full":
            return 'Full house'
        elif best["hand"] == "not found":
            best = flush(hand)

        if best["hand"] == "flush":
            return 'Flush'
        elif best["hand"] == "not found":
            best = straight(hand)

        if best["hand"] == "straight":
            return 'Straight'
        elif best["hand"] == "not found":
            best = three_of_a_kind(hand)

        if best["hand"] == "three":
            return 'Three of a kind'
        elif best["hand"] == "not found":
            best = two_pairs(hand)

        if best["hand"] == "two":
            return 'Two pairs'
        elif best["hand"] == "not found":
            best = one_pair(hand)

        if best["hand"] == "one":
            return 'one pair'
        elif best["hand"] == "not found":
            best = high_card(hand)

        if best["hand"] == "high":
            return 'high card'
    except Exception as es:
        print('You enter wrong input!')
        print(es)


best_hand = poker(all_cards)
print('Hand:', hand_cards, ' ', 'Deck:', deck_cards, ' ', 'Best hand:', best_hand)
