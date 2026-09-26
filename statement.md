# Problem Statement
Many people — especially elderly patients, individuals managing chronic conditions, and those on multi-drug regimens — struggle to take their medicines at the correct times. Missed or delayed doses can reduce treatment effectiveness and, in some cases, lead to serious health complications. There is a need for a simple, reliable tool that reminds users when to take their medicine.

# Scope of the Project
This project is a command-line based Medicine Reminder application. It allows a user to:
- Register and manage a personal list of medicines with a scheduled time and optional instructions
- Receive an on-screen (and, on Windows, audible) reminder when a dose is due
- Remove reminders that are no longer needed
- Keep this data saved between sessions in a local file

**Out of scope:** the system does not provide medical advice, does not connect to pharmacies or healthcare providers, and does not send notifications outside the application (e.g., SMS or push notifications). It is intended as a personal reminder tool, not a certified medical device.

# Target Users
- Patients managing daily or multiple-times-a-day medication schedules
- Elderly individuals who may need extra support remembering doses
- Caregivers setting up reminders on behalf of a dependent
- Students or developers studying scheduling and file-based CRUD application design

# High-Level Features
- **Medicine Management:** add, view, and remove medicine entries (name, 24-hour time, optional instructions)
- **Automated Reminders:** the system checks the current time every second and alerts the user once per day when a dose is due
- **Data Persistence:** all medicine data is saved locally in `medicines.json`, written safely so it can't be left in a corrupted state
- **Input Validation & Error Handling:** the system validates all user input and the stored data file, and handles errors gracefully without crashing
