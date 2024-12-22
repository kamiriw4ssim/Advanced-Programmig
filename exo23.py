while True:
    try:
        
        N = int(input("Please enter a positive integer: "))
        if N <= 0:
            print("Please enter a positive number.")
            continue    
        for i in range(-N, 0):
            print(i)    
        for i in range(1, N + 1):
            print(i)    
        break  
    except ValueError:
        print("Invalid input. Please enter a valid integer.")