def fizz_buzz():
    try:
        entier = int(input("input:"))
        if entier % 3 == 0 and entier % 5 == 0:
            print("FizzBuzz")
        elif entier % 3 == 0:
            print("Fizz")
        elif entier % 5 == 0:
            print("Buzz")
        else:
            print("[no output]")
    except ValueError:
        print ("donner un nombre entier")

fizz_buzz()
