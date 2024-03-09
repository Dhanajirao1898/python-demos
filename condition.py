
value=24*60
unit="min"
def unit_value(days,comment):
    if(input_value>0):
        return f"{days} days in {days * value} in {unit}.\n {comment}"
    elif(input_value==0):
        return "what is the use of using 0"
    elif isinstance(input_value, float):
        return "Kindly provide an integer value."
    else:
        return "Kindly provide positive value"
    
try:
    input_value=int(input("enter value which you want to covert into min "))
    print(input_value)
    val=unit_value(input_value,"good")
    print(val)

except ValueError:
    print("Please enter a valid integer value.")