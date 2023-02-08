# Passing a List


def greet_users(names):
    """Print a simple greeting to users in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


users = ['riley', 'hannah', 'strew', 'andrew']
greet_users(users)
print('\n')

# Modifying a List in a Function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for model in completed_models:
    print("\t" + model)  # or print(f"\t{model}")


def print_models(unprinted_models, completed_designs):
    """
    Simulate printing each design, until none are left.
    Move each design ti completed_models after printing.
    """
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print('\nThe following models have been printed:')
    for model in completed_models:
        print(f"\t{model}")


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print('\n')

# Preventing a Function from Modifying a List
unread_subjects = ['history', 'geography', 'hindi', 'phy edu']
completed_subjects = []
print_models(unread_subjects[:], completed_subjects)
print(unread_subjects)
print('\n')


# DO IT YOURSELF
# 1:Messages


def show_messages(list):
    """Display the messages"""
    print('The following messages are sent:')
    for message in messages:
        print(message)


messages = ['hi, how are you', "can't talk now", "i'll call you later", 'send me pics asap']
show_messages(messages)


# 2:Sending Messages


def send_messages(list, send_list):
    """Display sent messages and move them to sent folder"""
    print('\nThe following messages are being moved in sent messages:')
    while list:
        current_message = list.pop()
        print(f"Send message: {current_message}")
        send_list.append(current_message)


sent_messages = []
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)
print('\n')


# 3:Archived Messages
messages = ['hi, how are you', "can't talk now", "i'll call you later", 'send me pics asap']
archived_messages = messages[:]
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
