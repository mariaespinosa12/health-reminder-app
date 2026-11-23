# automation_engine.py

reminders_sent = ["Drink water at 9 AM", "Take medicine at 12 PM", "Drink water at 3 PM"]
missed_reminders= []
max_reminders_per_day = 5 

# Loop through reminders
for reminder in reminders_sent:
    if len(reminders_sent) > max_reminders_per_day:
        print("too many reminders scheduled today!")
        break  # stop loop if guardrail exceeded
    else:
        print(f"Sending: {reminder}")
        # Simulate user missing a reminder
        if "12 PM" in reminder:
            missed_reminders.append(reminder)

# After loop, show missed reminders
print("Missed reminders log:", missed_reminders)