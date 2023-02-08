# User class

class User:
    """Create a profile of the user."""
    def __init__(self, name, surname, age, city):
        self.first_name = name
        self.last_name = surname
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Display the user info."""
        print(f"name: {self.first_name.title()} {self.last_name.title()}")
        print(f"age: {self.age} years")
        print(f"city: {self.city.title()}.")

    def greet_user(self):
        """Greet the user."""
        print(f"\nHello {self.first_name}!")

    def increment_login_attempt(self):
        """Add the number of attempts to the original tally."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the no of login attempts."""
        self.login_attempts = 0
