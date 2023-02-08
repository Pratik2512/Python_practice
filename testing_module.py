def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


"""def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title() """


"""def get_formatted_name(first, middle,last):
    full_name = f"{first}  {middle} {last}"
    return full_name.title()"""


def city_info(city, country, population=''):
    """Describe the city and its country neatly."""
    if population:
        name = f"{city}, {country}, Population:{population}"
    else:
        name = f"{city}, {country}"
    return name.title()


# Class
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

# Class 2


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
