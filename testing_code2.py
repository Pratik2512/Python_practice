# TESTING A CLASS
# A variety of Assert Methods
"""
Method                   Use
--------------------------------------------------------
assertEqual(a, b)        Verify that a == b
assertNotEqual(a, b)     Verify that a != b
assertTrue(x)            Verify that x is True
assertFalse(x)           Verify that x is False
assertIn(item, list)     Verify that item is in list
assertNotIn(item, list)  Verify that item is not in list
"""

# A Class to Test


class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all th responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


# Define question, and make a survey.
question = "Which language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# The setUp() Method
"""The unittest.TestCase class has a setUp() method that allows you
to create these objects once and then use them in each of your test 
methods. When you include a setUp() method in a TestCase class, Python 
runs the setUp() method before running each method starting with test_.
Any objects created in the setUp() method are then available in each 
test method you write."""

# DO IT YOURSELF
# 1:Employee


class Employee:
    """Store information about the employee."""

    def __init__(self, first, last, salary):
        """Store the basic information about the employee."""
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary
        self.full_name = f"{self.first_name.title()} {self.last_name.title()}"

    def introduce(self):
        """Display the profile of the employee."""
        print(f"The employee: {self.full_name} receives annual salary"
              f" ${self.annual_salary}.")

    def give_raise(self, increase=5000):
        """Give raise to the employee."""
        self.annual_salary = self.annual_salary + increase


pratik = Employee('pratik', 'mohite', 40000)
pratik.give_raise()
pratik.introduce()

pratik.give_raise(10000)
pratik.introduce()
