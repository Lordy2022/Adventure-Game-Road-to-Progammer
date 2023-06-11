def main():
    name = input("Type your name: ")
    while not name.strip():  # Check if the name is empty or contains only whitespace
        print("Please enter a valid name.")
        name = input("Type your name: ")
    print("Welcome, {}! You have arrived in this world, congratulations!".format(name))

    answer = input("What do you want to do? (I want adventure/I want a mediocre existence): ").lower()

    if answer == "i want a mediocre existence":
        mediocre_existence(name)
    elif answer == "i want adventure":
        adventure(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")

    print("Thank you for playing", name)


def mediocre_existence(name):
    answer = input("Interesting choice... You arrive on your first day of school, and the teacher asks what everyone would like to be when they grow up? (I want to be a Traffic Warden/I want to be a Portable Toilet Cleaner): ").lower()

    if answer == "i want to be a traffic warden":
        print("You blink, and all of a sudden 60 years have passed you by. You come to the realization that you will die mediocre. Thankfully for us both, time is precious, and I have no time to waste - GAME OVER.")
    elif answer == "i want to be a portable toilet cleaner":
        print("You blink, and all of a sudden 30 years have passed you by... While doing work on a building site (during a particularly cold and icy winter's morning), you slip and fall into the builders' waste. Congratulations, you died mediocre! - GAME OVER.")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")


def adventure(name):
    answer = input("Do you know, once you start, there's no going back? (I know./Actually, mediocre sounds good...): ").lower()

    if answer == "actually, mediocre sounds good...":
        print("If you deserve it, the universe will serve it! Congratulations, you died mediocre! - GAME OVER.")
    elif answer == "i know.":
        answer = input("This means total commitment. Once you begin the path, there is no leaving the path. Are you sure you're ready for that? I mean really ready? (I-I guess so./Can we forget I asked?): ").lower()

        if answer == "can we forget i asked?":
            print("Met with mild adversity you crumbled, you are no Hal nor Hercules... you lose! - GAME OVER")
        elif answer == "i-i guess so.":
            start_adventure(name)
        else:
            print("You aren't taking this world seriously enough. You lose - GAME OVER")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")


def start_adventure(name):
    answer = input("Neat! We'll start from tomorrow, your first day of school. Your teacher asks what everyone would like to be when they grow up? (I want to work as a Fireman/I LOVE Lego, so I want to build things): ").lower()

    if answer == "i want to work as a fireman":
        print("You become a brave firefighter, saving lives and making a difference in your community. Congratulations, what an amazing life... but not quite what you were looking for in your heart of hearts. You lose - GAME OVER")
    elif answer == "i love lego, so i want to build things":
        on_the_right_path(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")


def on_the_right_path(name):
    answer = input("""You spend most of your childhood building amazing creations with Lego (fantastic move, what a great childhood). 
Before you know it, you're about to start your first day of secondary school (time flies). What are you having for breakfast, before the big day? (I fancy some pancakes/Maybe a handful of some dried almonds?): """).lower()

    if answer == "maybe some dried almonds?":
        print("You choke on the almonds, and die. You lose - GAME OVER")
    elif answer == "i fancy some pancakes":
        fantastic_breakfast(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")


def fantastic_breakfast(name):
    answer = input("""The perfect start to the day, you have an amazing first day of school, in your first class you meet your new best friend, Hal. You bond over your love Lego, and the two of you become inseparable.
    You spend the next year building amazing creations together, however as you get older you decide you need to grow up and stop playing with Lego. I suppose this was always going to happen, but it's still sad. 
    As with most burgeoning young teenagers, you dip your feet in the dating scene, you and Hal spend a less time together, and you begin to drift apart. This is also sad, Hal was a great chap and did a great job of keeping you on the right path.
    It's now time to pick which subjects you want to study for your GCSEs. You're not sure what you want to do, but you know deep down you still love to build things. For your final option, you are stuck beteween either taking...(Food Technology/Computer Science): """).lower()

    if answer == "i want to go to the park":
        print("You go to the park, and have a great time. You lose - GAME OVER")
    elif answer == "i want to go to school":
        print("You go to school, and have a great time. You lose - GAME OVER")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")





if __name__ == '__main__':
    main()

