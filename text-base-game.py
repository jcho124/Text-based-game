import time
import random

# game function 
def game():
    time.sleep(1)
    
    print("You wake up in a dark room, but you can make out a flashflight near you.")

    # take flashlight
    while True:
        q1 = input("Do you take it? [y/n]: ")
        if q1 in ["y", "yes"]:
            print("You have picked up the flashlight.")
            break
        elif q1 in ["n", 'no']: #loop q1 until y/yes
            print("You can't see anything, so you should probably take it.")

    time.sleep(2)
    print("You turn on the flashlight and the room illuminates.")
    time.sleep(1)
    print("You see a closed door in front of you.")

    # door open
    q2 = input("try opening? [y/n]")
    if q2 in ["y", "yes"]:
        print("door is locked.")

    else:
        print("you left the door alone.")
          
    time.sleep(2)
    print("By your side, you see a bed and a shelf.")

    # bed or shelf
    while True:
        q3 = str(input("which do you approach?"))
        if q3 in ["bed"]:  # if choose bed
            print("you shine the flashlight under the bed and find a key.")
            key = 1 #find key
            time.sleep(1)

            while True: #approach shelf next
                q4 = str(input("approach shelf?"))
                if q4 in ["y", "yes"]:
                    print("you shine the flashlight to the shelf and find a knife.")
                    knife = 1 #find knife
                    break
                elif q4 in ["n", 'no']:
                    print("there's noting else you can do, so try again")

            break

        if q3 in ["shelf"]:  # if choose shelf
            print("you shine the flashlight to the shelf and find a knife")
            knife = 1
            time.sleep(1)

            while True:
                q5 = str(input("approach bed?"))
                if q5 in ["y", "yes"]:
                    print("you shine the flashlight under the bed and find a key")
                    key = 1
                    break
                elif q5 in ["n", 'no']:
                    print("there's nothing else you can do, so try again")
            break

    time.sleep(2)
    # open door
    # at this point knife=1, key=1
    while True:
        q6 = input("open the door with the key? [y/n]")
        if q6 in ["y", "yes"]:
            print("door opened")
            break
        else:
            print("you should open the door")

    time.sleep(2)
    print("You left the room and entered a dark hallway")
    time.sleep(2)
    print("You make out a small glowing object at the end of the hall")
    time.sleep(1)
    q7 = str(input("Approach the object? [y/n]"))
    if q7 in ["yes", "y"]:
        print("you approach the object slowly...")
        time.sleep(2)
        print("as you get closer, the object multiplies into tiny little eyes")
        time.sleep(1)
        print("The eyes belong to a giant spider!")
        q8 = str(input("Do you try to fight it? [y/n]"))

        # fight with spider
        if q8 in ["y", "yes"]:

            if knife == 1:
                print("you lunge at the spider with your knife!")
                time.sleep(2)
                print("=================================================")
                print("                 Begin Battle...                 ")
                print("    YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print("IF THE SPIDERR HITS HIGHER THAN YOU, YOU WILL DIE")
                print("=================================================")
                time.sleep(2)


            cdmg = int(random.randint(3, 10)) #generates random attack of character
            hdmg = int(random.randint(1, 5))  #generates random attack of spider
            print("You hit a ", cdmg)
            print("Spider hits a ", hdmg)
            time.sleep(2)

            if cdmg < hdmg: #character dies
                print("The spider has dealt more damage than you!")
                complete = 0


            elif cdmg1 < 5: #character hits enough to escape
                print("You didn't do enough damage but you managed to get away.")
                complete = 1

            else: #kill spider
                print("You killed the spider!")
                complete = 1

        else: #choose not to fight but die anyway
            print("You choose not to fight the spider.")
            time.sleep(1)
            print("As you turn away, the spider ambushes you and kills you!!!")
            complete = 0


    else: #don't apprach the object and die
        print("you turn away from the object, and try to find another escape")
        time.sleep(1)
        print("But the object notices you and reveals itself to be a giant spider!")
        time.sleep(1)
        print("The spider ambushes you and kills you!!!")
        complete = 0

    # character dead or alive, try again option
    while True: 
        if complete == 1: #win
            print("You managed to escape the dark hall alive!")
            play_again =input("Try again?")
            if play_again in ["yes","Yes","y"]:
                game()
            else:
                break

        else: #lose
            print("You have died!")
            play_again =input("Try again?")
            if play_again in ["yes","Yes","y"]:
                game()
            else:
                break

game()
