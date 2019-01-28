
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def royal_flush(my_list):
    """
    This function is finding royal flush hand of psychic poker
    :param my_list:
    :return:  This method will return the result in json format. it will return that,
    it is royal flush. e.g: {'royal': ['TH', 'AH', 'JH', 'QH', 'KH']}
    If royal flush not found, it return a message: {'message': 'Royal Flush not found'}
    """
    royal_flush_c = list()
    royal_flush_d = list()
    royal_flush_h = list()
    royal_flush_s = list()

    for v, f in my_list:
        if f == 'C' and (v == 'A' or v == 'K' or v == 'Q' or v == 'J' or v == 'T'):
            royal_flush_c.append(v + f)
            if len(royal_flush_c) == 5:
                return {"hand": "royal", "cards": royal_flush_c}

        elif f == 'D' and (v == 'A' or v == 'K' or v == 'Q' or v == 'J' or v == 'T'):
            royal_flush_d.append(v + f)
            if len(royal_flush_d) == 5:
                return {'hand': "royal", "cards": royal_flush_d}

        elif f == 'H' and (v == 'A' or v == 'K' or v == 'Q' or v == 'J' or v == 'T'):
            royal_flush_h.append(v + f)
            if len(royal_flush_h) == 5:
                return {'hand': "royal", "cards": royal_flush_h}

        elif f == 'S' and (v == 'A' or v == 'K' or v == 'Q' or v == 'J' or v == 'T'):
            royal_flush_s.append(v + f)
            if len(royal_flush_s) == 5:
                return {'hand': "royal", "cards": royal_flush_s}
    else:
        return {"hand": "not found"}


def four_of_a_kind(all_10_cards):
    """
    This method will find four of a kind of psychic poker
    :param all_10_cards:
    :return:  This method will return the result in json format. it returns that, it is four of a kind with face value
    e.g: {"Face Value 3 is 'Four of a kind'": ['3C', '3D', '3H', '3S']}
    If four of a kind not found, it return a message: {'message': 'Not four of a kind'}
    """
    for a, b in all_10_cards:
        my_list = list()
        count = 0
        for x, y in all_10_cards:
            if a == x:
                my_list.append(x + y)
                count = count + 1
        if count == 4:
            return {"hand": "four", "cards": my_list}
    return {"hand": "not found"}


def full_house(all_10_cards):
    """
    This method will find full house of psychic poker
    :param all_10_cards:
    :return: This method will return the result in json format. it will return that, it is full house with face value
    e.g: {'Full House': ['AH', 'AC', 'AS', '9S', '9H']}
    If four of a kind not found, it return a message: {'message': 'Not full house'}
    """
    full_house_list = list()
    for a, b in all_10_cards:
        my_list = list()
        count = 0
        for x, y in all_10_cards:
            if a == x:
                my_list.append(x + y)
                count = count + 1
        if count == 3:
            full_house_list.extend(my_list)
            break

    if not full_house_list:
        return {"hand": "not found"}
    for c, d in all_10_cards:
        my_list = list()
        count = 0
        for i, j in all_10_cards:
            if c == i and i != full_house_list[0][0]:
                my_list.append(i + j)
                count = count + 1
        if count == 2:
            full_house_list.extend(my_list)
            return {"hand": "full", "cards": full_house_list}
    if len(full_house_list) != 5:
        return {"hand": "not found"}


def flush(my_list):
    """
    This function is finding flush hand of psychic poker
    :param my_list:
    :return: This method will return the result in json format. it will return that,
    it is flush of CLUBS OR DIAMONDS OR HEARTS OR SPADES.
    e.g: {'Flush of SPADES ': ['TS', '3S', '4S', '6S', 'AS']}
    If flush not found, it return a message: {'Message': 'Flush hand not found'}
    """
    flush_c = list()
    flush_d = list()
    flush_h = list()
    flush_s = list()

    for v, f in my_list:
        if f == 'C':
            flush_c.append(v + f)
            if len(flush_c) == 5:
                return {"hand": "flush", "cards": flush_c}

        elif f == 'D':
            flush_d.append(v + f)
            if len(flush_d) == 5:
                return {"hand": "flush", "cards": flush_d}

        elif f == 'H':
            flush_h.append(v + f)
            if len(flush_h) == 5:
                return {"hand": "flush", "cards": flush_h}

        elif f == 'S':
            flush_s.append(v + f)
            if len(flush_s) == 5:
                return {"hand": "flush", "cards": flush_s}

    else:
        return {"hand": "not found"}


def straight(all_10_cards):
    """
    This method will find straight of psychic poker
    :param all_10_cards:
    :return: This method will return the result in json format. it will return that, it is straight.
    e.g: {'Straight': ['TD', 'JS', 'QS', 'KS', 'AS']}
    If four of a kind not found, it return a message: {'message': 'Not Straight'}
    """
    cards_dict = dict()
    cards_value = list()

    for face, suit in all_10_cards:
        cards_dict[face] = values.get(face)
    for key, value in sorted(cards_dict.items(), key=lambda kv: kv[1]):
        cards_value.append(value)

    number_list = list()
    straight_list = list()
    result_list = list()
    for value in cards_value:
        if not number_list or number_list[-1][-1] != value-1:
            number_list.append([])
        number_list[-1].append(value)
    for number in number_list:
        if len(number) >= 5:
            straight_list.append(number)

    if not straight_list:
        return {"hand": "not found"}
    for number in straight_list[0]:
        for face, value in all_10_cards:
            if number == values[face]:
                result_list.append(face + value)

    return {"hand": "straight", "cards": result_list}


# ***********************************************************************


def three_of_a_kind(all_10_cards):
    """
    This method will find three of a kind of psychic poker
    :param all_10_cards:
    :return:  This method will return the result in json format. it returns that, it is three of a kind with face value
    e.g: {"Face Value Q is 'Three of a kind'": ['QD', 'QS', 'QH']}
    If three of a kind not found, it return a message: {'message': 'Not three of a kind'}
    """
    for a, b in all_10_cards:
        my_list = list()
        count = 0

        for x, y in all_10_cards:
            if a == x:
                my_list.append(x + y)
                count = count + 1
        if count == 3:
            return {"hand": "three", "cards": my_list}
    return {"hand": "not found"}


def two_pairs(all_10_cards):
    """
    This method will find two pairs of psychic poker
    :param all_10_cards:
    :return: This method will return the result in json format. it will return that, it is two pairs  with face value
    e.g: {'Full House': ['AH', 'AC', 'AS', '9S', '9H']}
    If four of a kind not found, it return a message: {'message': 'Not two pairs'}
    """
    two_pairs_list = list()
    for a, b in all_10_cards:
        my_list = list()
        count = 0
        for x, y in all_10_cards:
            if a == x:
                my_list.append(x + y)
                count = count + 1
        if count == 2:
            two_pairs_list.extend(my_list)
            break

    if not two_pairs_list:
        return {"hand": "not found"}

    for c, d in all_10_cards:
        my_list = list()
        count = 0
        for i, j in all_10_cards:
            if c == i and i != two_pairs_list[0][0]:
                my_list.append(i + j)
                count = count + 1
        if count == 2:
            two_pairs_list.extend(my_list)
            return {"hand": "two", "cards": two_pairs_list}
    if len(two_pairs_list) != 4:
        return {"hand": "not found"}


def one_pair(all_10_cards):
    """
    This method will find one pair of psychic poker
    :param all_10_cards:
    :return: This method will return the result in json format. it will return that, it is one pair with face value
    e.g: {"Face Value A is 'One Pair '": ['AH', 'AC']}
    If four of a kind not found, it return a message: {'message': 'Not One Pair'}
    """
    for a, b in all_10_cards:
        my_list = list()
        count = 0

        for x, y in all_10_cards:
            if a == x:
                my_list.append(x + y)
                count = count + 1
        if count == 2:
            return {"hand": "one", "cards": my_list}
    return {"hand": "not found"}


def high_card(all_10_cards):
    """
    This method will find high card of psychic poker
    :param all_10_cards:
    :return: This method will return the result in json format. it will return that, it is high card
    e.g:{'High Card': '5D'}
    """
    high = values[all_10_cards[0][0]]
    highest_card = all_10_cards[0]
    for i, j in all_10_cards:
        if values[i] > high:
            high = values[i]
            highest_card = i+j
    return {"hand": "high", "cards": highest_card}
