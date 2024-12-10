def determine_faster_runner(runner1_name, runner1_time, runner2_name, runner2_time):
    if runner1_time < runner2_time:
        return runner1_name
    elif runner2_time < runner1_time:
        return runner2_name
    else:
        return "Both runners have the same time."


try:
    runner1_name = input("Enter the name of the first runner: ")
    runner1_time = float(input(f"Enter {runner1_name}'s time in seconds: "))
    runner2_name = input("Enter the name of the second runner: ")
    runner2_time = float(input(f"Enter {runner2_name}'s time in seconds: "))
    faster_runner = determine_faster_runner(runner1_name, runner1_time, runner2_name, runner2_time)
    print(f"The faster runner is: {faster_runner}")
except ValueError:
    print("Invalid input. Please enter valid times in seconds.")
