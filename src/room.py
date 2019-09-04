# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        s = f'room: {self.name}, description: {self.description}'
        for i in self.items:
            s += "\nThere is one " + i.name
        return s

    def __repr__(self):
        pass
        #TODO: Impelement repr


    name = str
    description = str
    n_to = str
    s_to = str
    e_to = str
    w_to = str 
    items = []