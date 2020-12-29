
age = input("What is your current age?")



pending_age = 90 - int(age)
pending_months = int(pending_age)  * 12
pending_weeks = int(pending_age) * 52
pending_days = int(pending_age) * 365


print(f"You have {pending_days} days, {pending_weeks} weeks, {pending_months} months left")
