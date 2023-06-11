def main():
    name = input("Type your name: ")

    print("Welcome, {}! You have arrived in this world, congratulations!".format(name))

    answer = input("What do you want to do? (I want adventure/I want a mediocre existence): ").lower()

    if answer == "i want a mediocre existence":
        answer = input("Interesting choice... You arrive on your first day of school, the teacher asks what everyone would like to be when they grow up? (I want to be a Traffic Warden/I want to be a Portable Toilet Cleaner): ").lower()

        if answer == "i want to be a traffic warden":
            print("You blink and all of a sudden 60 years have passed you by, you come to the realization that you will die mediocre. Thankfully for us both, time is precious and I have no time to waste - GAME OVER.")
        elif answer == "i want to be a portable toilet cleaner":
            print("You blink and all of a sudden 30 years have passed you by... Whilst doing work on a building site (during a particularly cold and icy winter's morning), you slip and fall into the builders' waste. Congratulations, you died mediocre! - GAME OVER.")
        else:
            print("You aren't taking this world seriously enough. You lose - GAME OVER")

    elif answer == "i want adventure":
        answer = input("Do you know, once you start there's no going back? (I know./Actually, mediocre sounds good...): ").lower()

        if answer == "actually, mediocre sounds good...":
            print("If you deserve it, the universe will serve it! Congratulations, you died mediocre! - GAME OVER.")
        elif answer == "i know.":
            answer = input("This means total commitment. Once you begin the path, there is no leaving the path. Are you sure you're ready for that? I mean really ready? (I-I guess so./Can we forget I asked?): ").lower()

            if answer == "i-i guess so.":
                print("You talk to the stranger and they give you gold. You WIN!")
            elif answer == "can we forget i asked?":
                print("Met with mild adversity you crumbled, you are no Hal nor Hercules... you lose! - GAME OVER")
            else:
                print("You aren't taking this world seriously enough. You lose - GAME OVER")
        else:
            print("You aren't taking this world seriously enough. You lose - GAME OVER")

    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER")

    print("Thank you for trying", name)

if __name__ == '__main__':
    main()