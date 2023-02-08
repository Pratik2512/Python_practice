# FUNCTIONS
# Defining a Function
def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()


def gap():
    """Skips a line"""
    print('\n')


# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting by calling name"""
    print(f"Hello, {username.title()}!")


greet_user('pratik')
# Arguments and Parameters
""" parameter -> a piece of information function needs to do its job
 eg. username in above example
 argument -> a piece of information that's passed from a func. call to func.
 eg. pratik in above example """


# Do It Yourself
# 1:Message


def display_message():
    """Display a short message"""
    print("Hey, you are learning about functions.")


display_message()


# 2:Favourite Book


def favourite_book(title):
    """Display message telling your favourite book"""
    print(f"One of my favourite books is {title.title()}.")


gap()
favourite_book('the secret')
favourite_book('atomic habits')

