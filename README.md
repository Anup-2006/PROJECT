# Medicine Reminder

## Overview
Medicine Reminder is a command-line application that helps patients and caregivers manage daily medication schedules. It stores each medicine's name, scheduled time, and instructions, and alerts the user when a dose is due — helping reduce the risk of missed doses.

## Features
- **Medicine Management:** add, view, and remove medicine reminders (name, 24-hour time, optional instructions).
- **Reminder Engine:** continuously checks the current time and triggers an alert exactly once per day when a scheduled dose is due.
- **Alerts:** prints a clear on-screen reminder and plays a system beep on Windows (via `winsound`), with a terminal bell as a fallback on other platforms.
- **Input Validation & Error Handling:** rejects empty names and invalid/out-of-range times, and never crashes on bad input.
- **Safe Persistent Storage:** saves data to `medicines.json` using a write-to-temp-file-then-replace pattern, so a crash mid-save can't corrupt the file.
- **Data Integrity Checks:** validates the structure and types of every entry when loading, and reports a clear error instead of crashing if the file is damaged or hand-edited incorrectly.

## Technologies / Tools Used
- **Language:** Python 3.10+ (standard library only — `json`, `os`, `time`, `datetime`, `pathlib`, and `winsound` on Windows)
- **Storage:** JSON file-based storage (`medicines.json`)
- **Version Control:** Git & GitHub
- **Editor:** VS Code

## Project Structure
```
medicine-reminder/
├── README.md
├── statement.md
├── MEDICINE_REMINDER.py     (single-file application)
└── medicines.json           (auto-created next to the script on first save)
```
The application currently lives in one file, `MEDICINE_REMINDER.py`, organized into clearly separated functions: `load_medicines`, `save_medicines`, `get_valid_time`, `add_medicine`, `show_medicines`, `remove_medicine`, `alert`, `start_reminders`, and `main`. Data is stored in `medicines.json`, written safely using a temporary-file-then-replace pattern so the file is never left half-written.

## Steps to Install & Run the Project
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/medicine-reminder.git
   cd medicine-reminder
   ```
2. **Ensure Python 3.10+ is installed** (no external packages are required — the script only uses the standard library, plus the built-in `winsound` module for an audible beep on Windows)
   ```bash
   python --version
   ```
3. **Run the application**
   ```bash
   python MEDICINE_REMINDER.py
   ```
4. **Follow the on-screen menu**:
   - `1` Add a reminder (name, 24-hour `HH:MM` time, optional instructions)
   - `2` View all saved reminders, sorted by time
   - `3` Remove a reminder by its number
   - `4` Start monitoring — the app checks the clock every second and alerts you when a dose is due (press `Ctrl+C` to return to the menu)
   - `5` Exit

## Instructions for Testing
The application was manually tested against the following boundary and error cases; every case below was verified to behave correctly without the program crashing:

**Input validation**
- Empty medicine name → rejected with `Medicine name cannot be empty.`
- Invalid time formats (`8am`, `24:00`, `12:60`, `08:30:00`, blank, letters) → rejected and re-prompted
- Single-digit hour/minute (`9:5`) → accepted and normalized to `09:05`
- Extra surrounding spaces (`  08:30  `) → trimmed and accepted

**Removing reminders**
- Non-existent reminder number → `Reminder number not found.`
- Non-numeric input (e.g. `abc`) → `Please enter a valid number.`
- Removing from an empty list → shows `No medicine reminders saved.` and does not ask for a number

**Starting reminders**
- Starting with no medicines saved → `Add a medicine reminder first.`
- A due reminder correctly triggers the alert message (and a system beep on Windows) only once per day per medicine
- `Ctrl+C` during monitoring stops it cleanly and returns to the menu without crashing

**Data file integrity (`medicines.json`)**
- File contains invalid JSON syntax → `Could not load reminders: The medicines.json file is damaged or incomplete.`
- File contains something other than a list → `...must contain a list.`
- An entry is missing a required field → `...is missing information.`
- An entry has a wrong data type (e.g. `id` as text) → `...has invalid information.`
- An entry has an invalid time value (e.g. `99:99`) → `...has an invalid time.`

**General**
- Choosing a menu option outside 1–5 → `Invalid choice. Enter a number from 1 to 5.`

To repeat this testing yourself, run the app and try the inputs above at each menu option, or delete/corrupt `medicines.json` by hand and relaunch the app to confirm it fails gracefully rather than crashing.

## Screenshots

**Adding a reminder (with an invalid time first) and viewing the saved list:**

<img width="606" height="676" alt="shot1_add_view" src="https://github.com/user-attachments/assets/eb41167f-4693-4f24-9cb4-28d74be2f349" />


**Removing a reminder — an invalid number, then a non-numeric entry:**

<img width="504" height="722" alt="shot2_remove_boundaries" src="https://github.com/user-attachments/assets/00214ea9-ae18-4a82-97ea-d90cb8e60c47" />


**A live reminder alert firing, then stopped with Ctrl+C:**


<img width="678" height="423" alt="shot3_live_alert" src="https://github.com/user-attachments/assets/dcb644da-c718-4dd1-9d9b-d0ec6585e3ec" />


## Author
_Anup Kumar Jena_

_Integrated M.Tech BioInformatics_

_26MIB10011_
