students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display All")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}")
        else:
            print("Student not found!")

    elif choice == 3:
        print("\nAll Students and Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")