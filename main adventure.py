#redoing my text adventure because the other one is all over the place
 
from time import sleep

class room:
    def __init__(self, name, x, y):
        self.name = name
        self.coordinates = [x,y]
        self.desc_dark = ""
        self.desc_light = ""
    
    def checklight():
        if flashlight == 0:
            return 0
        if flashlight == 1:
            return 1
         
def look(flashlight):
    if flashlight == 0:
         print (location.desc_dark)
    if flashlight == 1:
         print (location.desc_light)
    
def light(flashlight):
    if flashlight == 0:
        print('You turn on your flashlight.')
        print(location.desc_light)
        return 1
        
    elif flashlight == 1:
        print("You turn your flashlight off. You can't see for a moment as your eyes adjust.")
        sleep(3)
        print(location.desc_dark)
        return 0
   
def inventory():
    for x in inventory:
         print(x)

        

room1=room('entrance', 0, 0)
room1.desc_dark = 'You find yourself in a dimly lit room. You can make out a closed door, where light is creeping through.'
room1.desc_light = 'You are in a wooden shack.'

corridor1=room('tunnel', 0, 1)
corridor1.desc_dark = 'You see brighter light - it seems to be shining through cracks in the walls. You hear birds chirping.'
corridor1.desc_light = 'You are in a wooden corridor made with crudely cut planks. There is a dirt floor, and you hear birds chirping.'

room2=room('in development', 0, 2)
room2.desc_dark = "In development."
room2.desc_light = "In development."



flashlight = 0
#Boolean, flashlight starts off
location = room1
door1=0
#Boolean, door starts closed
inventory = ['Flashlight']

print(room1.desc_dark)

while True:
    while location == room1:
        command = input ('>>')
        if command == 'open door':
            door1 = 1
            print('You open the door to the shack. Light dimly shines from the corridor ahead')

        elif command == 'location':
            print(location.name)
        elif command == 'light':
            flashlight = light(flashlight)
        elif (command == 'look') or (command == 'look around'):
            look(flashlight)
        elif command == 'inventory':
            inventory()           
        elif command == 'leave':
            if door1==0:
                print('You hit your head on the door! Ouch.')
            elif door1==1:
                print('You walk into the corridor ahead.')
                location=corridor1
                if flashlight==0:
                    print(corridor1.desc_dark)
                elif flashlight==1:
                    print(corridor1.desc_light)
                else:
                    print('flashlight error 2')
        else:
            print('unknown room1')
    while location == corridor1:
        command = input ('>>>')
        
    else:
        print('unknown general')
