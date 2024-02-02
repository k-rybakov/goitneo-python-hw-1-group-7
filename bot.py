def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_phone(args, contacts):
    return contacts.get(args[0], "Contact not found")

def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found"

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            continue
        
        num_args = len(args)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if num_args == 2:
                print(add_contact(args, contacts))
            else:
                print('Error: please enter space separated name and phone command')
        elif command == "change":
            if num_args == 2:
                print(change_contact(args, contacts))
            else:
                print('Error: please enter space separated name and phone command')
        elif command == "phone":
            if num_args == 0:
                print('Error: please enter name')
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()