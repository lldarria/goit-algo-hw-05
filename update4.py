def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Give me name and phone please."
        except KeyError:
            return "Error: The specified contact does not exist."
        except IndexError:
            return "Error: Not enough arguments provided. Please provide both name and phone number."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args  # Якщо аргументів не вистачає, буде ValueError
    contacts[name] = phone
    return f"Contact '{name}' added."


@input_error
def change_contact(args, contacts):
    name, phone = args  # Якщо аргументів не вистачає, буде ValueError
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated with new phone number."
    else:
        raise KeyError  # Якщо контакту немає, генеруємо KeyError


@input_error
def get_phone(args, contacts):
    name = args[0]  # Якщо аргументів не вистачає, буде IndexError
    return contacts[name]  # Якщо контакту немає, буде KeyError


@input_error
def get_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


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


if __name__ == "__main__":
    main()
