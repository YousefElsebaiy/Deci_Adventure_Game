# ##import library##


import time
import random


# ##variable##


score = 0


# ##function##


def pause(input_txt):
    print(input_txt)
    time.sleep(2)


def start_game():
    global score
    print("You find yourself in a forest full of predatory animals")
    pause("and tall grasses called the Cursed Forest")
    print("You remember some rumors that")
    pause("this forest has strange monsters and witches")
    print("Rumors say that no one enters")
    pause("or leaves the forest unless he is dead")
    pause("Now you start thinking about discovering the forest")
    print('1. Walk to explore the forest \n2. Stay where you are')
    while True:
        choice = input("Enter Your choice (1 or 2)\n")
        if choice == '1':
            score += 10
            explore_the_forset()
            break
        elif choice == '2':
            stay_where_your_self()
            break
        else:
            print("please try again")


def explore_the_forset():
    global score
    print("you started walking and exploring the forest")
    pause("and heard some voices, so you followed her")
    print("I found a wizard chanting spells,and when I stood on a tree branch")
    pause("it made a sound that made the wizard see me.")
    pause("what will you do")
    print("1. Run away\n2. I'm trying to ask him something")
    while True:
        choice = input("Enter Your choice (1 or 2)\n")
        if choice == '1':
            score -= 10
            run_away()
            break
        elif choice == '2':
            score += 10
            ask()
            break
        else:
            print("please try again")


def stay_where_your_self():
    global score
    print("You are now standing in your place, night has fallen upon you")
    pause("and creatures that fear the light have appeared.")
    print("what will you do")
    print("1. run away\n2. lighting a fire\n3. calling for help")
    while True:
        choice = input("Enter your choice (1, 2 or 3)\n")
        if choice == '1':
            if score != 10:
                score = 0
            else:
                score -= 10
            run_away()
            break
        if choice == '2':
            score += 10
            fire()
            break
        if choice == '3':
            score += 5
            call()
            break
        else:
            print("please try again")


def run_away():
    global score
    print("You start running while making a sound of fear,")
    pause("and one of the monsters hears you and starts chasing you.")
    print("The monster is faster than you, so it catches you and kills you.")
    print("Game over")
    print("You want play again (1 'for yes' or 2 'for no')")
    while True:
        choice = input("Enter your choice: \n")
        if choice == '1':
            pause("ok")
            pause("\n\nStart game now\n\n")
            score = 0
            start_game()
            break
        if choice == '2':
            pause("Thank you for played this game")
            print("bye bye")
            break
        else:
            print("plase try again")


def ask():
    global score
    print("You begin to ask the wizard about")
    pause("this forest with fear and hesitation")
    print("He answers you and says: 'This forest is enchanted,")
    print("filled with many nocturnal monsters,")
    pause("and it is rare to find a monster during the day")
    print("You need to find shelter, and I will give you a magical staff")
    pause("that grants you some abilities to survive")
    pause("You take the staff and begin searching for shelter.")
    pause("You find a cave as you walk.")
    print("1. You enter the cave.\n2. Continues walking")
    while True:
        choice = input("Enter your choice (1 or 2): \n")
        if choice == '1':
            score += 10
            cave()
            break
        elif choice == '2':
            continue_explore()
            break
        else:
            print("please try again")


def call():
    pause("Starts calling for help")
    pause("A wizard appears and rescues you")
    pause("The wizard orders you to walk with him.")
    ask()


def fire():
    global score
    pause("You start to light the fire")
    pause("The monsters begin to flee in fear of the light")
    pause("The sun rises,and you contemplate walking and exploring the forest")
    pause("You find a wizard's house.")
    print("1. You go to the wizard's house and ask him about something.")
    pause("2. Continues walking")
    while True:
        choice = input("Enter your choice (1 or 2)\n")
        if choice == '1':
            score += 10
            ask()
            break
        elif choice == '2':
            continue_explore()
            break
        else:
            print("please try again")


def cave():
    global score
    pause("You start entering the cave and find a monster")
    pause("The monster sees you and starts attacking")
    pause("You remember the staff that the wizard gave you")
    pause("1. Attack the monster\n2. Run away")
    while True:
        choice = input("Enter Your choice (1 or 2)\n")
        if choice == '1':
            score += 10
            attack()
            break
        elif choice == '2':
            run_away()
            break
        else:
            print("Please try again")


def attack():
    global score
    abilities = ['kill', 'attack', 'fire' 'hide your self']
    wand = random.choice(abilities)
    print("You start waving your staff to see")
    pause("what abilities it will grant you")
    if wand == 'kill':
        pause("Your ability is..." + wand + " is good")
        pause("You can now kill the monster")
        pause("But you need to hit it five consecutive times")
        print("1. Keep hitting\n2. Run away")
        while True:
            choice = input("Enter your choice (1 or 2)\n")
            if choice == '1':
                score += 10
                keep()
                break
            elif choice == '2':
                run_away()
                break
            else:
                print("Please try again")
    elif wand == 'attack':
        pause("Your ability is..." + wand + " is good")
        pause("You can now attack the monster")
        pause("But you need to hit it five consecutive times")
        print("1. Keep hitting\n2. Run away")
        while True:
            choice = input("Enter your choice (1 or 2)\n")
            if choice == '1':
                score += 10
                keep()
                break
            elif choice == '2':
                run_away()
                break
            else:
                print("Please try again")
    elif wand == 'fire':
        pause("Your ability is..." + wand + " is good")
        pause("You can now fire the monster")
        pause("But you need to hit it five consecutive times")
        print("1. Keep hitting\n2. Run away")
        while True:
            choice = input("Enter your choice (1 or 2)\n")
            if choice == '1':
                score += 10
                keep()
                break
            elif choice == '2':
                run_away()
                break
            else:
                print("Please try again")
    elif wand == 'hide your self':
        pause("Your ability is..." + wand + " is good")
        pause("You hide from the monster.")
        pause("But you need to hit it five consecutive times")
        print("1. Keep hitting\n2. Run away")
        while True:
            choice = input("Enter your choice (1 or 2)\n")
            if choice == '1':
                score += 10
                keep()
                break
            elif choice == '2':
                run_away()
                break
            else:
                print("Please try again")
    else:
        pause("Oh no, you don't have any abilities. You need to run away")
        run_away()


def keep():
    global score
    pause("You kept hitting and eventually won.")
    print("1. Do you want to stay in the cave?")
    pause("2. Leave the cave and continue exploring")
    while True:
        choice = input("Enter your choice (1 or 2):\n")
        if choice == '1':
            score += 10
            stay()
            break
        elif choice == '2':
            score += 5
            continue_explore()
            break
        else:
            print("Please try agin")


def stay():
    global score
    pause("Congratulations to you.")
    pause("You now have a shelter")
    pause("Your score now equal " + str(score))
    pause("But to win, your points must equal 100.")
    pause("Otherwise, you won't win")
    pause("To win, you must solve that riddle")
    print("How many months have 28 days?")
    while True:
        answer = input("Enter your answer (1, 2, 3, 4, ......, or 12):\n")
        if answer == '12':
            pause("Congratulations to you")
            score = 100
            pause("Your score is equal " + str(score))
            pause("You are win")
            print("You want play again (1 'for yes' or 2 'for no')")
            while True:
                choice = input("Enter your choice: \n")
                if choice == '1':
                    pause("ok")
                    pause("\n\nStart game now\n\n")
                    score = 0
                    start_game()
                    break
                if choice == '2':
                    pause("Thank you for played this game")
                    print("bye bye")
                    break
                else:
                    print("plase try again")
            break
        else:
            print("Due to your incorrect answer")
            pause(",your score is now less than 100")
            pause("Your score is equal " + str(score))
            pause("So you have lost")
            print("You want play again (1 'for yes' or 2 'for no')")
            while True:
                choice
                if choice == '1':
                    pause("ok")
                    pause("\n\nStart game now\n\n")
                    score = 0
                    start_game()
                    break
                elif choice == '2':
                    pause("Thank you for played this game")
                    print("bye bye")
                    break
                else:
                    print("plase try again")
            break


def continue_explore():
    global score
    pause("You begin to continue exploring the forest.")
    pause("You find a merchant's house selling some maps")
    print("You start asking about how to get out of the forest")
    pause("and if he has a map for that or not.")
    print("When you start negotiating with the merchant for the map,")
    print("he informs you that he's willing to provide the map")
    pause("but in exchange for your magical staff")
    pause("Do you accept or not? (1 'for yes' or 2 'for no)")
    while True:
        choice = input("Enter your choice: \n")
        if choice == '1':
            pause("You gave the merchant your staff and took the map.")
            print("You start walking and exit the forest,meeting your friends")
            pause("With that, you have succeeded.")
            pause("Your score now equal " + str(score))
            pause("But to win, your points must equal 100.")
            pause("Otherwise, you won't win")
            pause("To win, you must solve that riddle")
            print("How many months have 28 days?")
            while True:
                answer = input("Enter your answer (1, 2, 3, 4,.....,or 12):\n")
                if answer == '12':
                    pause("Congratulations to you")
                    score = 100
                    pause("Your score is equal " + str(score))
                    pause("You are win")
                    print("You want play again (1 'for yes' or 2 'for no')")
                    while True:
                        choice = input("Enter your choice: \n")
                        if choice == '1':
                            pause("ok")
                            pause("\n\nStart game now\n\n")
                            score = 0
                            start_game()
                            break
                        if choice == '2':
                            pause("Thank you for played this game")
                            print("bye bye")
                            break
                        else:
                            print("plase try again")
                    break
                else:
                    print("Due to your incorrect answer,")
                    pause("your score is now less than 100.")
                    pause("Your score is equal " + str(score))
                    pause("So you have lost")
                    print("You want play again (1 'for yes' or 2 'for no')")
                    while True:
                        choice
                        if choice == '1':
                            pause("ok")
                            pause("\n\nStart game now\n\n")
                            score = 0
                            start_game()
                            break
                        elif choice == '2':
                            pause("Thank you for played this game")
                            print("bye bye")
                            break
                        else:
                            print("plase try again")
                    break
            break
        elif choice == '2':
            pause("You refused the deal")
            pause("You start walking and hear the sound of a monster.")
            run_away()
            break


start_game()
