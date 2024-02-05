"""Tools for working with functions and callable objects"""

from functools import wraps


def input_error(func):
    """input_error Decorator to handle input errors.
    This decorator wraps a function and catches any `ValueError`
    that may occur during its execution. If a `ValueError` is caught,
    it returns the message "Give me name and phone please."
    :param func:  The function to decorate.
    :type func: callable
    :return:  The decorated function.
    :rtype: callable
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "No contacts saved. First you need to add at least one contact"
        except KeyError:
            return "No person unders such name/nickname"

    return inner


@input_error
def parse_input(user_input: str) -> tuple[str, *tuple[str, ...]]:
    """parse_input Parses the user input and extracts the command and arguments.
    :param  user_input: The user input string.
    :type args: tuple
    :return: A tuple containing the command and arguments.
    :rtype: tuple[str, *tuple[str, ...]]
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: tuple, contacts: dict) -> str:
    """add_contact This code defines a function called add_contact that takes two
    arguments: args and contacts. The function adds a new contact to the contacts
    dictionary using the name and phone number provided in args.It then returns
    the string "Contact added."

    :param args:  A tuple containing the name and phone number.
    :type args: tuple
    :param contacts: A dictionary of contacts where the contact will be added.
    :type contacts: dict
    :return: A success message indicating that the contact has been added.
    :rtype: str
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: tuple, contacts: dict) -> str:
    """change_contact Change the contact phone number in the contacts dictionary.

     :param args:  A tuple containing the name and new phone number.
     :type args: tuple
     :param contacts: A dictionary of contacts where the phone number will be updated.
    :type contacts: dict
     :return: A success message indicating that the contact has been changed.
     :rtype: str
    """
    name, phone = args
    contacts[name] = phone
    return "Success! Contact changed"


@input_error
def get_contact(args: tuple, contacts: dict) -> str:
    """get_contact Get a contact from the contacts dictionary.

    :param args: A tuple containing the arguments to retrieve the contact.
    :type args: tuple
    :param contacts: A dictionary containing the contacts.
    :type contacts: dict
    :return: The contact information for the specified arguments.
    :rtype: str
    """
    return contacts[args[0]]


def main():
    """main This code defines a main function that serves as the entry point of a program.
    It creates an empty contacts dictionary and then enters a loop to interact with the user.
    The user can enter different commands, and the program responds accordingly."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Goodbye!")
                break

            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(get_contact(args, contacts))
            case "all":
                if not contacts:
                    print("No saved contacts, wanna add some?")
                else:
                    print(contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
