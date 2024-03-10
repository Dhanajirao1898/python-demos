from datetime import datetime

user_input=input("enter you goal with deadline seperated by colon\n")
input_list=user_input.split(":")
goal=input_list[0]
deadline=input_list[1]
deadline_date=datetime.strptime(deadline, "%d.%m.%Y")
today_date=datetime.today()

#calculate how many days from now till deadline
reamining_days=deadline_date-today_date
print(f"Dear user time remaining to your {goal} is {reamining_days.days}")

