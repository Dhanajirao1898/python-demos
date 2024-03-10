from q16a import *    #validate_exec, user_input_message
import logging

logger=logging.getLogger("MAIN")
logger.error("error happened in the app")
"""user_input = ""
while user_input.lower() != "exit":
    user_input = input(user_input_message)
    if user_input.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    
    value_and_unit = user_input.split(":")
    if len(value_and_unit) == 2:
        value_and_unit_dict = {"days": value_and_unit[0], "unit": value_and_unit[1]}
        validate_exec(value_and_unit_dict)
    else:
        print("Please enter value and unit in the correct format (e.g., 2:hours).")"""
