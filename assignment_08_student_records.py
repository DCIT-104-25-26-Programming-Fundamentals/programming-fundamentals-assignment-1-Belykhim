def display_menu():
    # Show the main menu options
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    # Prompt for student details, scores, and save as a dictionary
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than zero.")
            return

        scores = []
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            scores.append(score)

        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        students.append(student)
        print(f'Student "{name}" added successfully.')

    except ValueError:
        print("Error: Invalid input. Please enter numbers for scores.")


def display_all_students(students):
    # Display all student records in a formatted table
    if not students:
        print("No student records found.")
        return

    print("\n--------------------------------------------------")
    print(f"{'Name':<15} {'ID':<12} {'Scores':<15} {'Average':<8}")
    print("--------------------------------------------------")

    for s in students:
        scores_str = ", ".join(str(int(x) if x.is_integer() else x) for x in s["scores"])
        avg = sum(s["scores"]) / len(s["scores"])
        print(f"{s['name']:<15} {s['id']:<12} {scores_str:<15} {avg:.2f}")

    print("--------------------------------------------------")


def calculate_student_average(students):
    # Find a student by ID and print their average score
    search_id = input("Enter student ID: ").strip()

    for s in students:
        if s["id"] == search_id:
            avg = sum(s["scores"]) / len(s["scores"])
            print(f"{s['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID {search_id} not found.")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()