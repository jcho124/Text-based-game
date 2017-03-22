import time
import random


def game():
    time.sleep(1)


print("You wake up in a dark room, but you can make out a flashflight near you.")

# take flashlight
while True:
    ch1 = str(input("Do you take it? [y/n]: "))
    if ch1 in ["y", "yes"]:
        print("you have picked up the flashlight.")
        break
    elif ch1 in ["n", 'no']:
        print("you should prob take it.")

time.sleep(2)
print("you turn on the flashlight and the room illuminates and you see a closed door.")

# door open
ch3 = str(input("try opening? [y/n]"))
if ch3 in ["y", "yes"]:
    print("door is locked.")

else:
    print("you left the door alone.")
time.sleep(2)

print("there is a bed and a shelf.")

# bed or shelf
while True:
    ch4 = str(input("which do you approach?"))
    if ch4 in ["bed"]:  # if bed
        print("you shine the flashlight under the bed and find a key.")
        key = 1
        time.sleep(1)

        while True:
            ch6 = str(input("approach shelf?"))
            if ch6 in ["y", "yes"]:
                print("you shine the flashlight to the shelf and find a knife.")
                knife = 1
                break
            elif ch6 in ["n", 'no']:
                print("try again")

        break

    if ch4 in ["shelf"]:  # if shelf
        print("you shine the flashlight to the shelf and find a knife")
        knife = 1
        time.sleep(1)

        while True:
            ch5 = str(input("approach bed?"))
            if ch5 in ["y", "yes"]:
                print("you shine the flashlight under the bed and find a key")
                key = 1
                break
            elif ch5 in ["n", 'no']:
                print("try again")
        break

time.sleep(2)
# open door
while True:
    ch7 = str(input("open the door with the key? [y/n]"))
    if ch7 in ["y", "yes"]:
        print("door opened")
        break
    else:
        print("you should open the door bro")

time.sleep(2)
print("You left the room and entered a dark hallway.")
time.sleep(2)
print("You see a glowing object at the end of the hall")
time.sleep(1)
ch8 = str(input("Approach the object? [y/n]"))
if ch8 in ["yes", "y"]:
    print("you approach the object...")
    time.sleep(2)
    print("As you draw closer, you begin to make out the object as an eye...")
    time.sleep(1)
    print("The eye belongs to a huge MONSTER!!!")
    ch9 = str(input("Do you try to fight it? [y/n]"))

    # fight
    if ch9 in ["y", "yes"]:

        # with knife
        if knife == 1:
            print("you lunge at the MONSTER with your knife!")
            time.sleep(2)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                    Fighting...                   ")
            print("    YOU MUST HIT ABOVE A 5 TO KILL THE MONSTER   ")
            print("IF THE MONSTER HITS HIGHER THAN YOU, YOU WILL DIE")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(2)


        cdmg1 = int(random.randint(3, 10))
        hdmg1 = int(random.randint(1, 5))
        print("You hit a ", cdmg1)
        print("Monster hits a ", hdmg1)
        time.sleep(2)

        if cdmg1 < hdmg1:
            print("The monster has dealt more damage than you!")
            complete = 0


        elif cdmg1 < 5:
            print("You didn't do enough damage but you managed to get away.")
            complete = 1

        else:
            print("You killed the monster!")
            complete = 1

    else:
        print("You choose not to fight the monster.")
        time.sleep(1)
        print("As you turn away, the monster ambushes you and kills you!!!")
        complete = 0


else:
    print("you turn away from the object, and attempt to flee...")
    time.sleep(1)
    print("But the object notices you and reveals itself to be a giant monster!")
    time.sleep(1)
    print("The heptopod ambushes you and kills you!!!")
    complete = 0

alive = True
while alive:
    complete = game()
    if complete == 1:
        alive = input("You managed to escape the hall alive!")
        break

    else:
        alive = input("You have died!")

        break








