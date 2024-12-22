from statistics import mean, median

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def save_to_file(current_list, sorted_list, stats):
    try:
        with open('number_lists.txt', 'w') as file:
            file.write("Current List: " + str(current_list) + "\n")
            file.write("Sorted (Ascending): " + str(sorted_list) + "\n")
            file.write("Sorted (Descending): " + str(sorted_list[::-1]) + "\n")
            file.write("\nStatistics:\n")
            for stat_name, stat_value in stats.items():
                file.write(f"{stat_name}: {stat_value}\n")
        print("\nList saved to 'number_lists.txt'")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_from_file():
    try:
        with open('number_lists.txt', 'r') as file:
            first_line = file.readline()
            # Extract numbers from the "Current List: [...]" format
            numbers_str = first_line.split(":")[1].strip()
            numbers = eval(numbers_str)  # Convert string representation to list
            return numbers
    except FileNotFoundError:
        print("No existing file found. Starting with empty list.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

def calculate_stats(numbers):
    if not numbers:
        return {"Mean": "N/A", "Median": "N/A"}
    return {
        "Mean": f"{mean(numbers):.2f}",
        "Median": f"{median(numbers):.2f}"
    }

def main():
    print("Sorted List Builder")
    print("Enter 0 to stop, 's' to save, 'l' to load existing list")
    
    user_list = []
    
    while True:
        user_input = input("\nEnter a number: ")
        
        # Check for special commands
        if user_input.lower() == 's':
            if user_list:
                stats = calculate_stats(user_list)
                save_to_file(user_list, sorted(user_list), stats)
            else:
                print("List is empty. Nothing to save.")
            continue
            
        if user_input.lower() == 'l':
            loaded_list = load_from_file()
            if loaded_list:
                user_list.extend(loaded_list)
                print(f"Loaded list: {loaded_list}")
            continue
            
        # Convert input to number
        try:
            number = float(user_input)
        except ValueError:
            print("Please enter a valid number, 's' to save, or 'l' to load.")
            continue
            
        # Check for exit condition
        if number == 0:
            break
            
        # Add number to list
        user_list.append(number)
        
        # Display lists
        print("\nCurrent List:", user_list)
        print("Sorted (Ascending):", sorted(user_list))
        print("Sorted (Descending):", sorted(user_list, reverse=True))
        
        # Display statistics
        stats = calculate_stats(user_list)
        print("\nStatistics:")
        for stat_name, stat_value in stats.items():
            print(f"{stat_name}: {stat_value}")

    # Final display if list is not empty
    if user_list:
        print("\nFinal Results:")
        print("Current List:", user_list)
        print("Sorted (Ascending):", sorted(user_list))
        print("Sorted (Descending):", sorted(user_list, reverse=True))
        
        stats = calculate_stats(user_list)
        print("\nFinal Statistics:")
        for stat_name, stat_value in stats.items():
            print(f"{stat_name}: {stat_value}")
        
        save_prompt = input("\nWould you like to save these results? (y/n): ")
        if save_prompt.lower().startswith('y'):
            save_to_file(user_list, sorted(user_list), stats)

if __name__ == "__main__":
    main()