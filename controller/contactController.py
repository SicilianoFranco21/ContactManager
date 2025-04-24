from model.contactList import Contact
from model.contactList import ContactList
from view.consoleView import ConsoleView


class ContactController:
    def __init__(self) -> None:
        self.model: ContactList = ContactList()

    def add_contact(self) -> None:
        alias: str = ConsoleView.request_contact_alias("Please enter a valid alias")
        number: int | None = ConsoleView.request_contact_number("Please enter a valid phone number")
        if not alias or number is None:
            ConsoleView.display_message("Alias and number cannot be empty.")
            return

        contact = Contact(alias, number)
        if self.model.add_contact(contact):
            ConsoleView.display_message("Contact was added successfully.")
            return

        ConsoleView.display_message("Contact was not added because it already exists.")

    def get_contact(self) -> None:
        alias: str = ConsoleView.request_contact_alias("Enter the alias to search for a contact")
        contact: Contact = self.model.get_contact(alias)
        if not contact:
            ConsoleView.display_message("Contact not found.")
            return

        ConsoleView.show_contact(contact)

    def get_all_contacts(self) -> None:
        all_contacts: list[Contact] = self.model.get_contacts()
        if not all_contacts:
            ConsoleView.display_message("There are no contacts yet")
            return

        ConsoleView.show_all_contacts(all_contacts)

    def update_contact(self) -> None:
        alias: str = ConsoleView.request_contact_alias("Enter the alias of the contact to update")
        new_alias: str = ConsoleView.request_contact_alias("Please enter a new alias")
        new_phone_number: int | None = ConsoleView.request_contact_number("Please enter a new phone number")
        if not new_alias or new_phone_number is None:
            ConsoleView.display_message("New alias and phone number cannot be empty.")
            return

        was_updated: bool = self.model.update_contact(alias, new_alias, new_phone_number)
        if not was_updated:
            ConsoleView.display_message("Contact was not found or updated.")
            return

        ConsoleView.display_message("Contact was updated successfully.")

    def delete_contact(self) -> None:
        alias: str = ConsoleView.request_contact_alias("Enter the alias of the contact to delete")
        was_deleted: bool = self.model.delete_contact(alias)
        if not was_deleted:
            ConsoleView.display_message("Contact could not be found for deletion.")
            return

        ConsoleView.display_message("Contact was deleted successfully.")

    def run(self) -> None:
        while True:
            ConsoleView.show_menu()
            option = ConsoleView.request_user_option()
            ConsoleView.clear_console()

            if option == 1:
                self.add_contact()

            elif option == 2:
                self.get_contact()

            elif option == 3:
                self.get_all_contacts()

            elif option == 4:
                self.update_contact()

            elif option == 5:
                self.delete_contact()

            elif option == 6:
                ConsoleView.display_message("Goodbye!")
                return

            else:
                ConsoleView.display_message("Please, enter a valid option.")
