from time import sleep

actions = {}

class room:
    def __init__(self, name, x, y):
        self.name = name
        self.coordinates = [x,y]
        self.desc_dark = ""
        self.desc_light = ""
        self.actions = actions
#confirmed error for inspect(str) call
    
    def add_act(self, act, result):
        self.actions.append(act)
        self.actions.append(" : ")
        self.actions.append(result)
#does NOT work, need to change

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
    else:
        print('flashlight error')

def inventory():
    for x in carrying:
        print(x.name)

def inspect(x):
    print(x.desc)
    
def delete(dict, x):
    if x in dict:
        del (x)
#not certain this works. will check once code compiles without error 
      
room1=room('entrance', 0, 0)
room1.desc_dark = ('You find yourself in a dimly lit room. You can make out a closed door, where light is ' +
                       'creeping through.')
room1.desc_light = 'You are in a wooden shack.'

corridor1=room('tunnel', 0, 1)
corridor1.desc_dark = ('You see brighter light - it seems to be shining through cracks in the walls. ' +
                           'You hear birds chirping.')
corridor1.desc_light = ('You are in a wooden corridor made with crudely cut planks. There is a dirt ' +
                            'floor, and you hear birds chirping.')

room2=room('open room', 0, 2)
#name tentatively 'open room', subject to change
room2.desc_dark = "In development."
room2.desc_light = "In development."

flashlight = item("flashlight")
flashlight.desc = ("It's a flashlight. It's bright yellow color and the light is a little dim, but it's enough" +
                       " to make out your surroundings.")
flashlight.state = 0

location = room1
door1=0
#Boolean, door starts closed
carrying=[flashlight]

actions={'location' : print(location.name),
         'look' : look(flashlight.state),
         'inventory' : inventory(), 
         'light' : light(flashlight.state),
         'inspect flashlight' : inspect(flashlight)}
#had to take out 'inspect x' command, couldn't get it to work within a dictionary.




print("You are Prince Corwin of Amber, son of King Oberon, son of Dworkin Barimen.")
print("Your elder brother, Eric, has died in an assault by mysterious forces, an assault you led an army to repel, " + 
      "but not before passing the crown, and more importantly, the Jewel of Amber on to you.")
print("The Jewel of Judgement gives you power over Amber - over the weather, over the castle, and ultimately over the Shadows:")
print("the reflections of Amber, a multiverse of alternate worlds which are similar Amber to a greater or lesser extent," + 
      "before eventually dissolving into infinite Shadows of Chaos.")
print("To use the Jewel, however, you must attune yourself to the Pattern, the magical maze deep underneath the castle of Amber.")

while input("Are you ready to walk the Pattern?") not in ["yes", "Yes", "y", "ready"]:
    print("The Pattern will wait. The Pattern is eternal.")
    


while True:
    actions.append('open door')
    actions.append('open')
    while location == room1:
        command = input ('>>')
        if (command =='open door') or (command == 'open'):
            door1=1
            print('You open the door to the shack. Light dimly shines from the corridor ahead.')
        elif command == 'location':
            print(location.name)    
        elif command == 'look':
            look(flashlight.state)
        elif command =='inventory':
            for x in inventory:
                print(x.name)
        for x in ['light', 'light flashlight', "turn on", "turn on light"]:
            if command == x:
                flashlight.state = light(flashlight.state) 
        for x in ['leave', 'exit', 'forward', 'enter']:
            if command==x:
                if door1==0:
                    print('You hit your head on the door! Ouch.')
                elif door1==1:
                    print('You walk into the corridor ahead.')
                    location=corridor1
                    if flashlight.state==0:
                        print(corridor1.desc_dark)
                    elif flashlight.state==1:
                        print(corridor1.desc_light)
                    else:
                        print('flashlight error 2')
                else:
                    print('door error')
        for x in inventory:
            if (command == x.name) or (command == "inspect " + x.name):
                print(x.desc)
        if command not in actions:
            print("Sorry, I don't recognize that word.")
        
    delete(actions, 'open door')
    delete(actions, 'open')

    print('Out of content. I guess that counts as beating the game?')
    while location == corridor1:
        command = input ('>>')
        if command == 'location':
            print(location.name)    
        elif command == 'look':
            look(flashlight.state)
        elif command =='inventory':
            for x in inventory:
                print(x.name)
        for x in ['light', 'light flashlight', "turn on", "turn on light"]:
            if command == x:
                flashlight.state = light(flashlight.state)
                for x in inventory:
                    if (command == x.name) or (command == "inspect " + x.name):
                        print(x.desc)
        if command not in actions:
            print("Sorry, I don't recognize that word.")
       

