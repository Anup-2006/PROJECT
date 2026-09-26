import json
import os
import time
from datetime import datetime
from pathlib import Path

try:
    import winsound
except ImportError:
    winsound = None


DATA_FILE = Path(__file__).with_name("medicines.json")


def load_medicines():
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("The medicines.json file is damaged or incomplete.") from error

    if not isinstance(data, list):
        raise ValueError("The medicines.json file must contain a list.")

    for medicine in data:
        if not isinstance(medicine, dict):
            raise ValueError("A medicine entry in medicines.json is invalid.")
        if not all(key in medicine for key in ("id", "name", "time", "instructions")):
            raise ValueError("A medicine entry in medicines.json is missing information.")
        if not isinstance(medicine["id"], int) or not isinstance(medicine["name"], str):
            raise ValueError("A medicine entry in medicines.json has invalid information.")
        if not isinstance(medicine["instructions"], str):
            raise ValueError("A medicine entry in medicines.json has invalid instructions.")
        if not isinstance(medicine["time"], str):
            raise ValueError("A medicine entry in medicines.json has an invalid time.")
        try:
            datetime.strptime(medicine["time"], "%H:%M")
        except ValueError as error:
            raise ValueError("A medicine entry in medicines.json has an invalid time.") from error

    return data


def save_medicines(medicines):
    temporary_file = DATA_FILE.with_suffix(".json.tmp")
    temporary_file.write_text(
        json.dumps(medicines, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    os.replace(temporary_file, DATA_FILE)


def get_valid_time():
    while True:
        value = input("Reminder time (24-hour HH:MM, for example 08:30): ").strip()
        try:
            return datetime.strptime(value, "%H:%M").strftime("%H:%M")
        except ValueError:
            print("Invalid time. Enter a time such as 08:30 or 17:45.")


def add_medicine(medicines):
    name = input("Medicine name: ").strip()
    if not name:
        print("Medicine name cannot be empty.")
        return

    reminder_time = get_valid_time()
    instructions = input("Instructions (optional): ").strip()
    next_id = max((medicine["id"] for medicine in medicines), default=0) + 1
    medicines.append({
        "id": next_id,
        "name": name,
        "time": reminder_time,
        "instructions": instructions,
    })
    save_medicines(medicines)
    print("Reminder saved.")


def show_medicines(medicines):
    if not medicines:
        print("No medicine reminders saved.")
        return

    print("\nSaved medicine reminders:")
    for medicine in sorted(medicines, key=lambda item: (item["time"], item["name"].lower())):
        details = f" - {medicine['instructions']}" if medicine["instructions"] else ""
        print(f"{medicine['id']}. {medicine['time']} - {medicine['name']}{details}")


def remove_medicine(medicines):
    show_medicines(medicines)
    if not medicines:
        return

    try:
        medicine_id = int(input("Enter the reminder number to remove: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    remaining = [medicine for medicine in medicines if medicine["id"] != medicine_id]
    if len(remaining) == len(medicines):
        print("Reminder number not found.")
        return

    medicines[:] = remaining
    save_medicines(medicines)
    print("Reminder removed.")


def alert(medicine):
    print(f"\nREMINDER: It is time for {medicine['name']}.")
    if medicine["instructions"]:
        print(f"Instructions: {medicine['instructions']}")
    print("Follow the instructions given by your healthcare professional.\a")
    if winsound is not None:
        try:
            winsound.MessageBeep()
        except RuntimeError:
            pass


def start_reminders(medicines):
    if not medicines:
        print("Add a medicine reminder first.")
        return

    print("Reminders are running. Press Ctrl+C to return to the menu.")
    last_alerted = {}
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            today = now.date()
            for medicine in medicines:
                if medicine["time"] == current_time and last_alerted.get(medicine["id"]) != today:
                    alert(medicine)
                    last_alerted[medicine["id"]] = today
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReminder monitoring stopped.")


def main():
    try:
        medicines = load_medicines()
    except (OSError, ValueError) as error:
        print(f"Could not load reminders: {error}")
        return

    while True:
        print("\n===== MEDICINE REMINDER =====")
        print("1. Add reminder")
        print("2. View reminders")
        print("3. Remove reminder")
        print("4. Start reminders")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                add_medicine(medicines)
            elif choice == "2":
                show_medicines(medicines)
            elif choice == "3":
                remove_medicine(medicines)
            elif choice == "4":
                start_reminders(medicines)
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Invalid choice. Enter a number from 1 to 5.")
        except OSError as error:
            print(f"Could not save reminders: {error}")


if __name__ == "__main__":
    main()