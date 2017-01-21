from time import sleep

class room:
    def __init__(self, name, x, y):
        self.name = name
        self.coordinates = [x,y]
        self.desc_dark = ""
        self.desc_light = ""    
           
        
class item:
    def __init__(self, name):
        self.name=name
        self.desc = ""

def look(lit):
    if lit == 0:
        print(location.desc_dark)
    if lit == 1:
        print(location.desc_light)
        
def light(lit):
    if lit == 0:
        print('You turn on your flashlight.')
        print(location.desc_light)
        return 1     
    elif lit == 1:
        print("You turn your flashlight off. You can't see for a moment as your eyes adjust.")
        sleep(3)
        print(location.desc_dark)
        return 0
    
def check_water(water):
    if water == "full":
        return bottle.desc_full
    if water == "half":
        return bottle.desc_half_full
    if water == "empty":
        return bottle.desc_empty

def inspect(x):
    if x in inventory:
        print(x.desc)
    else:
        print("You can't inspect things that aren't in your backpack. Try looking instead.")

def delete(list, x):
    if x in list:
        x=[]
        
room1=room('entrance', 0, 0)
room1.desc_dark = ('You find yourself in a dimly lit room. You can make out a closed door, where light is ' +
                       'creeping through.')
room1.desc_light = ('Your flashlight is brighter than you expected in the dim room. The room is made of wood planks, ' +
                       'and the ceiling is sloped. There is a chest in the middle of the room.')

corridor1=room('collapsed corridor', 0, 1)
corridor1.desc_dark = ("There's a hole in the roof! There's a ton of snow all over the passageway. \n" +
                       "It's night-time out, and your eyes are starting to adjust to the light of the moon.")
corridor1.desc_light = ("This whole corridor looks ready to collapse. The room has already caved in, and there's snow  " +
                            "all over the passageway. \nBroken planks stick out here and there amongst the wreckage.")

room2=room('basement', 0, 2)
room2.desc_dark = "In development."
room2.desc_light = "In development."

flashlight = item("flashlight")
flashlight.desc = ("It's a flashlight. It's bright yellow color and the light is a little dim, but it's enough" +
                       " to make out your surroundings.")
flashlight.state = 0

backpack = item("backpack")
backpack.desc = ("Your handy backpack. You brought it when you went hiking. It's a lot dirtier now than it " +
                 "was then. It contains: \n")

bottle = item("water bottle")
bottle.water = "full"
bottle.desc_full =  "It's full to the brim, and a little heavy to carry."
bottle.desc_half_full = "It's half-full, and lighter than it was."
bottle.desc_empty = ("It's dry. There's a couple droplets left, but they're resolutely clinging to the bottom.")
bottle.desc = ("Your water bottle. It's made of a light metal, maybe aluminum. " + check_water(bottle.water))

location = room1
door1=0
game_finish = 0 
inventory=[backpack, flashlight, bottle, ]

actions=['location', 'look', 'inventory', 'backpack', 'bookbag', 'bag', 'inspect backpack', 'light', 
         'use flashlight', 'light flashlight', 'leave', 'exit', 'forward', 'flashlight',
         'Flashlight', "inspect flashlight", "enter", 'water bottle', "drink", "drink water", "use water",
         'enter corridor', 'inspect bottle', 'inspect water bottle', 'flashlight on', 'turn on', 'exit room',
         'open door', 'open', 'look backpack']
#need to make this list automated, ton of useless typing

#needs to be dictionary, not list. will fix when i have time to figure it out

#intro starts here
print("Would you like to watch the intro? It adds a story to the game. (yes/no)")
command = input(">>")
while (command != 'yes') and (command != 'no'):
    print("Please type yes or no.")
    command = input(">>")
    
if command == 'yes':
    print(room1.desc_dark)
    print("You can't remember how you got here. The last thing you remember is hiking with your dog,"
          + "Fido, in . . . ")
    sleep(5)
    print("Where were you hiking? God, your head hurts. Maybe a glass of water would do you good. \n" +
          "You reach into your backpack.")
    sleep(2)
    print("It's beaten up, not worn but as if it had been left in mud and marched on. What in the world" +
          "happened?")
    sleep(2)
    print("You get out your water bottle. The water inside is lukewarm, but it's better than nothing.")
    sleep(2)
    print("(hint: type 'backpack' or 'inventory' to check what's inside your backpack.)")
    sleep(2)
    print("Where's Fido? Hopefully he wasn't killed in the avalanche - an avalanche!")
    sleep(5)
    print("You remember now. You were hiking in Alaska, near Anchorage, when an avalanche, " +
          "threw you off the path and into the air. \nYou need to find Fido and get out of here, " +
          "wherever 'here' is.")
    sleep(3)
    command = 'no'
    
print("(Basic commands: look, inventory, inspect [item in inventory])")    
while game_finish == 0:
    #interactive game starts here    

    command = input ('>>')
    if location == room1:
        if (command =='open door') or (command == 'open'):
            door1=1
            print('You open the door to the shack. Light dimly shines from the corridor ahead.')
        for x in ['leave', 'exit', 'forward', 'enter', 'enter corridor', 'exit room']:
            if command==x:
                if door1==0:
                    print('You hit your head on the door! Ouch.')
                elif door1==1:
                    print("You walk into the corridor ahead. There is a chill in the air you can feel even through" +
                               "your winter clothes.")
                    location=corridor1
                    delete(actions, 'open door')
                    delete(actions, 'open')    
                    if flashlight.state==0:
                        print(corridor1.desc_dark)
                    elif flashlight.state==1:
                        print(corridor1.desc_light)
                    else:
                        print('flashlight error 2')
                else:
                    print('door error')    
    if command == 'location':
        print(location.name)    
    if command == 'look':
        look(flashlight.state)
    for x in inventory:
        if (command == x.name) or (command == "inspect " + x.name) or (command == "look " + x.name):
            inspect(x)
    for x in ['bottle', 'inspect bottle', 'look bottle']:
        if command == x:
            inspect(bottle)
    for x in ['inspect backpack', 'backpack', 'bookbag', 'bag', 'inventory', 'look backpack']:
        if command == x:
            for y in inventory:
                print(y.name)
    for x in ['light', 'use flashlight', 'light flashlight', "turn on", "turn on light", 'flashlight on']:
        if command == x:
            flashlight.state = light(flashlight.state) 

    for x in ["drink", "drink water", "use water"]:
        if command == x :
            if bottle.water == "empty":
                print(bottle.desc_empty)        
            if bottle.water == "half":
                bottle.water = "empty"
                print("You drink the remaining half of your water. It's empty now.")            
            if bottle.water == "full":
                bottle.water = "half"
                print("You drink half the water in your bottle.")
                


    if command not in actions:
        print("Sorry, I don't recognize that word.")

print('Out of content. I guess that counts as beating the game?')
game_finish = 1

