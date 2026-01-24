# Student Grade Calculator
# Week 2 Project – Control Flow & Data Structures
# Author: Prabhu Sangeetha

import datetime

INPUT_FILE = "test_students.txt"

# -------------------- GRADE LOGIC --------------------
def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent! Keep it up"
    elif avg >= 80:
        return "B", "Very Good"
    elif avg >= 70:
        return "C", "Good, but you can improve"
    elif avg >= 60:
        return "D", "Needs Improvement"
    else:
        return "F", "Failed"

# -------------------- READ INPUT FROM FILE --------------------
def read_input_file(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]
        return lines
    except FileNotFoundError:
        print(f"ERROR: '{filename}' file not found.")
        print("Please create the file and try again.")
        exit()

# -------------------- DISPLAY RESULTS --------------------
def display_results(results):
    print("\n" + "=" * 70)
    print(f"{'Name':<15}{'Avg':>8}{'Grade':>10}   Comment")
    print("-" * 70)
    for r in results:
        print(f"{r['name']:<15}{r['average']:>8.1f}{r['grade']:>10}   {r['comment']}")

# -------------------- MAIN PROGRAM --------------------
def main():
    data = read_input_file(INPUT_FILE)
    index = 0

    print("=" * 50)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # Number of students
    num_students = int(data[index])
    index += 1
    print(f"Number of students: {num_students}")

    results = []

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")

        name = data[index]; index += 1
        math = float(data[index]); index += 1
        science = float(data[index]); index += 1
        english = float(data[index]); index += 1

        print(f"Name: {name}")
        print(f"Math: {math}")
        print(f"Science: {science}")
        print(f"English: {english}")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        results.append({
            "name": name,
            "average": avg,
            "grade": grade,
            "comment": comment
        })

    display_results(results)

    averages = [r["average"] for r in results]
    print("\nCLASS STATISTICS")
    print("-" * 40)
    print("Class Average:", round(sum(averages) / len(averages), 1))
    print("Highest:", max(averages))
    print("Lowest :", min(averages))

    print("\nThank you for using the Grade Calculator!")

# -------------------- PROGRAM ENTRY --------------------
if __name__ == "__main__":
    main()
