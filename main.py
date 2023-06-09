def main():
    welcome()

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
    print("This is no trivial feat... adventure awaits! :)")

main()
