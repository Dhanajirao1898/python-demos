value=24*60
unit="min"
def unit_value(days,custom_msg):
    print(f"{days} days value {days * value} in {unit}")
    print(custom_msg)
def scope_check(days):
    my_scope="internal variable"
    print(unit)
    print(days)   
    print(my_scope)
scope_check(20)     