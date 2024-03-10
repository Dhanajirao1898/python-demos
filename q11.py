value=24*60
unit="min"
def unit_value(days,comment):
    if(days>0):
        return f"{days} days are {days * value} {unit}.\n{comment}"
    elif(days==0):
        return "there is no use of 0"
    else:
        return "kindly provide positive value"
def validate_execute():
    if input_value.isdigit():
        input_value_number=int(input_value)
        val=unit_value(input_value_number,"good")
        print(val)
    else:
        print("dont ruin")
       

        
input_value=input("print the value which you want to convert into min")  
print(input_value)              
validate_execute() 