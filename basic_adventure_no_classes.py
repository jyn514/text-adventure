#redoing my text adventure because the other one is all over the place
 
from time import sleep

def light():
    if flashlight == 0:
        print('You turn on your flashlight.')
        flashlight = 1
        print(location.desc_light)
        
    elif flashlight == 1:
        print("You turn your flashlight off. You can't see for a moment as your eyes adjust.")
        flashlight = 0
        sleep(3)
        print(location.desc_dark)
        
    else:
        print('flashlight error')

flashlight=0
#Boolean, flashlight starts off
location=room1
door1=0
#Boolean, door starts closed

room1.desc_dark = 'You find yourself in a dimly lit room. You can make out a closed door, where light is creeping through.'
room1.desc_light = 'You are in a wooden shack.'

corridor1.desc_dark = 'You see brighter light - it seems to be shining through cracks in the walls. You hear birds chirping.'
corridor1.desc_light = 'You are in a wooden corridor made with crudely cut planks. There is a dirt floor, and you hear birds chirping.'

room2.desc_dark = "In development."
room2.desc_light = "In development."

while True
    command = input ('>')
    if command == 'location':
        print(location)
    if command == 'location':
        light()
    while location == room1:
        command = input ('>')
        if command == 'open door' or 'open':
            door1=1
            print('You open the door to the shack. Light dimly shines from the corridor ahead')
        if command == 'leave' or 'leave room' or 'forward' or 'corridor':
            if door1==0:
                print('You hit your head on the door! Ouch.')
            if door1==1:
                print('You walk into the corridor ahead.')
                location=corridor1
                if flashlight==0:
                    print(corridor1.desc_dark)
                if flashlight==1:
                    print(corridor1.desc_light)
