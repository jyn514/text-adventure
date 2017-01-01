
class room:
    def __init__(self, name, coordinate):
        self.name = name
        self.acts = []
        self.acts.append(light)
        self.coordinate = []

    def add_act(self, act):
        self.acts.append(act)

    def prompt():
        command = (input('>'))
        if command == 'light':
            light()
        elif command == act:
            pass
               

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
              
def north():
    location [1]+1

def south():
    location [1]-1

def east():
    location [0]+1

def west():
    location [0]-1

room1 = room('entrance', [0,0])
room1.desc_dark = 'You find yourself in a dimly lit room. You can make out a closed door, where light is creeping through.'
room1.add_act ('flashlight')
room1.add_act ('look around')
room1.add_act ('open door')
room1.desc_light = 'You are in a wooden shack.'

corridor1 = room('tunnel', [0,1])
corridor1.desc_dark = 'You see brighter light - it seems to be shining through cracks in the walls. You hear birds chirping.'
corridor1.desc_light = 'You are in a wooden corridor made with crudely cut planks. There is a dirt floor, and you hear birds chirping.'
corridor1.add_act ('back')
corridor1.add_act ('forward')

room2 = room('open room', [0,2])



location = room1

flashlight=0

print (location.desc_dark)

while True:
    command = input('>')

    if command == 'location':
        print(location)
        
    if command == 'light':
        light(flashlight)

    else:
        print('You have entered an unknown value.')

    while location == room1:
        if command == 'open door':
            room1.add_act ('exit room')
            print ('You see more light shining through a hallway ahead.')

        elif command == 'exit room' or 'leave':
            location=corridor1
            if flashlight==0:
               print ('dark corridor')
            if flashlight == 1:
                print ('lit corridor')
        else:
            print('You have entered an unknown value.')

    #need to make this a function

    while location == corridor1:
        if command =='forward' or 'straight' or 'keep going':
            location = room2
            if flashlight==0:
                print ('dark room')
            if flashlight == 1:
                print ('lit room')
        else:
            print('You have entered an unknown value.')
