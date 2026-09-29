# MEDICINE REMAINDER
print("Medicine Reminder")
print("-----------------")

medicines = []

while True:
    print("\n1. Add medicine")
    print("2. View medicines")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Medicine name: ")
        time_to_take = input("Time to take (HH:MM): ")
        medicines.append({"name": name, "time": time_to_take})
        print("Medicine added successfully!")

    elif choice == "2":
        if not medicines:
            print("No medicines added yet.")
        else:
            for i, med in enumerate(medicines, start=1):
                print(f"{i}. {med['name']} - {med['time']}")

    elif choice == "3":
        print("Thank you!")
        end = input("Press Enter to exit...")
        break

    else:
        print("Please choose 1, 2 or 3.")
