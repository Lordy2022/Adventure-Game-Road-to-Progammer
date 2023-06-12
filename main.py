def main():
    name = input("Type your name: ")
    while not name.strip():  # Check if the name is empty or contains only whitespace
        print("Please enter a valid name.")
        name = input("Type your name: ")
    print("Welcome, {}! You have arrived in this world, congratulations!".format(name))
    print("You have two choices: you can either have a mediocre existence, or you can have an adventure - but you can't go through this world not knowing how to spell...")


    answer = input("What do you want to do? (I want adventure/I want a mediocre existence): ").lower()

    if answer == "i want a mediocre existence":
        mediocre_existence(name)
    elif answer == "i want adventure":
        adventure(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")

    print("Thank you for playing", name)


def mediocre_existence(name):
    answer = input("Interesting choice... You arrive on your first day of school, and the teacher asks what everyone would like to be when they grow up? (I want to be a Traffic Warden/I want to be a Portable Toilet Cleaner): ").lower()

    if answer == "i want to be a traffic warden":
        print("You blink, and all of a sudden 60 years have passed you by. You come to the realization that you will die mediocre. Thankfully for us both, time is precious, and I have no time to waste - GAME OVER.")
    elif answer == "i want to be a portable toilet cleaner":
        print("You blink, and all of a sudden 30 years have passed you by... While doing work on a building site (during a particularly cold and icy winter's morning), you slip and fall into the builders' waste. Congratulations, you died mediocre! - GAME OVER.")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def adventure(name):
    answer = input("Do you know, once you start, there's no going back? (I know./Actually, mediocre sounds good...): ").lower()

    if answer == "actually, mediocre sounds good...":
        print("If you deserve it, the universe will serve it! Congratulations, you died mediocre! - GAME OVER.")
    elif answer == "i know.":
        answer = input("This means total commitment. Once you begin the path, there is no leaving the path. Are you sure you're ready for that? I mean really ready? (I-I guess so./Can we forget I asked?): ").lower()

        if answer == "can we forget i asked?":
            print("Met with mild adversity you crumbled, you are no Hal nor Hercules... you lose! - GAME OVER.")
        elif answer == "i-i guess so.":
            start_adventure(name)
        else:
            print("You aren't taking this world seriously enough. You lose - GAME OVER.")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def start_adventure(name):
    answer = input("Neat! We'll start from tomorrow, your first day of school. Your teacher asks what everyone would like to be when they grow up? (I want to work as a Fireman/I LOVE Lego, so I want to build things): ").lower()

    if answer == "i want to work as a fireman":
        print("You become a brave firefighter, saving lives and making a difference in your community. Congratulations, what an amazing life... but not quite what you were looking for in your heart of hearts. You lose - GAME OVER.")
    elif answer == "i love lego, so i want to build things":
        on_the_right_path(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def on_the_right_path(name):
    answer = input("""You spend most of your childhood building amazing creations with Lego (fantastic move, what a great childhood). 
Before you know it, you're about to start your first day of secondary school (time flies). What are you having for breakfast, before the big day? (I fancy some pancakes/Maybe a handful of some dried almonds?): """).lower()

    if answer == "maybe some dried almonds?":
        print("You choke on the almonds, and die. You lose - GAME OVER.")
    elif answer == "i fancy some pancakes":
        fantastic_breakfast(name)
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def fantastic_breakfast(name):
    answer = input("""The perfect start to the day, you have an amazing first day of school, in your first class you meet your new best friend, Hal. You bond over your love Lego, and the two of you become inseparable.

You spend the next year building amazing creations together, however as you get older you decide you need to grow up and stop playing with Lego. I suppose this was always going to happen, but it's still sad. 

As with most burgeoning young teenagers, you dip your feet in the dating scene, you and Hal spend a less time together, and you begin to drift apart. This is also sad, Hal was a great chap and did a great job of keeping you on the right path.
Before you know it, a few hormone filled years have passed... It's now time to pick which subjects you want to study for your GCSEs.

You're not sure what you want to do, but you know deep down you still love to build things. For your final option, you are stuck between either taking...(Food Technology/Computer Science): """).lower()

    if answer == "computer science":
        computer_science(name)
    elif answer == "food technology":
        print("""You pick Food Technology, where you find a new passion for the science around creating amazing food (you also rekindle your love for eating pancakes and boy, do you LOVE eating pancakes).
You spend the next few years eating pancakes and other food... A LOT of food.
The good news is, you eventually become a professional eater and are known around the world for your endeavours. The bad news is, you die of a heart attack at the age of 35.
Your old friend Hal does turn up to the funeral to show his condolences though, I always knew he was a good guy... You lose - GAME OVER.""")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def computer_science(name):
     answer= input("""You pick Computer Science, although you have never really read much into this idea. You didn't know exactly what this entailed, you just figured that it meant you would be building things with code.
You were inspired to pick this choice after being addicted to Facebook during your teen years and watching The Social Network movie (ahh, aren't teenagers easily influenced). Time to go home and tell your parents the good news.

You tell your parents you want to study Computer Science and they are over the Moon, they always knew you were a smart kid, your older brother however is not so impressed. He gives you a wedgie and tells you that you need to go out and get a life.
So that is exactly what you do, you go out and get a life. You spend the next few years at school going to parties but never really studying. You scrape through your GCSEs and decide to go to Sixth Form, but you aren't sure if you want to study Computer Science anymore.

So, you decide to take a walk to reflect on your choice. Where are you going? (I'm going to the park/No idea, I just need to leave the house): """).lower()
     if answer == "i'm going to the park":
        print("""You go to the same boring park that you always go to, you sit on the same boring bench that you always sit on, and you think about the same boring things that you always think about. Maybe you should do a nice boring course, Mathematics sounds good? 
You spend the rest of your time at college surrounded by numbers and it drives you insane. You muster the strength to get into your final year, where you have a new teacher, Mr Andrews. 

His monotone voice and boring teaching style, causes you to die from boredom. You lose - GAME OVER.""")
     elif answer == "no idea, i just need to leave the house":
        leaving_the_house_with_no_plan_adventure(name)
     else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")


def leaving_the_house_with_no_plan_adventure(name):
    answer = input("""Fate rewards you for leaving the house with no plan, for the first time in a while, you almost feel a sense of adventure. You walk around the corner from your house and you never guess who you bump into.. Hal! 
You two haven't seen each other in years, but you pick up right where you left off. You tell him about your dilemma and he tells you that he is studying computer science at sixth form and that you should join him.
He gives you an short pep talk about Hercules and the crossroads, and you feel inspired to take the road less travelled. You and Hal spend the next two years studying together, and you both get into the same university to study Computer Science.

You can't help but remember what Hal said to you a couple of years ago about Hercules and taking the road less travelled. You decide to take a different path, you never needed to education system to teach you how to build things, you already knew how to do that.
You have a choice to make, stay in your home town, or move to Nottingham with Hal? (I'm going to stay in my home town/I'm going to move to Nottingham): """).lower()
    if answer == "i'm going to stay in my home town":
        print("""You stay in your home town, you get a job at the local supermarket (just while you find your feet of course). But you never do find your feet, infact you start to feel comfortable...
Maybe a little too comfortable! You spend the rest of your life stacking shelves. You lose - GAME OVER.""")
    elif answer == "i'm going to move to nottingham":
        print("""You move to Nottingham with Hal, you get a job at a local university in the Digital Technologies department. You spend your extra hours learning how to code independently, until you managed to find yourself on an amazing course called Code In Place.
This course is ran by Stanford University Profesors and you learn how to code in Python. You spend the next few weeks learning how to code, and you build some amazing things. You even build a game, where you can choose your own adventure.
Shortly after you finish this course, you land your dream job as a Software Engineer. Sometimes, life really is about taking the road less travelled. You win - GAME OVER (amazing work conrgatulations!))""")
    else:
        print("You aren't taking this world seriously enough. You lose - GAME OVER.")
        

if __name__ == '__main__':
    main()

