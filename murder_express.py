import time

def print_slow(text):
    """Prints text slowly to enhance immersion."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print("\n")

def start_game():
    print_slow("Welcome to 'Murder Express'!")
    print_slow("You are a detective aboard a luxurious train where a shocking murder has occurred...")
    print_slow("Your task is to find the truth and catch the killer.")

    # First part: Discovering the murder
    print("\nThe conductor approaches you and informs you that a passenger has been found dead in their cabin. You prepare to:")
    print("1. Immediately head to the crime scene")
    print("2. Ask the conductor for more details")
    choice1 = input("> ")
    
    if choice1 == "1":
        scene_crime()
    elif choice1 == "2":
        ask_details()
    else:
        print_slow("Invalid choice, please try again.")
        start_game()

def scene_crime():
    print_slow("\nYou arrive at the crime scene. The victim is a wealthy businessman, apparently poisoned.")
    print_slow("In the room, you notice several suspicious items:")
    print("1. A torn letter")
    print("2. A small silver bottle")
    print("3. A list of passengers")
    
    choice2 = input("What do you want to examine first? > ")
    if choice2 == "1":
        print_slow("\nThe letter appears to be part of a will, but it's incomplete. Someone tried to destroy it.")
        interrogate_suspects()
    elif choice2 == "2":
        print_slow("\nThe liquid in the bottle is confirmed to be a deadly poison.")
        interrogate_suspects()
    elif choice2 == "3":
        print_slow("\nThe passenger list has some interesting symbols marked next to certain names. It seems some passengers had a close relationship with the victim.")
        interrogate_suspects()
    else:
        print_slow("Invalid choice, please try again.")
        scene_crime()

def ask_details():
    print_slow("\nThe conductor tells you that the victim had argued with a few passengers the previous night.")
    print_slow("He also mentioned some strange noises on the train that might be a clue.")
    scene_crime()

def interrogate_suspects():
    print_slow("\nAfter your initial investigation, you decide to interrogate three suspects:")
    print("1. A young waiter who seems nervous")
    print("2. A wealthy woman who appears to have been close to the victim")
    print("3. A businessman who had financial disputes with the victim")
    
    choice3 = input("Who would you like to interrogate? > ")
    if choice3 == "1":
        print_slow("\nThe waiter admits seeing someone enter the victim's cabin last night, but refuses to say more.")
        final_decision()
    elif choice3 == "2":
        print_slow("\nThe woman gets agitated and insists she is innocent, providing some strong alibis.")
        final_decision()
    elif choice3 == "3":
        print_slow("\nThe businessman remains cold and denies having any involvement, though he had arguments with the victim.")
        final_decision()
    else:
        print_slow("Invalid choice, please try again.")
        interrogate_suspects()

def final_decision():
    print_slow("\nAfter gathering enough evidence, you think it's time to make a decision.")
    print("It's time to identify the killer.")
    print("1. Accuse the waiter")
    print("2. Accuse the woman")
    print("3. Accuse the businessman")
    
    choice4 = input("Who do you think did it? > ")
    if choice4 == "1":
        print_slow("\nYou accuse the waiter, and with enough evidence, it is confirmed that he poisoned the victim. The case is solved!")
    elif choice4 == "2":
        print_slow("\nYou accuse the woman, but lack sufficient evidence, and she is released. The case remains unsolved.")
    elif choice4 == "3":
        print_slow("\nYou accuse the businessman, but it turns out he was innocent. The case is still open.")
    else:
        print_slow("Invalid choice, please try again.")
        final_decision()

# Start the game
start_game()