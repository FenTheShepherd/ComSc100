gold = 10

def start():
    global gold
    print("Welcome to Clover's Adventure!")
    print("Clover is lost in the marketplace and needs to find her family.")
    print("Current Gold: " + str(gold))
    choice = input("Who should she look for first? (Dyvia/Kirb/Parents): ").strip().lower()
    
    if choice == "dyvia":
        dyvia_path()
    elif choice == "kirb":
        kirb_path()
    elif choice == "parents":
        parents_path()
    else:
        print("Invalid choice. Try again.")
        start()

def dyvia_path():
    global gold
    print("Clover finds Dyvia shopping for a new bow.")
    choice = input("Should she buy Dyvia the expensive bow with their shared gold or convince her to get food instead? (buy/food/back): ").strip().lower()
    if choice == "buy":
        gold = gold - 5
        print("Dyvia happily buys the new bow and thanks Clover. They continue shopping together, Dyvia's treat.")
    elif choice == "food":
        gold = gold + 3
        print("Dyvia agrees and they enjoy a delicious hearty meal together. Clover earns some gold as a thank you!")
    elif choice == "back":
        print("Clover decides to return to town to look for her parents and Kirb.")
        start()
    else:
        print("Invalid choice. Try again.")
        dyvia_path()
    restart()

def kirb_path():
    global gold
    print("Clover finds Kirb looking at staffs in an apothecary shop.")
    choice = input("Should Kirb buy the healing staff or the cool-looking staff? (healing/cool/back): ").strip().lower()
    
    if choice == "healing":
        print("Kirb buys the healing staff with Clover's input, feeling satisfied with a practical choice.")
        gold = gold - 2
    elif choice == "cool":
        print("Kirb hesitates but buys the cool staff for Clover's sake, hoping it has some hidden power.")
        gold = gold - 3
    elif choice == "back":
        print("Clover decides to return to town to look for her parents and Dyvia.")
        start()
    else:
        print("Invalid choice. Try again.")
        kirb_path()
    restart()

def parents_path():
    global gold
    print("Clover finds her parents, Fen and Genny, outside of town enjoying their time together.")
    choice = input("Should she spend time with them or go back to find her other siblings? (stay/back): ").strip().lower()
    
    if choice == "stay":
        gold = gold + 5
        print("Clover enjoys a peaceful time with her parents, cherishing the moment. Dyvia and Kirb eventually unite, and the 5 of them enjoy the sunset together. Clover earns some gold as a gift!")
    elif choice == "back":
        print("Clover decides to return to town to look for Dyvia and Kirb.")
        start()
    else:
        print("Invalid choice. Try again.")
        parents_path()
    restart()

def restart():
    global gold
    choice = input("Want to try a different path? (yes/no): ").strip().lower()
    if choice == "yes":
        print("Gold before restarting: " + str(gold))
        start()
    elif choice == "no":
        print("Thanks for playing! Clover ends with " + str(gold) + " gold. Hope to see you again soon!")
    else:
        print("Invalid choice. You can't english lmao :3")

start()
