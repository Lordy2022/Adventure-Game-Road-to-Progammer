def main():
    welcome()
    questionOne()
    
    
    
def welcome():
    while True:
        try:
            name = input("What is your name?: ")
            if name.strip():  # Check if name is not empty or only whitespace
                break
            else:
                print("Please enter a valid name.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return
    print("Welcome, {}! You have arrived in this world, congratulations!".format(name))


def questionOne():
    answer = input("What do you want to do? (I want adventure/I want a mediocre existence): ").lower()

    if answer == "i want adventure":
        questionTwo()
    elif answer == "i want a mediocre existence":
        print("You will die mediocre, thankfully for us both time is precious and I have no time to waste - game over.")
    else:
        print("You aren't taking this world seriously enough. You lose")
        
        
       
def questionTwo():
    answer = input("Do you know, once you start there's no going back? (I know./Actually, mediocre sounds good...): ").lower()
    
    if answer == "I know.":
        questionThree()
    elif answer == "actually, mediocre sounds good...":
        print("You will die mediocre, thankfully for us both time is precious and I have no time to waste - game over.")
    else:
        print("You aren't taking this world seriously enough. You lose")


def questionThree():
    answer = input("This means total commitment. Once you begin the path, there is no leaving the path. Are you sure you're ready for that? I mean really ready? (I-I guess so./Can we forget I asked?): ").lower()
    
    if answer == "I-I guess so.":
        questionFour()
    elif answer == "Can we forget I asked?":
        print("Met with mild adversity you crumbled, you are no Hal nor Hercules... you lose!")
    else:
        print("You aren't taking this world seriously enough. You lose")

if __name__ == "__main__":
    main()
