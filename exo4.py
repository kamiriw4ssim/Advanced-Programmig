try: 
    age1= int(input("Please type in the age of the first person: "))
    age2 = int(input("Please type in the age of the second person: "))
except ValueError:
    print("Input must be an integer")
    exit()
if(age1 > age2) : print(f"The older age is: {age1}")
elif (age1 < age2):  print(f"The older age is {age2}")
else : print("Both people are the same age!") 