# main.py

# --- Imports ---
import importlib
from dataclasses import dataclass

search_engine = None

try:
    search_engine = importlib.import_module("search_engine")
    search_inventory = search_engine.search_inventory
except (ModuleNotFoundError, AttributeError):
    def search_inventory(reminders, query):
        """Return reminders whose task or time contains ``query``.

        Matching is case-insensitive and ignores surrounding whitespace.  An
        empty query returns all reminders, which makes the function useful for
        callers that want to display the complete collection through the same
        search interface.
        """
        query = str(query).strip().casefold()
        if not query:
            return list(reminders)

        return [
            reminder
            for reminder in reminders
            if query in str(getattr(reminder, "task", "")).casefold()
            or query in str(getattr(reminder, "time", "")).casefold()
        ]

    class _FallbackSearchEngine:
        @staticmethod
        def search_inventory(reminders, query):
            return search_inventory(reminders, query)

    search_engine = _FallbackSearchEngine()

try:
    Reminder = importlib.import_module("models").Reminder
except ModuleNotFoundError:
    @dataclass
    class Reminder:
        task: str
        time: str
        completed: bool = False

# --- Data Store ---
reminders = []  # simple list to hold Reminder objects

# --- Menu Loop ---
def main():
    while True:
        print("n===Reminder med App ===")
        print("1. Set Reminder")
        print("2. View All Reminders")
        print("3. Search Reminders")
        print("4. Exit")

        try:
            choice = int(input("Enter choice (1-4): "))
        except ValueError:
            print(" Invalid input. Please type a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter reminder task (e.g., 'Drink water'): ")
            time = input("Enter reminder time (e.g., '14:00'): ")
            reminders.append(Reminder(task=task, time=time, completed=False))
            print(f" Reminder set: {task} at {time}")

        elif choice == "2":
            if not reminders:
                print("No reminders yet.")
            else:
                for r in reminders:
                    status = " Done" if r.completed else " Pending"
                    print(f"- {r.task} at {r.time} [{status}]")

        elif choice == "3":
            query = input("Enter search term: ")
            results = search_engine.search_inventory(reminders, query)
            if results:
                print(" Search Results:")
                for r in results:
                    print(f"- {r.task} at {r.time}")
            else:
                print("No matches found.")

        elif choice == "4":
            print("Exiting Reminder Med. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()