from time import sleep

class room:
    def __init__(self, name, x, y):
        self.name = name
        self.coordinates = [x,y]
        self.desc_dark = ""
        self.desc_light = ""
    
    def checklight():
        if flashlight.state == 0:
            return 0
        if flashlight.state == 1:
            return 1

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

      
room1=room('entrance', 0, 0)
room1.desc_dark = ('You find yourself in a dimly lit room. You can make out a closed door, where light is ' +
                       'creeping through.')
room1.desc_light = 'You are in a wooden shack.'

corridor1=room('tunnel', 0, 1)
corridor1.desc_dark = ('You see brighter light - it seems to be shining through cracks in the walls. ' +
                           'You hear birds chirping.')
corridor1.desc_light = ('You are in a wooden corridor made with crudely cut planks. There is a dirt ' +
                            'floor, and you hear birds chirping.')

room2=room('in development', 0, 2)
room2.desc_dark = "In development."
room2.desc_light = "In development."

flashlight = item("flashlight")
flashlight.desc = ("It's a flashlight. It's bright yellow color and the light is a little dim, but it's enough" +
                       " to make out your surroundings.")
flashlight.state = 0

location = room1
door1=0
#Boolean, door starts closed
inventory=[flashlight]

actions=['location', 'look', 'inventory', 'light', 'light flashlight', 'leave', 'exit', 'forward', 'flashlight',
         'Flashlight', "inspect flashlight", "enter"]
def delete(list, x):
    if x in list:
        x=[]
#needs to be dictionary, not list. will fix when i have time to figure it out



print(room1.desc_dark)
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
       
