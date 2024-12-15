try:
    width = int(input("Width: "))
    Height = int(input("Height: "))
    for i in range(Height):
        print("#" * width)

except ValueError:
    print("donner un entier")
