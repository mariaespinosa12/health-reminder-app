# nested_v1.py

# Multi-layered data: users with categories of reminders
users = [
    {
        "name": "Ana",
        "reminders": {
            "hydration": ["8:00 AM", "12:00 PM", "4:00 PM"],
            "medicine": ["9:00 AM", "9:00 PM"]
        }
    },
    {
        "name": "Luis",
        "reminders": {
            "hydration": ["7:30 AM", "1:00 PM", "6:00 PM"],
            "medicine": ["8:00 AM"]
        }
    }
]

# Outer loop: go through each user
for user in users:
    print(f"Checking reminders for {user['name']}:")

    # Inner loop: go through each category (hydration, medicine)
    for category, times in user["reminders"].items():
        print(f"  Category: {category}")

        # Nested loop: go through each reminder time
        for time in times:
            if category == "hydration":
                print(f"Hydration reminder at {time}")
            elif category == "medicine":
                print(f"Medicine reminder at {time}")
