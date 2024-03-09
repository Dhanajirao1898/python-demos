usr_input=int(input("enter days value which you want to convert into min "))
print(usr_input)
value=24*60
unit="min"
def unit_value(usr_input,comment):
    print(f"{usr_input} days are {usr_input*value} in {unit}")
    print(comment)
unit_value(usr_input,"awesome")    