# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    """The Room Class contains a contructor to instanciate a new room.
    The Room Class Also Contains a Method to Print its Description. Trigger the 
    method upon player entering the Room."""
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory