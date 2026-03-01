import json

# File name where data will be stored
DATA_FILE = "python-projects/students.json"

def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f)

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def main():
    students = load_data()
    
    while True:
        print("\n--- 🎓 Student Record System ---")
        print("1. Add Student  2. View Students  3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            students[name] = grade
            save_data(students)
            print("Student added and saved!")
        elif choice == '2':
            print("\n--- Current Records ---")
            for name, grade in students.items():
                print(f"Name: {name} | Grade: {grade}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()