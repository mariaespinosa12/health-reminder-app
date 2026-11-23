import streamlit as st

# Page title
st.title("Health Reminder System")

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Choose an option",
    ["Dashboard", "Search Reminders", "Add Reminder"]
)

# Example data
reminders_sent = 8
missed_reminders = 3
max_reminders_per_day = 10

# Dashboard page
if menu == "Dashboard":
    st.header(" Health Reminder: Hidden Truth")

    # Calculate actual success rate
    adherence_rate = int((reminders_sent / (reminders_sent + missed_reminders)) * 100)

    st.write("Compare what you think about your habits versus what your reminder data shows.")

    col1, col2 = st.columns(2)

    # Left side: Perception
    with col1:
        st.subheader(" What You Think")

        st.warning("""
        **Perception**

        "I usually follow all of my health reminders."
        """)

        st.metric(
            label="Estimated Success",
            value="90%"
        )

    # Right side: Hidden Truth
    with col2:
        st.subheader(" Hidden Truth")

        st.success("""
        **Reality**

        Your reminder history shows that several reminders were missed.
        """)

        st.metric(
            label="Actual Success Rate",
            value=f"{adherence_rate}%"
        )

        st.progress(adherence_rate)

    st.divider()

    if adherence_rate < 80:
        st.error(
            f" Hidden Truth Revealed: Your actual reminder completion rate is only {adherence_rate}%."
        )
    else:
        st.success(" Great job! Your habits match your perception.")

    st.info(
        "Health Reminder helps users understand the difference between what they think they do and what their data actually shows."
    )

# Search page
elif menu == "Search Reminders":
    st.header(" Search Your Reminders")

    # Input for search query
    query = st.text_input("Enter a task or time to search for reminders:")

    # Example reminders data
    reminders = [
        {"task": "Drink water", "time": "08:00", "completed": True},
        {"task": "Take medication", "time": "12:00", "completed": False},
        {"task": "Exercise", "time": "18:00", "completed": True},
        {"task": "Meditate", "time": "20:00", "completed": False},
    ]

    # Search functionality
    if query:
        filtered_reminders = [
            r for r in reminders if query.lower() in r["task"].lower() or query.lower() in r["time"]
        ]
    else:
        filtered_reminders = reminders

    # Display results
    if filtered_reminders:
        st.write(f"Found {len(filtered_reminders)} reminder(s):")
        for r in filtered_reminders:
            status = "Done" if r["completed"] else "Pending"
            st.write(f"- {r['task']} at {r['time']} [{status}]")
    else:
        st.write("No reminders found matching your search.")

# Add Reminder page
elif menu == "Add Reminder":
    st.header(" Add a New Reminder")

    # Input fields for new reminder
    task = st.text_input("Enter reminder task (e.g., 'Drink water'):")
    time = st.text_input("Enter reminder time (e.g., '14:00'):")

    if st.button("Add Reminder"):
        if task and time:
            # Here you would normally save the reminder to a database or data store
            st.success(f"Reminder set: {task} at {time}")
        else:
            st.error("Please fill in both the task and time fields.")