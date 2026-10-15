
# =====================================================
# PROGRAMMING ACTIVITY 1: STUDENT INFORMATION SYSTEM
# Topic: Object-Oriented Programming - Encapsulation
# Time Allotment: 15 Minutes
# Mode: Individual Activity
# =====================================================

# LEARNING OBJECTIVE:
# Apply encapsulation by implementing setter methods
# that validate and control changes to private attributes.


# GENERAL INSTRUCTIONS:
# 1. Access the starter code through the GitHub link
#    provided by your teacher.
# 2. Duplicate the code by copying it into your own
#    Python file or notebook, or by forking the repository.
# 3. Rename your file:
#    Student_Encapsulation_YourName.py
# 4. Complete TASKS 1, 2, and 3 below.
# 5. Run your program and verify the expected results.
#
# IMPORTANT:
# - Do not modify the original shared starter code.
# - Do not remove the existing class or getter methods.
# - Replace the "pass" statements with your own code.


class Student:

    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age
        self.__grade = grade

    # Getter for age
    def get_age(self):
        return self.__age

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # ================================================
    # TASK 1: COMPLETE THE AGE SETTER
    # ================================================
    # Requirements:
    # - Accept ages greater than or equal to 0.
    # - Reject negative ages.
    # - Print "Invalid age!" for invalid values.
    # - Retain the previous age if input is invalid.

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age!")

    # ================================================
    # TASK 2: COMPLETE THE GRADE SETTER
    # ================================================
    # Requirements:
    # - Accept grades from 0 to 100 (inclusive).
    # - Reject grades below 0 or above 100.
    # - Print "Invalid grade!" for invalid values.
    # - Retain the previous grade if input is invalid.

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")


# =====================================================
# TASK 3: TEST YOUR PROGRAM
# =====================================================

# Create a student object
student1 = Student("Alex", 15, 90)

# Display original values
print("Original Student Information")
print("Name:", student1.name)
print("Age:", student1.get_age())
print("Grade:", student1.get_grade())


# TEST 1: Change age to 16
# Expected: Age becomes 16
student1.set_age(16)
print("\nTest 1 - Age:", student1.get_age())


# TEST 2: Change age to -5
# Expected: "Invalid age!" and age remains 16
student1.set_age(-5)
print("Test 2 - Age:", student1.get_age())


# TEST 3: Change grade to 95
# Expected: Grade becomes 95
student1.set_grade(95)
print("\nTest 3 - Grade:", student1.get_grade())


# TEST 4: Change grade to 150
# Expected: "Invalid grade!" and grade remains 95
student1.set_grade(150)
print("Test 4 - Grade:", student1.get_grade())


# TEST 5: Change grade to 0
# Expected: Grade becomes 0
student1.set_grade(0)
print("\nTest 5 - Grade:", student1.get_grade())


# =====================================================
# BONUS CHALLENGE: CONSTRUCTOR VALIDATION
# =====================================================
# The constructor currently accepts invalid values.
#
# Investigate what happens when you create:
#
# student2 = Student("Maria", -10, 150)
#
# CHALLENGE:
# Modify the constructor so that it uses the setter
# methods to validate age and grade during object
# creation.
#
# Ensure that invalid inputs are rejected and that
# the object retains valid default values.
#
# This challenge is optional.


# =====================================================
# REFLECTION QUESTION
# =====================================================
# Answer in 2-3 sentences:
#
# Why is it important to use setter methods instead
# of allowing unrestricted modification of an
# object's attributes?
#
# YOUR ANSWER:
# Setter methods are important because they set rules for modifying an object's attributes, 
# ensuring that the data remains valid and consistent.
# This helps prevent errors and absurd values in attributes like the age or grade of a student
# having a negative value. 
# 
#
#
# =====================================================
# CHECKLIST
# =====================================================
# [ ] Completed set_age() method
# [ ] Completed set_grade() method
# [ ] Executed all five test cases
# [ ] Verified the expected output
# [ ] Answered the reflection question
# [ ] Saved and submitted the completed Python file
#
# END OF ACTIVITY
# =====================================================