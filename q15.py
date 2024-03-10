def unit_value(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} hours"
    elif conversion_unit == "min":
        return f"{days} days are {days * 24 * 60} min"
    else:
        return "Unsupported unit"

def validate_exec(value_and_unit_dict):
    try:
        value_and_unit = int(value_and_unit_dict["days"])
        if value_and_unit > 0:
            val = unit_value(value_and_unit, value_and_unit_dict["unit"])
            print(val)
        elif value_and_unit == 0:
            print("No value for 0")
        else:
            print("You entered a negative number")
    except ValueError:
        print("Please enter a valid positive integer for days.")

user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter value and unit (e.g., 2:hours) to convert into min (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    
    value_and_unit = user_input.split(":")
    if len(value_and_unit) == 2:
        value_and_unit_dict = {"days": value_and_unit[0], "unit": value_and_unit[1]}
        validate_exec(value_and_unit_dict)
    else:
        print("Please enter value and unit in the correct format (e.g., 2:hours).")
