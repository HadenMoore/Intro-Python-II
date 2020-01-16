# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    """The Main Character or (Hero) for this incredible, slightly disappointing adventure."""
    def __init__(self, name, location, inventory): 
        self.name = name
        self.location = location
        self.inventory = inventory