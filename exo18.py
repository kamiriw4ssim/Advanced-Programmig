def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort list")
    print("6. Reverse list")
    print("7. Search for element")
    print("8. Save list to file")
    print("9. Load list from file")
    print("10. Quit")

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def save_to_file(numbers):
    try:
        with open('numbers.txt', 'w') as file:
            file.write(','.join(map(str, numbers)))
        print("List saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file():
    try:
        with open('numbers.txt', 'r') as file:
            content = file.read()
            return [int(x) for x in content.split(',')]
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def main():
    numbers = [1, 2, 3, 4, 5]
    
    while True:
        print("\nCurrent List:", numbers)
        display_menu()
        
        choice = get_integer_input("Choose an option: ")
        
        if choice == 1:  # Append
            value = get_integer_input("Enter value to append: ")
            numbers.append(value)
            
        elif choice == 2:  # Insert
            value = get_integer_input("Enter value to insert: ")
            while True:
                index = get_integer_input("Enter index position: ")
                try:
                    numbers.insert(index, value)
                    break
                except IndexError:
                    print(f"Invalid index. Please enter a value between 0 and {len(numbers)}")
                    
        elif choice == 3:  # Pop
            try:
                popped = numbers.pop()
                print(f"Popped value: {popped}")
            except IndexError:
                print("Cannot pop from empty list")
                
        elif choice == 4:  # Remove
            value = get_integer_input("Enter value to remove: ")
            try:
                numbers.remove(value)
            except ValueError:
                print(f"Value {value} not found in list")
                
        elif choice == 5:  # Sort
            numbers.sort()
            print("List sorted!")
            
        elif choice == 6:  # Reverse
            numbers.reverse()
            print("List reversed!")
            
        elif choice == 7:  # Search
            value = get_integer_input("Enter value to search: ")
            try:
                index = numbers.index(value)
                print(f"Value {value} found at index {index}")
            except ValueError:
                print(f"Value {value} not found in list")
                
        elif choice == 8:  # Save to file
            save_to_file(numbers)
            
        elif choice == 9:  # Load from file
            loaded_list = load_from_file()
            if loaded_list:
                numbers = loaded_list
                print("List loaded successfully!")
                
        elif choice == 10:  # Quit
            print("Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()