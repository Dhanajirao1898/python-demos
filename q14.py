

def unit_value(days,coversion_unit):
    if coversion_unit=="hours":
        return f"{days} days are {days * 24} hours"
    elif coversion_unit=="min":
        return f"{days} days are {days *24*60} min"
    else:
        return "unsupported unit"
    
def validate_exec(value_and_unit_dict):
    try:
        user_val_number=int(value_and_unit_dict["days"])
        if(user_val_number>0):
            val=unit_value(user_val_number,value_and_unit_dict["unit"])
            print(val)
        elif(user_val_number==0):
            print("dont ruin my program")
        else:
            print("dont ruin code") 
    except ValueError:
        print("dont ruin my code")

user_value=""        
while user_value != "exit":
    user_value=input("enter value which want to convert into min ")
    value_and_unit=user_value.split(":")
    print(value_and_unit)
    value_and_unit_dict={"days": value_and_unit[0],"unit":value_and_unit[1]}
    print(value_and_unit_dict)
    validate_exec()  


                           
