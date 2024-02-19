from main import StudentsInMLOps

def test_enroll_students():
    """Test enrolling students."""
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5

def test_drop_students():
    """Test dropping students."""
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)  # Enroll some students first
    class_instance.dropStudents(2)
    assert class_instance.getTotalStrength() == 3

def test_total_strength():
    """Test the total strength method."""
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(3)
    assert class_instance.getTotalStrength() == 3

def test_class_name():
    """Test the get class name method."""
    class_instance = StudentsInMLOps()
    assert class_instance.getClassName() == "Students in MLOps"
