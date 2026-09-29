# Problem Statement

## Title
Medicine Reminder

## Problem

Many people, especially elderly patients or those managing chronic conditions, need to take multiple medicines at specific times each day. Forgetting to take a medicine on time, or losing track of which medicines have already been taken, can affect health outcomes. Writing down or manually remembering a medicine schedule is inconvenient and error-prone, particularly when the list of medicines changes frequently.

## Objective

To build a simple, easy-to-use command-line application that allows a user to:
- Record the medicines they need to take, along with the time each one should be taken.
- View the complete list of stored medicines and their timings at any point.
- Exit the application safely when done.

The goal is to provide a lightweight digital alternative to a handwritten medicine schedule, using only core Python concepts, so that a user does not have to rely on memory alone to keep track of their medicines.

## Scope

This project focuses on the basic functionality of storing and displaying medicine information during a single program session. It does not include:
- Persistent storage (data is not saved after the program is closed).
- Automated time-based alerts or notifications.
- A graphical user interface.

These are identified as potential future enhancements.

## Proposed Solution

A menu-driven Python console program was developed with three core operations:
1. **Add Medicine** – Takes the medicine name and time as input from the user and stores them in a list of dictionaries.
2. **View Medicines** – Iterates through the stored list and displays each medicine with its corresponding time.
3. **Exit** – Ends the program gracefully.

The program runs in a continuous loop, repeatedly showing the menu until the user chooses to exit, making it simple for a user to add multiple medicines and check the list as many times as needed within one session.

## Expected Outcome

A working command-line tool that demonstrates the practical use of loops, conditionals, lists, and dictionaries in Python to solve a small but relatable real-world problem — helping a user keep a running record of their medicines and reminder times.
