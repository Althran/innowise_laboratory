def main():
    students = []

    while True:
        print(f'\n--- Student Grade Analyzer ---\n'
              f'1. Add a new student\n'
              f'2. Add grades for a student\n'
              f'3. Show report\n'
              f'4. Find top performer\n'
              f'5. Exit')

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()

            student_exists = any(student['name'].lower() == name.lower() for student in students)

            if student_exists:
                print(f"Student '{name}' already exists!")
            else:
                new_student = {"name": name, "grades": []}
                students.append(new_student)
                print(f"Student '{name}' added successfully!")

        elif choice == "2":
            if not students:
                print("No students available. Please add students first.")
                continue

            name = input("Enter student name: ").strip()

            student = None
            for s in students:
                if s['name'].lower() == name.lower():
                    student = s
                    break

            if student is None:
                print(f"Student '{name}' not found!")
            else:
                print(f"Adding grades for {student['name']}. Enter 'done' to finish.")

                while True:
                    grade_input = input("Enter grade (0-100): ").strip()

                    if grade_input.lower() == 'done':
                        break

                    try:
                        grade = float(grade_input)
                        if 0 <= grade <= 100:
                            student['grades'].append(grade)
                            print(f"Grade {grade} added successfully!")
                        else:
                            print("Grade must be between 0 and 100!")
                    except ValueError:
                        print("Please enter a valid number or 'done' to finish!")

        elif choice == "3":
            if not students:
                print("No students available.")
                continue

            all_grades = []
            students_with_grades = 0

            print("\n--- Student Report ---")
            for student in students:
                try:
                    if student['grades']:
                        avg_grade = sum(student['grades']) / len(student['grades'])
                        print(f"{student['name']}'s average grade is {avg_grade:.2f}")
                        all_grades.extend(student['grades'])
                        students_with_grades += 1
                    else:
                        print(f"{student['name']}'s average grade is N/A")
                except ZeroDivisionError:
                    print(f"{student['name']}'s average grade is N/A")

            if all_grades:
                print(f"\nSummary:\n"
                      f"Highest grade: {max(all_grades)}\n"
                      f"Lowest grade: {min(all_grades)}\n"
                      f"Total grades entered: {len(all_grades)}")
            else:
                print("\nNo grades available for any student.")

        elif choice == "4":
            if not students:
                print("No students available.")
                continue

            students_with_valid_grades = []
            for student in students:
                if student['grades']:
                    try:
                        avg_grade = sum(student['grades']) / len(student['grades'])
                        students_with_valid_grades.append((student, avg_grade))
                    except:
                        continue

            if not students_with_valid_grades:
                print("No students with grades available.")
                continue

            top_student = max(students_with_valid_grades, key=lambda x: x[1])

            print(f"\nTop performer: {top_student[0]['name']}\n"
                  f"Average grade: {top_student[1]:.2f}\n"
                  f"Grades: {top_student[0]['grades']}")

        elif choice == "5":
            print("\nExecution completed")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
