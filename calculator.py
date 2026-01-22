# Smart Calculator with History and Purpose

import json
import os
from datetime import datetime

FILE_NAME = "calc_history.json"


# Load history from file
def load_history():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("History file is not readable. Starting with empty history.")
        return []


history = load_history()


# Save history to file
def save_history():
    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def calculator():
    while True:
        print("\n====== SMART CALCULATOR ======")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. View Full History")
        print("8. View History by Date")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()

        # -------- FULL HISTORY --------
        if choice == '7':
            print("\n--- Calculation History ---")
            if not history:
                print("No history available.")
            else:
                for item in history:
                    print(
                        f"{item.get('time', 'N/A')} | "
                        f"{item.get('expression', 'N/A')} = "
                        f"{item.get('result', 'N/A')} | "
                        f"Purpose: {item.get('purpose', 'Not specified')}"
                    )
            continue

        # -------- HISTORY BY DATE --------
        elif choice == '8':
            date = input("Enter date (YYYY-MM-DD): ").strip()
            found = False

            for item in history:
                if item.get('time', '').startswith(date):
                    if not found:
                        print(f"\n--- History for {date} ---")
                        found = True

                    print(
                        f"{item.get('time')} | "
                        f"{item.get('expression')} = "
                        f"{item.get('result')} | "
                        f"Purpose: {item.get('purpose', 'Not specified')}"
                    )

            if not found:
                print(f"No history found for {date}.")
            continue

        # -------- EXIT --------
        elif choice == '9':
            print("Calculator closed. Goodbye!")
            break

        # -------- CALCULATIONS --------
        try:
            if choice in ['1', '2', '3', '4', '5']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = a + b
                    expression = f"{a} + {b}"

                elif choice == '2':
                    result = a - b
                    expression = f"{a} - {b}"

                elif choice == '3':
                    result = a * b
                    expression = f"{a} * {b}"

                elif choice == '4':
                    if b == 0:
                        print("Division by zero is not allowed.")
                        continue
                    result = a / b
                    expression = f"{a} / {b}"

                else:  # Power
                    result = a ** b
                    expression = f"{a} ^ {b}"

            elif choice == '6':
                a = float(input("Enter a number: "))
                if a < 0:
                    print("Square root of a negative number is not possible.")
                    continue
                result = a ** 0.5
                expression = f"sqrt({a})"

            else:
                print("Invalid option. Please choose between 1 and 9.")
                continue

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # -------- SAVE RESULT --------
        purpose = input("Purpose of this calculation: ").strip()
        if purpose == "":
            purpose = "Not specified"

        print("Result:", result)

        history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "expression": expression,
            "result": result,
            "purpose": purpose
        })

        save_history()


# Program starts here
if __name__ == "__main__":
    calculator()
