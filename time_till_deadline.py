from datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon\n")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.today()

time_till = deadline_date - today_date

print(f' Dear user! The time remaining for your goal is: {time_till.days} days\n')

print(f' Dear user! The time remaining for your goal is: {int(time_till.total_seconds()/60/60)} hours\n')

print(f' Dear user! The time remaining for your goal is: {time_till.days} days\n')