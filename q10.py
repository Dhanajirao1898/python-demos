value=24*60
unit="min"
def unit_value(days,comment):
    if(user_input_number>0):
        return f"{days} days mean{days*value} {unit}.\n{comment}"
    elif(user_input_number==0):
        return "no use of 0"
    else:
        return "kindly provide positive value"
    

user_input=input("enter number which u want into min ")
print(user_input)
if user_input.isdigit():
    user_input_number=int(user_input)
    val=unit_value(user_input_number,"good")
    print(val)
else:
    print("dont ruin my program")    