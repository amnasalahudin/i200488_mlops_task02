class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0
        self.class_name = "Students in MLOps"

    def enrollStudents(self, number):
        """Enrolls the specified number of students into the class."""
        self.total_students += number

    def dropStudents(self, number):
        """Drops the specified number of students from the class."""
        # Ensure we don't have negative students
        self.total_students = max(0, self.total_students - number)

    def getTotalStrength(self):
        """Returns the total number of students currently enrolled."""
        return self.total_students

    def getClassName(self):
        """Returns the name of the class."""
        return self.class_name


def main():
    # Create an instance of the StudentsInMLOps class
    class_instance = StudentsInMLOps()

    # Enroll students
    print("Enrolling 5 students...")
    class_instance.enrollStudents(5)
    print(f"Total strength after enrollment: {class_instance.getTotalStrength()}")

    # Drop students
    print("Dropping 2 students...")
    class_instance.dropStudents(2)
    print(f"Total strength after dropping students: {class_instance.getTotalStrength()}")

    # Get total strength
    print(f"Final total strength: {class_instance.getTotalStrength()}")

    # Get class name
    print(f"Class Name: {class_instance.getClassName()}")

# Check if the script is run directly (and not imported)
if __name__ == '__main__':
    main()

