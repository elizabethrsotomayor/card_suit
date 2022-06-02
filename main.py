def define_suit(card: str) -> str:
    """
    Return the suit of the card given.
    :param card: the card to determine suit from (ie, '3C', '3H', 'QS')
    :return: the suit of the card as a string
    """
    suit = ""
    if card[-1] == 'C':
        suit = 'clubs'
    elif card[-1] == 'S':
        suit = 'spades'
    elif card[-1] == 'D':
        suit = 'diamonds'
    elif card[-1] == 'H':
        suit = 'hearts'

    return suit
