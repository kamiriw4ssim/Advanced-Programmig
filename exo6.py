

try:
    amount = float(input("Enter the amount in dinars: "))
    dinars = int(amount)
    centimes = int(round((amount - dinars) * 100))
    print(f"Dinars: {dinars}, Centimes: {centimes}")
except ValueError:
    print("Invalid input. Please enter a valid amount.")
