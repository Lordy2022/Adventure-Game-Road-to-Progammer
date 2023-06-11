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

    print("Thank you for trying", name)


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
        print("You become a brave firefighter, saving lives and making a difference in your community. Congratulations, you WIN!")
    elif answer == "i love lego, so i want to build things":
        print("You dedicate your life to creating amazing Lego structures. You become a renowned Lego designer, traveling the world and inspiring others with your creations. Congratulations, you WIN!")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")


if __name__ == '__main__':
    main()

