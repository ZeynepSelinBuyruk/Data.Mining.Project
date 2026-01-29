from abc import ABC, abstractmethod
from datetime import datetime

class Student(ABC):
    """
    Abstract base class representing a university student.
    
    Encapsulation: All attributes are private (protected with underscore prefix)
    Abstraction: Contains abstract method that subclasses must implement
    """
    
    def __init__(self, student_id, full_name, email, department, enrollment_year):
        """Initialize student with shared attributes."""
        self._student_id = student_id
        self._full_name = full_name
        self._email = email
        self._department = department
        self._enrollment_year = enrollment_year
    
    # ===== ENCAPSULATION: Getter Methods =====
    def get_student_id(self):
        """Get student ID."""
        return self._student_id
    
    def get_full_name(self):
        """Get student's full name."""
        return self._full_name
    
    def get_email(self):
        """Get student's email."""
        return self._email
    
    def get_department(self):
        """Get student's department."""
        return self._department
    
    def get_enrollment_year(self):
        """Get student's enrollment year."""
        return self._enrollment_year
    
    # ===== ENCAPSULATION: Setter Methods with Validation =====
    def set_full_name(self, full_name):
        """Set student's name with validation."""
        if isinstance(full_name, str) and len(full_name.strip()) > 0:
            self._full_name = full_name
        else:
            raise ValueError("Name must be a non-empty string")
    
    def set_email(self, email):
        """Set student's email with validation."""
        if isinstance(email, str) and "@" in email:
            self._email = email
        else:
            raise ValueError("Invalid email format")
    
    def set_department(self, department):
        """Set student's department with validation."""
        if isinstance(department, str) and len(department.strip()) > 0:
            self._department = department
        else:
            raise ValueError("Department must be a non-empty string")
    
    # ===== ABSTRACTION: Abstract Method =====
    @abstractmethod
    def get_student_status(self):
        """Abstract method that must be implemented by subclasses."""
        pass
    
    # ===== POLYMORPHIC METHOD =====
    def display_info(self):
        """Display basic student information. Can be overridden by subclasses."""
        return f"\nStudent ID: {self._student_id}\nName: {self._full_name}\nEmail: {self._email}\nDepartment: {self._department}\nEnrollment Year: {self._enrollment_year}"
    
    def get_years_enrolled(self):
        """Calculate years of enrollment."""
        current_year = datetime.now().year
        return current_year - self._enrollment_year


class UndergraduateStudent(Student):
    """
    Represents an undergraduate student pursuing a Bachelor's degree.
    
    Inheritance: Extends Student class using super()
    Polymorphism: Overrides get_student_status() with unique implementation
    """
    
    def __init__(self, student_id, full_name, email, department, enrollment_year, current_year, gpa):
        """Initialize undergraduate student with inherited and unique attributes."""
        super().__init__(student_id, full_name, email, department, enrollment_year)
        self._current_year = current_year
        self._gpa = gpa
    
    # ===== Getter Methods =====
    def get_current_year(self):
        """Get current academic year (1-4)."""
        return self._current_year
    
    def get_gpa(self):
        """Get student's GPA."""
        return self._gpa
    
    # ===== Setter Methods with Validation =====
    def set_current_year(self, year):
        """Set current year with validation (1-4)."""
        if 1 <= year <= 4:
            self._current_year = year
        else:
            raise ValueError("Current year must be between 1 and 4")
    
    def set_gpa(self, gpa):
        """Set GPA with validation (0.0-4.0)."""
        if 0.0 <= gpa <= 4.0:
            self._gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    
    # ===== POLYMORPHISM: Override abstract method =====
    def get_student_status(self):
        """
        Returns undergraduate-specific status information.
        Implements abstract method from Student class.
        """
        year_names = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}
        status = year_names.get(self._current_year, "Unknown")
        return f"{status} - GPA: {self._gpa:.2f}"
    
    # ===== Override polymorphic method =====
    def display_info(self):
        """Display detailed undergraduate student information."""
        base_info = super().display_info()
        return f"{base_info}\n--- Undergraduate Student ---\nAcademic Year: {self._current_year}\nGPA: {self._gpa:.2f}\nStatus: {self.get_student_status()}"


class GraduateStudent(Student):
    """
    Represents a graduate student pursuing a Master's degree.
    
    Inheritance: Extends Student class using super()
    Polymorphism: Overrides get_student_status() with unique implementation
    """
    
    def __init__(self, student_id, full_name, email, department, enrollment_year, thesis_title, advisor_name):
        """Initialize graduate student with inherited and unique attributes."""
        super().__init__(student_id, full_name, email, department, enrollment_year)
        self._thesis_title = thesis_title
        self._advisor_name = advisor_name
    
    # ===== Getter Methods =====
    def get_thesis_title(self):
        """Get thesis title."""
        return self._thesis_title
    
    def get_advisor_name(self):
        """Get advisor's name."""
        return self._advisor_name
    
    # ===== Setter Methods with Validation =====
    def set_thesis_title(self, title):
        """Set thesis title with validation."""
        if isinstance(title, str) and len(title.strip()) > 0:
            self._thesis_title = title
        else:
            raise ValueError("Thesis title must be a non-empty string")
    
    def set_advisor_name(self, name):
        """Set advisor name with validation."""
        if isinstance(name, str) and len(name.strip()) > 0:
            self._advisor_name = name
        else:
            raise ValueError("Advisor name must be a non-empty string")
    
    # ===== POLYMORPHISM: Override abstract method =====
    def get_student_status(self):
        """
        Returns graduate-specific status information.
        Implements abstract method from Student class.
        """
        years = self.get_years_enrolled()
        return f"Master's Student - {years} years enrolled - Advisor: {self._advisor_name}"
    
    # ===== Override polymorphic method =====
    def display_info(self):
        """Display detailed graduate student information."""
        base_info = super().display_info()
        return f"{base_info}\n--- Graduate Student (Master's) ---\nThesis Title: {self._thesis_title}\nAdvisor: {self._advisor_name}\nStatus: {self.get_student_status()}"


class PhDStudent(Student):
    """
    Represents a doctoral student pursuing a PhD degree.
    
    Inheritance: Extends Student class using super()
    Polymorphism: Overrides get_student_status() with unique implementation
    """
    
    def __init__(self, student_id, full_name, email, department, enrollment_year, 
                 dissertation_topic, research_area, publication_count):
        """Initialize PhD student with inherited and unique attributes."""
        super().__init__(student_id, full_name, email, department, enrollment_year)
        self._dissertation_topic = dissertation_topic
        self._research_area = research_area
        self._publication_count = publication_count
    
    # ===== Getter Methods =====
    def get_dissertation_topic(self):
        """Get dissertation topic."""
        return self._dissertation_topic
    
    def get_research_area(self):
        """Get research area."""
        return self._research_area
    
    def get_publication_count(self):
        """Get number of publications."""
        return self._publication_count
    
    # ===== Setter Methods with Validation =====
    def set_dissertation_topic(self, topic):
        """Set dissertation topic with validation."""
        if isinstance(topic, str) and len(topic.strip()) > 0:
            self._dissertation_topic = topic
        else:
            raise ValueError("Dissertation topic must be a non-empty string")
    
    def set_research_area(self, area):
        """Set research area with validation."""
        if isinstance(area, str) and len(area.strip()) > 0:
            self._research_area = area
        else:
            raise ValueError("Research area must be a non-empty string")
    
    def set_publication_count(self, count):
        """Set publication count with validation."""
        if isinstance(count, int) and count >= 0:
            self._publication_count = count
        else:
            raise ValueError("Publication count must be a non-negative integer")
    
    def add_publication(self):
        """Increment publication count by one."""
        self._publication_count += 1
    
    # ===== POLYMORPHISM: Override abstract method =====
    def get_student_status(self):
        """
        Returns doctoral-specific status information.
        Implements abstract method from Student class.
        """
        years = self.get_years_enrolled()
        return f"PhD Student - {years} years enrolled - Publications: {self._publication_count}"
    
    # ===== Override polymorphic method =====
    def display_info(self):
        """Display detailed PhD student information."""
        base_info = super().display_info()
        return f"{base_info}\n--- PhD Student ---\nDissertation Topic: {self._dissertation_topic}\nResearch Area: {self._research_area}\nPublications: {self._publication_count}\nStatus: {self.get_student_status()}"


# Create UndergraduateStudent objects
undergrad1 = UndergraduateStudent(
    student_id="20231001",
    full_name="Ahmet Yilmaz",
    email="ahmet.yilmaz@university.edu",
    department="Computer Science",
    enrollment_year=2022,
    current_year=3,
    gpa=3.45
)

undergrad2 = UndergraduateStudent(
    student_id="20231002",
    full_name="Zeynep Kaya",
    email="zeynep.kaya@university.edu",
    department="Mathematics",
    enrollment_year=2023,
    current_year=2,
    gpa=3.87
)

# Create GraduateStudent objects
grad1 = GraduateStudent(
    student_id="20201101",
    full_name="Mehmet Ozturk",
    email="mehmet.ozturk@university.edu",
    department="Computer Science",
    enrollment_year=2022,
    thesis_title="Machine Learning Applications in Healthcare",
    advisor_name="Prof. Dr. Ali Demir"
)

# Create PhDStudent objects
phd1 = PhDStudent(
    student_id="20191001",
    full_name="Fatima Hassan",
    email="fatima.hassan@university.edu",
    department="Physics",
    enrollment_year=2019,
    dissertation_topic="Quantum Computing and Cryptography",
    research_area="Quantum Information Science",
    publication_count=8
)

print("✓ All student objects created successfully!")

# Create a list to store all students (demonstrating polymorphism)
students = [undergrad1, undergrad2, grad1, phd1]

print(f"Total students in system: {len(students)}")
print(f"Student types: {[type(s).__name__ for s in students]}")
print("✓ All students stored in polymorphic list!")

print("\n" + "="*60)
print("POLYMORPHISM DEMONSTRATION: Calling get_student_status()")
print("="*60)

for student in students:
    # All students respond to the same method call differently
    print(f"\n{student.get_full_name()} ({type(student).__name__}):")
    print(f"  Status: {student.get_student_status()}")

print("\n" + "="*60)
print("POLYMORPHISM DEMONSTRATION: Calling display_info()")
print("="*60)

for student in students:
    # display_info() is also polymorphic - returns different formatted info
    print(student.display_info())

print("\n" + "="*60)
print("ENCAPSULATION DEMONSTRATION: Valid Updates")
print("="*60)

# Update undergraduate GPA (valid)
print(f"\nBefore: {undergrad1.get_full_name()} - GPA: {undergrad1.get_gpa()}")
undergrad1.set_gpa(3.67)
print(f"After:  {undergrad1.get_full_name()} - GPA: {undergrad1.get_gpa()}")
print("✓ GPA updated successfully")

# Update undergraduate year (valid)
print(f"\nBefore: {undergrad2.get_full_name()} - Year: {undergrad2.get_current_year()}")
undergrad2.set_current_year(3)
print(f"After:  {undergrad2.get_full_name()} - Year: {undergrad2.get_current_year()}")
print("✓ Academic year updated successfully")

# Add publication for PhD student
print(f"\nBefore: {phd1.get_full_name()} - Publications: {phd1.get_publication_count()}")
phd1.add_publication()
phd1.add_publication()
print(f"After:  {phd1.get_full_name()} - Publications: {phd1.get_publication_count()}")
print("✓ Publications updated successfully")

# Update graduate student advisor
print(f"\nBefore: {grad1.get_full_name()} - Advisor: {grad1.get_advisor_name()}")
grad1.set_advisor_name("Prof. Dr. Ayse Kaya")
print(f"After:  {grad1.get_full_name()} - Advisor: {grad1.get_advisor_name()}")
print("✓ Advisor updated successfully")

print("\n" + "="*60)
print("ENCAPSULATION DEMONSTRATION: Invalid Updates (Error Handling)")
print("="*60)

# Attempt to set invalid GPA (out of range)
try:
    undergrad1.set_gpa(4.5)
except ValueError as e:
    print(f"\n✗ Error setting GPA: {e}")

# Attempt to set invalid year
try:
    undergrad2.set_current_year(5)
except ValueError as e:
    print(f"✗ Error setting year: {e}")

# Attempt to set invalid publication count
try:
    phd1.set_publication_count(-5)
except ValueError as e:
    print(f"✗ Error setting publication count: {e}")

# Attempt to set invalid email
try:
    grad1.set_email("invalid-email-format")
except ValueError as e:
    print(f"✗ Error setting email: {e}")

print("\n✓ All encapsulation protections working correctly!")

print("\n" + "="*70)
print("COMPLETE UNIVERSITY STUDENT INFORMATION SYSTEM")
print("="*70)

for i, student in enumerate(students, 1):
    print(f"\n{'─'*70}")
    print(f"STUDENT {i}/{len(students)}")
    print(f"{'─'*70}")
    print(student.display_info())
    print()

print("="*70)
print("SYSTEM SUMMARY")
print("="*70)

# Statistics
undergrads = sum(1 for s in students if isinstance(s, UndergraduateStudent))
grads = sum(1 for s in students if isinstance(s, GraduateStudent))
phds = sum(1 for s in students if isinstance(s, PhDStudent))

print(f"\nTotal Students: {len(students)}")
print(f"  ├─ Undergraduate: {undergrads}")
print(f"  ├─ Graduate (Master's): {grads}")
print(f"  └─ Doctoral (PhD): {phds}")

print(f"\nDepartments represented:")
departments = set(s.get_department() for s in students)
for dept in sorted(departments):
    dept_students = [s.get_full_name() for s in students if s.get_department() == dept]
    print(f"  ├─ {dept}: {', '.join(dept_students)}")

print("\n✓ System demonstration completed successfully!")
print("\n" + "="*70)
