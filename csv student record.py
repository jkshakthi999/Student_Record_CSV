import csv
class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename=filename
    def add_student(self, name, roll, grade):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, roll, grade])
        print(f"Student {name} added successfully!")
    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                reader=csv.reader(file)
                print("\n--- Student Records ---")
                for row in reader:
                    print(f"Name: {row[0]}, Roll: {row[1]}, Grade: {row[2]}")
        except FileNotFoundError:
            print("No records found.")
    def search_student(self, roll):
        try:
            with open(self.filename, "r") as file:
                reader=csv.reader(file)
                for row in reader:
                    if row[1]==roll:
                        print(f"Found: Name={row[0]}, Roll={row[1]}, Grade={row[2]}")
                        return
            print("Student not found.")
        except FileNotFoundError:
            print("No records found.")
    def generate_report(self):
        try:
            grades=[]
            with open(self.filename, "r") as file:
                reader=csv.reader(file)
                for row in reader:
                    grades.append(row[2])
            if grades:
                print("\n--- Report ---")
                print(f"Total Students: {len(grades)}")
                print(f"Grades List: {grades}")
                print(f"Highest Grade: {max(grades)}")
            else:
                print("No data to generate report.")
        except FileNotFoundError:
            print("No records found.")
