from time import sleep
#classes
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
#functions
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
    print("Your water bottle. It's made of a light metal, maybe aluminum.", end=" ")
    if water == "full":
        print(bottle.desc_full)
    elif water == "half":
        print(bottle.desc_half_full)
    elif water == "empty":
        print(bottle.desc_empty)
    else:
        print('error')

def inspect(x):
    if x in inventory:
        print(x.desc)
    else:
        print("You can't inspect things that aren't in your backpack. Try looking instead.")

def help(location):
    print("Actions available: ")
    for x in base_acts:
        print(x, end=", ")
    for x in location.acts:
            print(x, end=", ")
    print("\n")

#static variables

room1=room('A mysterious shack.', 0, 0)
room1.desc_dark = ('You find yourself in a dimly lit room. You can make out a closed door, where light is ' +
                       'creeping through.')
room1.desc_light = ('Your flashlight is brighter than you expected in the dim room. The room is made of wood planks, ' +
                       'and the ceiling is sloped. There is a chest in the middle of the room.')

corridor1=room('A snow-filled corridor.', 0, 1)
corridor1.desc_dark = ("There's a hole in the roof. There's a ton of snow all over the passageway, and even with the light of the " +
                       "moon, you can't see to the end of the corridor.")
corridor1.desc_light = ("This whole corridor looks ready to collapse. The room has already caved in, and there's snow  " +
                        "all over the passageway. Broken planks stick out here and there amongst the wreckage. At the end of "+
                        "the passage, you can just make out a closed door.")

corridor2=room('An abandoned basement.', 0, 2)
corridor2.desc_dark = ("The snow is everywhere down here. The corners are dark and musty, although a harsh wind is quickly sweeping " +
                       "the smell away.\nYou've got to get out of here, but you can't see an exit in this accursed snow.")
corridor2.desc_light = ("The snow above is nothing compared to the snow here, which fills the room. "
                        "It looks like this was a basement in another time. There's a broom in the corner and some kitchen supplies. " +
                        "\nThere's a ladder up to the corridor above, if you're careful you might be able to climb it. " +
                        "If there's another exit, it's been buried by the snow.")

room1new=room("A mysterious shack.", 0, 0)
room1new.desc_dark = ("This is the room you woke up in. The door is ajar and you can see the remains of the collapsed " +
              "corridor through it.")
room1new.desc_light = ("This is the room you woke up in. It held up surprisingly well to the snow, which spills in from the ajar " +
                       "door. There's a chest in the center of the room.")

flashlight = item("flashlight")
flashlight.desc = ("It's a flashlight. It's bright yellow color and the light is a little dim, but it's enough " +
                       "to make out your surroundings.")
flashlight.state = 0

backpack = item("backpack")
backpack.desc = ("Your handy backpack. You brought it when you went hiking. It's a lot dirtier now than it " +
                 "was then. It contains: \n")

bottle = item("water bottle")
bottle.water = "full"
bottle.desc_full =  "It's full to the brim, and a little heavy to carry."
bottle.desc_half_full = "It's half-full, and lighter than it was."
bottle.desc_empty = "It's dry. There's a couple droplets left, but they're resolutely clinging to the bottom."
                       
key = item("key")
key.desc = "An old iron key, worn by time. Perhaps you'll find a use for it later."

note = item("note")
note.desc = "A hastily scribbled note. It says 'Key to door. Remember, lock turns right.'"

chest = item("wooden chest")
chest.desc = "A hand-crafted chest that looks as if it's seen better days. It contains:"
chest.contents = [key, note] 

broom = item("wooden broom")
broom.desc = "An old, wooden, broom. What could be its use?"
corridor2.contents=[broom]

#action lists
start_acts = ['yes', 'no', 'quit', 'y', 'n']
room1.acts = ['open door', 'enter corridor']
corridor1.acts = ['back', 'forward', 'look door', 'open door', 'clear snow']
corridor2.acts = ['climb ladder']
room1new.acts = ['open chest', 'look chest', 'take key', 'take note', 'descend ladder']
base_acts = ['help', 'quit', 'location', 'look', 'inspect item',
         'inventory', 'light flashlight', 'drink']


#dynamic variables
location = room1
door1=0
game_finish = 0 
inventory=[backpack, flashlight, bottle]
check_action = 0
    
#intro starts here
print("Would you like to watch the intro? It adds a story to the game. (yes/no/quit)")
command = input(">>")
k=0    
while not(command in ['yes', 'no', 'y', 'n']):
    if command in ['quit', 'quit()', 'exit', 'exit()']:
        quit()
    else:
        if k>=3:
            print("Press Ctrl+D twice to force-close the game.")
        print("Please type yes or no, or type 'quit' to exit the game.")
        k+=1
        command = input(">>")
        
if command == 'no' or command=='n':
    def loading(action, time):
        pass
    def prints(str):
        print(str)
    print("All loading sequences will be skipped.")    
if command == 'yes' or command == 'y':       
    def loading(action, time):
        print(action, end = " ")
        loading = 0
        while loading < time:
            sleep(1)
            loading += 1
            print(".", end = " ")
        print("\n")
    def prints(str):
        print(str)
        sleep(2)
    prints(room1.desc_dark)
    print("You can't remember how you got here. The last thing you remember is hiking with your dog, Fido, ", end="")
    loading('in', 5)
    prints("Where were you hiking? God, your head hurts. Maybe a glass of water would do you good. \n" +
          "You reach into your backpack.")
    prints("It's beaten up, as if it had been left in mud and marched on. What in the world " +
          "happened?")
    prints("You get out your water bottle. The water inside is lukewarm, but it's better than nothing. ")
    prints("(hint: type 'backpack' or 'inventory' to check what's inside your backpack.)\n")
    print("Where's Fido? Hopefully he wasn't killed in the", end=" ")
    loading("avalanche", 3)
    prints(" -- an avalanche! ")
    prints("You remember now. You were hiking in Alaska, near Anchorage, when an avalanche, " +
          "threw you off the path and into the air. \nYou need to find Fido and get out of here, " +
          "wherever 'here' is.")

help(location)
while game_finish == 0:
#interactive game starts here    
    check_action = 0
    for x in ['take ', 'use ', 'look ']:
        if x in command:
            temp = command.replace(x, "")
            print(temp)
    command = input ('>>')
    if location == room1:
        if (command =='open door') or (command == 'open'):
            door1=1
            check_action += 1
            print('You open the door to the shack. Light dimly shines from the corridor ahead.')
        for x in ['look chest', 'chest', 'open chest', 'look at chest']:
            if command == x:
                print(chest.desc)
                for x in chest.contents:
                    print(x.name)
                check_action += 1
        for x in chest.contents:
            for y in [x.name, "inspect " + x.name, "look " + x.name, "look at " + x.name]:
                if command == y:
                    print (x.desc)
                    check_action += 1
            if (command == "take " + x.name):
                inventory.append(x)
                print("You take the " + x.name + ".")
                check_action += 1
                chest.contents.remove(x)
        
        for x in ['leave', 'leave room', 'exit', 'corridor', 'forward', 'enter', 'enter corridor', 'enter door', 'exit room']:
            if command==x or command == "go " + x:
                check_action += 1
                if door1==0:
                    print('You hit your head on the door! Ouch.')
                elif door1==1:
                    prints("You walk into the corridor ahead. There is a chill in the air you can feel even through " +
                               "your winter clothes.")
#location changes to corridor1
                    location=corridor1
                    if flashlight.state==0:
                        print("It's night-time out, and your eyes are starting to adjust to the light of the moon.")
                        loading("Your eyes are adjusting", 3)
                    look(flashlight.state)              
    if location == corridor1:
        for x in ['back', 'room1', 'entrance', 'turn around']:
            if (command == x) or (command == "go" + x):
                check_action += 1
                location = room1
                look(flashlight.state)
        for x in ['forward', 'door', 'end of corridor']:
            if command in [x, "go " + x, "look " + x, "look at " + x]:
                print("You walk through the dense snow. It's hard to find your footing, good thing you're wearing boots.")
                print("At the end of the corridor, the snow is even thicker, piling up against the door in a giant drift. " +
                      "It's a blinding white even in the moonlight. You can feel wind blow in from outside, " +
                      "an icy breeze that chills you to the bone.")
                print("The door itself is made of a dark thick wood, made darker by melted snow. " +
                      "Its rusted hinges face you on your left.")
                check_action += 1
        if command == 'open door':
            print("It's stuck. The snow is piled against it, forcing it shut.")
            sleep(1)
            print("(hint: type 'clear snow' to open the door)")
            check_action += 1
        if command in ['clear snow', 'move snow', 'push snow']:
            print("The snow is, quite literally, freezing cold. Good thing you've got your ski clothes on.")
            loading("Pushing snow", 5)
            location = corridor2
            corridor_collapsed = 1
            print("There's an avalanche! The snow is collapsing, run!")
            sleep(1)
            print("Too late, you're falling!")
            sleep(1)
            prints("You've fallen through the floor! It's a miracle you weren't killed in the collapse.") 
            print("There's a basement here - good thing, too, or you would have been buried by the snow.")
            look(flashlight.state)
            check_action += 1
#location changes to corridor2
    if location==room1new:
        for x in ['look chest', 'chest', 'open chest', 'look at chest']:
            if command == x:
                print(chest.desc)
                for x in chest.contents:
                    print(x.name)
                check_action += 1
        for x in chest.contents:
            for y in [x.name, "inspect " + x.name, "look " + x.name, "look at " + x.name]:
                if command == y:
                    print (x.desc)
                    check_action += 1
            if (command == "take " + x.name):
                inventory.append(x)
                print("You take the " + x.name + ".")
                check_action += 1
                chest.contents.remove(x)
        for x in ['back', 'climb', 'climb down', 'descend', 'basement']:
            if command==x or command=="go " + x:
                print("You climb down the ladder.")
                location=corridor2
                look(flashlight.state)
                check_action+=1
    if location == corridor2:
        if command in ['climb ladder', 'climb', 'use ladder', 'climb up']:
            if flashlight.state==1:
                loading("Climbing ladder", 3)
#location changes to room1new
                location = room1new
                look(flashlight.state)
            else:
                print("You can't see well enough to climb in the dark.")
            check_action=1
        if command == 'take broom':
            if broom in corridor2.contents:    
                inventory.append(broom)
                corridor2.contents.remove(broom)
                print("You take the broom.")
            else:
                print("The broom is already in your inventory.")
        for x in ['use broom', 'sweep']:
            if command==x or command==x+" snow":
                print("You sweep the snow out of the way using the broom. ")
    if command == 'help':
        help(location)
        check_action+=1
    if command == 'location':
        check_action += 1
        print(location.name)    
    if command == 'look':
        check_action += 1
        look(flashlight.state)
    for x in inventory:
        if command in ['bottle', 'inspect bottle', 'look bottle', 'look at bottle']:
            break
        elif command in [x.name, "inspect " + x.name, "look " + x.name, "look at " + x.name]:
            inspect(x)
            check_action += 1
    if command == 'inspect':
        print(eval(temp))
        inspect(temp)
        check_action+=1
    if command == 'use':
        doc = open('main-adventure.py')
        exec(println(doc.search('use ' + temp)+1))
    if command in ['bottle', 'inspect bottle', 'look bottle', 'look at bottle']:
        check_water(bottle.water)
        check_action += 1 
    for x in ['inspect backpack', 'backpack', 'bookbag', 'bag', 'inventory', 'look backpack', 'look at backpack']:
        if command == x:
            for y in inventory:
                print(y.name)
                check_action += 1
    for x in ['light', 'use flashlight', 'light flashlight', "turn on", "turn on light", 'flashlight on',
              'turn on flashlight', 'turn flashlight on']:
        if command == x:
            flashlight.state = light(flashlight.state) 
            check_action += 1
    for x in ["drink", "drink water", "use water"]:
        if command == x :
            check_action += 1
            if bottle.water == "empty":
                print(bottle.desc_empty)        
            if bottle.water == "half":
                bottle.water = "empty"
                print("You drink the remaining half of your water. It's empty now.")            
            if bottle.water == "full":
                bottle.water = "half"
                print("You drink half the water in your bottle.")
    if command == 'quit' or command == 'quit()':
        quit()
    if check_action == 0:
        if " " in command:
            print("I don't recognize that phrase. If you only typed one word, please remove any spaces.")
            if "inspect" in command:
                print("You can only inspect items in your inventory. Try looking instead (not all objects can be looked at).")
            elif 'kill' in command:
                print("You don't have a weapon.")
            elif 'take ' in command:
                print("You tried to take something that the game doesn't allow. Perhaps it is already in inventory, or doesn't exist.")
        else:
            print("Sorry, I don't recognize that word.")
        
print('Out of content. I guess that counts as beating the game?')
quit()
