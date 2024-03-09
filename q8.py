#function return value

value=24*60
unit="min"
def unit_value(days,comment):
    return f"{days} days are {days * value} in {unit}.\n{comment}"
result=unit_value(20,"good")
print(result)    


usr_input=int(input("enter the value which you want to convert into min"))
print(usr_input)
value=24*60
unit="min"
def unit_value(days,comment):
    return f"{days}days are in {days * value} {unit}.\n{comment}"
val=unit_value(usr_input,"good")
print(val)
