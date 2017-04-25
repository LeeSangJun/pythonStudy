def get_description():
    """Return random weather, just like the pros"""

    from random import choice
    possibilities = ['rani', 'snow', 'sleet', 'fog', 'sun', 'who knowns']
    return choice(possibilities)