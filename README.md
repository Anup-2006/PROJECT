# Medicine Reminder

A simple command-line Python application that helps users keep track of the medicines they need to take and the times at which to take them.

## Description

Medicine Reminder is a beginner-level console application built in Python. It allows a user to store the names of medicines along with the time they should be taken, and to view the full list at any time during the session. The project demonstrates the use of fundamental Python concepts such as loops, conditionals, functions-free procedural flow, lists, dictionaries, and user input handling.

## Features

- **Add Medicine** – Enter a medicine name and the time it should be taken (HH:MM format), which is stored in the program's memory.
- **View Medicines** – Displays a numbered list of all medicines added so far, along with their scheduled times.
- **Exit** – Safely exits the program with a closing message.
- Simple menu-driven interface that keeps running until the user chooses to exit.
- Input validation for menu choices (prompts the user again if an invalid option is entered).

## How It Works

1. When the program starts, it prints a welcome header and shows a menu with three options.
2. The user enters a number (1, 2, or 3) to choose an action.
3. Based on the choice:
   - **1** asks for the medicine name and time, then adds it to an in-memory list.
   - **2** prints every medicine currently stored, or a message if the list is empty.
   - **3** prints a thank-you message and ends the program.
4. Any other input shows an error message and redisplays the menu.

## Technologies Used

- Python 3 (no external libraries required)

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:
   ```
   python medicine_reminder.py
   ```
5. Follow the on-screen menu to add and view medicines.

## Example Usage

```
Medicine Reminder
-----------------

1. Add medicine
2. View medicines
3. Exit
Enter your choice: 1
Medicine name: Paracetamol
Time to take (HH:MM): 09:00
Medicine added successfully!

1. Add medicine
2. View medicines
3. Exit
Enter your choice: 2
1. Paracetamol - 09:00
```

## Future Improvements

- Store medicines permanently using a file (CSV/JSON) or a database so data isn't lost after the program closes.
- Add real-time reminders/alerts using the `datetime` and `time` modules.
- Allow editing or deleting a medicine entry.
- Add dosage information and notes for each medicine.
- Build a graphical or web-based interface.

## Author

Student project submitted as part of the VITyarthi "Build Your Own Project" module.
