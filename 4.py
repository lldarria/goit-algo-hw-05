def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

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
def add_contact(args):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_contact(args):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated with new phone number."
    else:
        return f"Error: Contact '{name}' not found."

@input_error
def get_phone(args):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def get_all_contacts():
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
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
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(get_phone(args))
        elif command == "all":
            print(get_all_contacts())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

