numbers = [1,2,3,4,5]
while True:
    
    try:
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            break  
        new_value = int (input("Enter new value: "))
        if 0 <= index < len(numbers): 
            numbers[index] = new_value  
            print(numbers)  
        else:
            print("Invalid index! Please enter a valid index.")
    except ValueError:
        print("Invalid input! Please enter a valid integer for index.")
