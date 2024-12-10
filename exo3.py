


try:
    total_amount = float(input("Total amount: "))
    num_items = int(input("Number of items: "))
    day_of_week = input("Day of the week: ")
    day_of_week = day_of_week.lower()
    discount = 0

    if day_of_week in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        discount += 0.10
    elif day_of_week in ['saturday', 'sunday']:
        discount += 0.20
    else:
        print("Invalid day of the week.")
       

    if num_items > 5:
        discount += 0.05

    discounted_price = total_amount * (1 - discount)
    print (discounted_price)
    
except ValueError:
    print("Invalid input. Please enter numeric values for amount and number of items.")
