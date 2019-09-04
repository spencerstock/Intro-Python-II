from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'dagger': Item("Small Dagger", 
                    "It fits in the palm of your hand",
                    1),
    'sword': Item("Small Sword", 
                    "Looks like a child's toy",
                    1)
}





# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].items.append(items['dagger'])
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("Welcome to Balrog MUD")
username = input("Please enter your username: ")
player1 = Player(username, room['outside'])

while True:

    print(player1.room)
    command = input("> ")

    if (command == "q"):
        print("quitting")
        break

    elif (command == "e"):
            if (isinstance(player1.room.e_to, Room)):
                print(player1.name + " moves East")
                player1.room = player1.room.e_to
            else:
                print("You can't go that direction")

    elif (command == "w"):
        if (isinstance(player1.room.w_to, Room)):
                print(player1.name + " moves West")
                player1.room = player1.room.w_to
        else:
            print("You can't go that direction")
    
    elif (command == "s"):
        if (isinstance(player1.room.s_to, Room)):
                print(player1.name + " moves South")
                player1.room = player1.room.s_to
        else:
            print("You can't go that direction")

    elif (command == "n"):
        if (isinstance(player1.room.n_to, Room)):
                print(player1.name + " moves North")
                player1.room = player1.room.n_to
        else:
            print("You can't go that direction")

    else:
        print("What?")
        
    
        

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
