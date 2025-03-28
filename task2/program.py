import csv

# Define the Student class
class Student:
    def __init__(self, name, math_marks, physics_marks, geography_marks):
        self.name = name
        self.math_marks = math_marks
        self.physics_marks = physics_marks
        self.geography_marks = geography_marks
        self.max_marks = 50  # Max marks for each subject
        
    def calculate_average(self):
        total_marks = self.math_marks + self.physics_marks + self.geography_marks
        average_marks = total_marks / 3
        return average_marks
    
    def calculate_percentage(self):
        total_marks = self.math_marks + self.physics_marks + self.geography_marks
        percentage = (total_marks / (self.max_marks * 3)) * 100
        return percentage
    
    def get_student_data(self):
        average = self.calculate_average()
        percentage = self.calculate_percentage()
        return [self.name, self.math_marks, self.physics_marks, self.geography_marks, average, percentage]

# Function to save data to CSV file
def save_data_to_csv(students, filename="student_marks.csv"):
    header = ["Name", "Math Marks", "Physics Marks", "Geography Marks", "Average Marks", "Percentage"]
    
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(header)
        
        # Write student data
        for student in students:
            writer.writerow(student.get_student_data())

# Main function
def main():
    students = []
    
    # Collect student data
    while True:
        name = input("Enter student's name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        
        try:
            math_marks = int(input("Enter marks for Math (0-50): "))
            physics_marks = int(input("Enter marks for Physics (0-50): "))
            geography_marks = int(input("Enter marks for Geography (0-50): "))
            
            if not (0 <= math_marks <= 50 and 0 <= physics_marks <= 50 and 0 <= geography_marks <= 50):
                print("Marks must be between 0 and 50. Try again.")
                continue

            student = Student(name, math_marks, physics_marks, geography_marks)
            students.append(student)
        except ValueError:
            print("Invalid input, please enter numeric values for marks.")
    
    # Save student data to CSV
    save_data_to_csv(students)
    print("Student data has been saved to 'student_marks.csv'.")

if __name__ == "__main__":
    main()
