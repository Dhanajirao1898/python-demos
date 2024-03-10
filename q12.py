
value=24*60
unit="min"
def unit_value(days):
    return f"{days} days are {days * value} {unit}"
    
def validate_execute():
    try:
        user_value_number=int(value_and_unit_dict["days"])
        if(user_value_number>0):
            val=unit_value(user_value_number,value_and_unit_dict["unit"])
            print(val)
        elif(user_value_number==0):
            print("dont ruin my code") 
        else:
            print("u entered -ve number")       
    except ValueError:
        print("dont ruin my code")


user_value=""        
while user_value != "exit":
    user_value=input("enter value which want to convert into min ")
    value_and_unit=user_value.split(":")
    print(value_and_unit)
    value_and_unit_dict={"days": value_and_unit[0],"unit":value_and_unit[1]}
    print(value_and_unit_dict)
    validate_execute()
    """list_of_days=user_value.split(",")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days in set(list_of_days):
        validate_execute()"""   

        


