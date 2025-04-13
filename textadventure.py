#text adventure

class Location():
    def __init__(self,number, text, item, character, exits):
        self.number = number
        self.location_text = text
        self.item = item
        self.character = character
        self.exits = exits

location1 = Location(1, "You are in Glen. There is an exit south", "", "", [-1, -1, 1, -1]) #0
location2 = Location(2, "You have reached the valley. There is smoke billowing from the town to the south. There are exits north, east and south", "", "", [1, 4, 5, 0]) #1
location3 = Location(3, "You have reached the town. It looks like there been a recent battle", "", "", [2, -1, -1, -1]) #2

locations = [location1, location2, location3]

running = True

location = location1
next_location = -1

while running:
    print(location.location_text)
    direction = input("Which direction do you want to go? N, E, S, W or Q to quit - ")
    direction = direction.upper()
    if(direction == "Q"):
        running = False
    elif direction == "N":
        next_location = locations[location.exits[0]]
    elif direction == "S":
        next_location = locations[location.exits[2]]
    
    if next_location != -1:
        location = next_location
    else:
        print("Not a valid direction")
