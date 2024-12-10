try :
    nbperson = int(input("How many people need a taxi? "))
    nbfittaxi = int(input("How many people fit in a taxi? "))
    if (nbperson % nbfittaxi ==0):
        nbtaxi=nbperson // nbfittaxi
    else  :  
        nbtaxi=nbperson // nbfittaxi +1

    
except ValueError: 
    print("The input must be an integer")
    exit()
print(f"Number of taxis needed is {nbtaxi} ")