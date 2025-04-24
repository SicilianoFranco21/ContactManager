from model.contact import Contact
from model.contactList import ContactList
import os


class ConsoleView:
    @staticmethod
    def show_menu() -> None:
        print("""
==========================
     <<< CONTACTS >>>     
  [1] - Add new contact   
  [2] - Get contact       
  [3] - Get all contacts  
  [4] - Update contact    
  [5] - Delete contact    
  [6] - Exit contact      
==========================
""") 

    @staticmethod
    def request_user_option() -> int:
        while True:
            try:
                option: int = int(input("Enter an option to continue: "))
                return option
            except ValueError:
                ConsoleView.clear_console()
                print("Error: please enter a valid option (numeric value).")
                ConsoleView.show_menu()
    
    @staticmethod
    def request_contact_alias(msg: str) -> str:
        alias: str = input(f"{msg}: ")
        return alias

    @staticmethod
    def request_contact_number(msg: str) -> int | None:
        while True:
            user_input: str = input(f"{msg}: ")
            if user_input == "":
                return None
            try:
                number: int = int(user_input)
                return number
            except ValueError:
                ConsoleView.clear_console()
                print("Error: input contains non-numeric characters. Please enter only numbers.")


    @staticmethod
    def show_contact(contact: Contact) -> None:
        print(f"{contact.alias}: {contact.phone_number}")

    @staticmethod
    def show_all_contacts(contacts: list[Contact]) -> None:
        for contact in contacts:
            print(f"{contact.alias}: {contact.phone_number}")

    @staticmethod
    def display_message(msg: str) -> None:
        print(msg)

    @staticmethod
    def clear_console() -> None:
        WINDOWS: str = "nt"
        MCOS_LINUX: str = "posix"
        system = os.name
        if system == WINDOWS:  
            os.system('cls')  
        elif system == MCOS_LINUX:  
            os.system('clear')  
        else:
            print("Unsupported operating system for clearing the console.")
