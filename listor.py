#lista på saker på coop att köpa
menu = 0
cooplista = []
while True:
    try:
        menu = int(input("Welcome to the list\n Press 1 to print out the list\n Press 2 to add something to the list\n Press 3 to clear the list\n Press 4 to exit\n"))
    except: #1 print list, 2 add to list, 3 delete list
        print("You can only use the numbers 1-4")
    if menu == 1:
        print("Your cooplist:\n", cooplista)
    elif menu == 2:
        cooplista.append(input("Write here what to add to the list\n"))
    elif menu == 3:
        cooplista.clear()
    elif menu == 4:
        break