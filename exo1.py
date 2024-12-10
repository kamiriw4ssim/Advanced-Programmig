name = input("Please enter your name: ")
if (name == "VIP"):
    print("Enjoy the show for free !")
else :
    TICKET_PRICE = 15.50
    try:
        nb_tickets = int(input("How many tickets would you like to buy? "))
    except ValueError:
        print("Number of tickets must be an integer")
        exit()
    if(nb_tickets == 0) :
        print("You can't attend the show unless you buy at least one ticket!")
    else :
        print(f"The total cost is {TICKET_PRICE * nb_tickets}")
        print("Enjoy your tickets!")