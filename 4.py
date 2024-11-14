def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Please provide both a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Please provide both a name and a new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated with new phone number."
    else:
        return f"Error: Contact '{name}' not found."

def get_phone(args, contacts):
    if len(args) < 1:
        return "Error: Please provide a contact name."
    name = args[0]
    return contacts.get(name, f"Error: Contact '{name}' not found.")

def get_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "The specified contact does not exist."
        except IndexError:
            return "Not enough arguments provided. Please provide both name and phone number."
    return inner
    
contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args=None):
    if not contacts:
        return "No contacts available."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
 
if __name__ == "__main__":
    main()

