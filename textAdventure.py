### Name: Amir Namini
### Filename: textAdventure.py
### Description:
###     This game allows the user to navigate between different scenarios surrounding "stop" versus
###     "search."  The user can navigate in the story by choosing among different options that game
###     provides.  To make a selection type the provided phrase and return to move to next screen.
###     If not sure, the user can get help on each stage by inputting help.  For more
###     information on how to play the game, please refer to "readme.txt".
### Dependencies:
###     None.
### Help:
###     None.

#==================================================================================================

# Storing all inventories. 
inventories = {}

# Things in inventory. Probably just a list would have done the work.
inventories['list'] = {'current': ['handgun', 'handcuff', 'baton', 'keys'],}

# Storing all seized suspects.
seizes = {}

# Suspects seized. Probably just a list would have done the work. 
seizes['person'] = {'name': [],}

# Storing all rooms.
rooms = {}

# Driving in the car is a room named patrol. 
rooms['patrol'] = {

# Describing the incident in room patrol.
'desc': 'Officer Smith is crusing in his patrol car, when he finds himself on \n' +
    'McAllister St., few blocks from UC Tenderloin. He remembers that his friend, \n' +
    'officer Dodge, is on the shift as a guard that morning. Should officer Smith \n' +
    'call his buddy?',

# Options of the user are stored in actions.
'actions': {'call the friend': 'polkSt', 'keep driving': 'keepDriving'},

# Items stores the things that user can pick or drop into.
'items': ['cell phone'],

# Suspects which is activated only in some rooms, stores possible suspects.
'suspects': [],

# Help stores room specific help. 
'help': 'Type any of the prompts appearing on the screen and press enter to move forward.',

# If there is a handcuf in borrow, allows user to borrow a handcuff.
'borrow': [],

# if False moves the user to the next level and if True exits to the outerloop.
'exit':False
}

# Walking on PolkSt. 
rooms['polkSt'] = {
'desc': 'Dodge agrees to go for a doughnut break. Officer Smith parks his car on Polk St. \n' +
    'and starts walking on McAllister toward the Supreme Court of California. \n' +
    'The Tenderloin neighborhood is known to be the Xanax mecca of San Francisco. \n' +
    'Walking down the street, evidence of drug epidemic is clearly visible. On some corners \n' +
    'users are coming down from their high, while on others hustlers are hustling. \n' +
    'As officer Smith passes the the Supreme Court, something on his right grabs \n' +
    'his attention. Should officer Smith look to his right?',

'actions': {'look to the right': 'civicCenter', 'focus on doughnut': 'ucTenderloin'},

'items': ['used syringes', 'human feces'],

'suspects': [],

'help': "Remember you can always drop stuff from inventory by inputting 'drop' and \n" +
    "pick stuff by inputting 'get'.",

'borrow': [],

'exit':False
}

# Outside the civic center.
rooms['civicCenter'] = {
'desc': 'At the Civic Center lawn, offider Smith sees Mr. Jones, an African American teenager,\n' +
    'standing with his friends. Officer Smith suspects that members of the group may be in \n' +
    'possession of illegal substance. Should officer Smith secure a warrant or approach \n' +
    'the group?',

'actions': {'secure a warrant': 'nineCir', 'approach the group': 'decision'},

'items': [],

'suspects': [],

'help': 'Warrants are granted only based on specific facts indicating probable cause.',

'borrow': [],

'exit':False
}

# Inside the ninth circuit room. 
rooms['nineCir'] = {

'desc': 'Will the magistrate judge issue a warrant?',

'actions': {'warrant issued': 'backAtCivic', "no warrant issued": 'decision'},

'items': [],

'suspects': [],

'help': 'Warrants are granted only based on probable cause.',

'borrow': [],

'exit':False
}

# Outside the ninth circuit.  
rooms['backAtCivic'] = {

'desc': 'Based on the facts, it is unlikely that a magistrate judge would issue a warrant. \n' +
    'Regardless, when officer Smith returns with the warrant, the kids are long gone.',

'actions': {'get doughnut': 'ucTenderloin'},

'items': [],

'suspects': [],

'help': 'This is one reason why the Supreme Court permitted stop on reasonable suspicion.',

'borrow': [],

'exit':False
}

# Decision to stop or arrest.
rooms['decision'] = {
    
'desc': 'Should officer Smith arrest Mr. Jones or proceed with stop and frisk?',

'actions': {'stop and frisk': 'stopAndFrisk', 'arrest jones': 'arrestAndSearch'},

'items': [],

'suspects': [],

'help': 'To arrest someone, police need to have a probable cause.',

'borrow': [],

'exit':False
}

# If the user decides to arrest, the game exits. 
rooms['arrestAndSearch'] = {
'desc': 'Based on the facts, officer Smith does not have any probable cause to arrest the \n' +
    'poor kid. You lose!',

'actions': {},

'items': [],

'suspects': [],

'help': '',

'borrow': [],

'exit':True
}

# If the user decides to stop, the game continues.
rooms['stopAndFrisk'] = {
    
'desc': "Officer Smith yells, 'everyone, stay where you are!' Mr. Jones turns and runs \n" +
    "away. As officer Smith gives chase, he sees Mr. Jones reach into his pocket, \n" +
    'pull out a small object, and throw it to the ground. Officer Smith catches up \n' +
    "to Mr. Jones and tackles him. Mr. Jones starts shouting, 'let me go!' Is officer \n" +
    "Smith obligated to let him go?",

'actions': {'let him go': 'letGo', 'investigate': 'getCoke'}, 

'items': [],

'suspects': [],

'help': 'The Court has held that unprovoked flight in a area of heavy narcotics trafficking \n' +
    'justifies reasonable suspicion.',

'borrow': [],

'exit':False
}

# If the user decides to let the suspect go after tackle.
rooms['letGo'] = {
'desc': "Letting the suspect go may not be the wisest decision.",

'actions': {'grab doughnut': 'ucTenderloin'},

'items': [],

'suspects': [],

'help': '',

'borrow': [],

'exit':False
}

# User picking the evidence before moving to the next room. 
rooms['getCoke'] = {
'desc': 'After waiting for other officers to arrive, including his friend, officer Dodge, \n' + 
    'officer Smith goes back to investigate the object that Mr. Jones discarded during \n' +
    'the chase. Based on what officer Smith will discover on the scene, does \n' +
    'he have to apprehend Mr. Jones?',

'actions': {'apprehend': 'apprehend', "don't apprehend": 'letGo',}, 

'items': ['bag of crack cocaine'],

'suspects': [],

'help': "To pick up the evidence use input 'get'.",

'borrow': ['handcuff'],

'exit':False
}


# After evidence is picked, then user can move to next room: apprehend. If handcuff dropped
# at earlier place, user can borrow one.
rooms['apprehend'] = {

'desc': 'After further investigating content of the bag, officer Smith put Mr. Jones under \n' +
    'arrest for possession of crack cocaine. Does he have to read the miranda warning?',

'actions': {'read miranda warning': 'readMiranda', 'put suspect in patrol car': 'arrestForCoke'},

'items': [],

'suspects': ['jones'],

'help': "To arrest use input 'arrest'. If no handcuff, input borrow.",

'borrow': ['handcuff'],

'exit':False
}

# Read miranda. 
rooms['readMiranda'] = {

'desc': 'You have the right to remain silent and refuse to answer questions. \n' +
    'Anything you say may be used against you in a court of law. you have the \n' +
    'right to consult an attorney before speaking to the police and to have an \n' +
    'attorney present during questioning now or in the future. If you cannot \n' +
    'afford an attorney, one will be ppointed for you before any questioning if \n' +
    'you wish. If you decide to answer questions now without an attorney present \n' +
    'you will still have the right to stop answering at any time until you talk to \n' +
    'an attorney.',

'actions': {'put suspect in patrol car': 'arrestForCoke'},

'items': [],

'suspects': ['jones'],

'help': "To arrest use input 'arrest'. \n" +
    "Note: Miranda warnings apply when the suspect is formally in police \n" +
    'custody and the suspect is being interrogated. Here, because the \n' +
    'suspect is not being interrogated, Miranda warning may not apply.',

'borrow': ['handcuff'],

'exit':False
}

# Putting suspect in the patrol car, game exits.
rooms['arrestForCoke'] = {

'desc': 'Officer Smith helps Mr. Jones inside the car. Before getting into his car to take \n' +
    "Mr. Jones to the police station, officer Smith says to his friend, 'There goes our \n" +
    "doughnut date!' \n" +
    "Note: Although officer Smith didn't get to enjoy his doughnut, he did the right \n" +
    "thing. C'est la vie!",

'actions': {},

'items': [],

'suspects': [],

'help': '',

'borrow': [],

'exit': True
}

# UC Tenderloin to get doughnut, game exits. 
rooms['ucTenderloin'] = {
'desc': 'Although officer Smith failed to do the right thing, at least he gets to \n' +
    "enjoy a doughnut with his buddy. C'est la vie!",

'actions': {},

'items': [],

'suspects': [],

'help': '',

'borrow': [],

'exit':True
}

# Keep driving, if user decides to keep drive. 
rooms['keepDriving'] = {

'desc': 'This is boring!',

'actions': {'call up': 'polkSt', 'keep driving': 'keepDriving'},

'items': [],

'help': '',

'borrow': [],

'exit':False
}

    
# The main game loop.
room = rooms['patrol']

# Print story based on desc of current room.
print(room['desc'])

# While the game is not over.
while not(room['exit']):

    # Indexing rooms.
    nextRoom = None

    # For shorthand and poiting the code to inventories dictionary, define inventory. 
    inventory = inventories['list']

    # For shorthand and poiting the code to seizes dictionary, define seize. 
    seize = seizes['person']

    # While in the current room and waiting for user's input.
    while not nextRoom:

        # Prompt to select.
        print('You can . . .')

        # Iterating and printing values stored in actions' key. 
        for possibleAction in room['actions'].keys():
            print('\t' + possibleAction)

       
        # Receive user's argument to control narrative. 
        userInput = input('> ')
        userInput = userInput.strip().lower()


        # Verbs or actions that aren't room-specific.
        # Help: provides legal hint. 
        if userInput == 'help' or userInput == 'h':
            print(room['help'])
            
        # Inventory: shows content of inventory.
        elif userInput == "inv" or userInput == 'i' or userInput == 'inventory':
            print(inventory['current'])

        # See: shows what items are around for get action. 
        elif userInput == 'see':
            print(room['items'])

        # Suspects: shows if there are suspects in the room.
        elif userInput == 'suspects':
            print(room['suspects'])
            
        # Get: allows user to pick up an item if such item is available in the room.
        elif userInput == 'get':
                
            # Print the items in the room, and receive user input to control.
            for possibleItem in room['items']:
                print('\t' + possibleItem)
            userInput = input('> ')
            userInput = userInput.strip().lower()

            # Add the item to inventory and delete from the room.
            if userInput in room['items']: 
                add = inventory['current'].insert(0, userInput)
                addDrop = room['items'].remove(userInput)

            # If user's input not in room. 
            else:
                print('Item not found')
                    
        # Drop: allows user to drop a thing if that thing is in inventory. 
        elif userInput == 'drop':
            
            # Show things in inventory to discard, and receive input to dicard.
            for possibleThing in inventory['current']:
                print('\t' + possibleThing)
            userInput = input('> ')
            userInput = userInput.strip().lower()

            # Drop thing from current inventory and add to items of the room.
            if userInput in inventory['current']:
                drop = inventory['current'].remove(userInput)
                dropAdd = room['items'].insert(0, userInput)
            
            # If user's input is not in inventory.
            else:
                print("Can't get rid of what you don't have.")
                 

        # Other actions that are room specific. 
        # Ability to borrow a handcuff if dropped earlier.
        elif userInput == 'borrow':

            # If there are handcuffs to borrow, add to inventory and delete from room.
            if 'handcuff' in room['borrow']:
                borrow = inventory['current'].insert(0, 'handcuff')
                deleteBorrow = room['borrow'].remove('handcuff')

            # If no one to borrow, print to that effect.
            elif 'handcuff' not in room['borrow']:
                print('No one to borrow from.')

                
        # Arrest: in some rooms, user must arrest the person before putting in car.    
        elif userInput == 'arrest':
 
            # Review and print content of suspects, and receive input of user.
            for possibleSuspect in room['suspects']:
                print('\t' + possibleSuspect)
            userInput = input('> ')
            userInput = userInput.strip().lower()

            # Seize the suspect with handcuff if suspect is in that room.
            if userInput in room['suspects']:
                
                # If handcuff in inventory, arrest possible. Remove handcuff from inventory,
                # add suspect to seizes dictionary and delete suspect from the room.
                if 'handcuff' in inventory['current']:
                    handcuffDrop = inventory['current'].remove('handcuff')
                    arrestSuspect = seize['name'].insert(0, userInput)
                    suspectDrop = room['suspects'].remove(userInput) 

                # If user dropped a handcuff, shows which room handcuff was dropped.
                elif 'handcuff' != inventory['current']:

                    # The two for loops will search to see in which room the handcuff was dropped.
                    handcuffRoom = ''
                    for handcuffRoom in rooms.keys():
                        for item in rooms[handcuffRoom]['items']:
                            if item == 'handcuff':
                                print('Left handcuff in ' + handcuffRoom + '.')
                        
                # If suspect is not in the room.
                else:
                    print('Suspect not found.')
                
        # Must get evidence to change room.
        elif userInput == 'apprehend':

            # If user has not get the evidence.
            if 'bag of crack cocaine' in room['items']:
                print('Must pick the evidence first.')

            # If got the evidence, move to next room. 
            if 'bag of crack cocaine' in inventory['current']:
                nextRoom = rooms[room['actions'][userInput]]

        # Must arrest suspect before get him into patrol. 
        elif userInput == 'put suspect in patrol car':

            # If user has not arrested the suspect. 
            if 'jones' not in seize['name']:
                print('Must arrest the suspect first.')

            # If user has put suspect under arrest. 
            elif 'jones' in seize['name']:
                nextRoom = rooms[room['actions'][userInput]]
                
                
        # Changing to other rooms, generally, based on user's input.
        elif userInput in room['actions'].keys():
            nextRoom = rooms[room['actions'][userInput]]
           
        # If user's input is not supported by the game.
        else:
            print(userInput + ' is not supported. Please try again.')

    # Move to next room.        
    room = nextRoom
    print(room['desc'])
        
# Outside the game loop.
print('Thanks for playing!')
                             

        

        



        



        

      




    


