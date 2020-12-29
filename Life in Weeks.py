
age = input("What is your current age?")


months = int(age)  * 12
weeks = int(age) * 52
days = int(age) * 365

pending_months = 1080 - months
pending_weeks = 4680 - weeks
pending_days = 32850 - days

print(f"You have {pending_days} days, {pending_weeks} weeks, {pending_months} months left")
