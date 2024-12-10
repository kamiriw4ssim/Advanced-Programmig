try:
        temperature = int(input("Please type in the temperature: "))
        if temperature < 0:
            print("It's freezing!")
        if temperature < 10:
            print("It's cold!")
        if temperature < 20:
            print("It's cool!")
        print("Stay safe!")
except ValueError:
        print("Invalid input. Please enter an integer value for temperature.")