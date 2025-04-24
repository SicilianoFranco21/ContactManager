from unittest import TestCase, main
from model.contactList import Contact, ContactList


class TestContactList(TestCase):

    def setUp(self) -> None:
        """Sets up a new contact list before each test"""
        self.contact_list: ContactList = ContactList()
        self.contact1: Contact = Contact("John Doe", 123456789)
        self.contact2: Contact = Contact("Jane Doe", 987654321)
        self.contact_list.add_contact(self.contact1)
        self.contact_list.add_contact(self.contact2)

    def test_add_contact(self) -> None:
        """Checks if a new contact can be added"""
        contact3: Contact = Contact("Alice", 555555555)
        result: bool = self.contact_list.add_contact(contact3)
        self.assertTrue(result)

    def test_add_existing_contact(self) -> None:
        """Checks that a duplicate contact cannot be added"""
        result: bool = self.contact_list.add_contact(self.contact1)
        self.assertFalse(result)

    def test_get_contacts(self) -> None:
        """Checks if all contacts are returned correctly"""
        contacts: list[Contact] = self.contact_list.get_contacts()
        self.assertEqual(contacts, [self.contact1, self.contact2])

    def test_update_contact(self) -> None:
        """Checks if alias and phone number can be updated"""
        result: bool = self.contact_list.update_contact("John Doe", new_alias="Johnny", new_phone_number=111111111)
        self.assertTrue(result)

    def test_update_contact_not_found(self) -> None:
        """Checks that an update fails if the contact is not found"""
        result: bool = self.contact_list.update_contact("Nonexistent", new_alias="New Name", new_phone_number=222222222)
        self.assertFalse(result)

    def test_delete_contact(self) -> None:
        """Checks if a contact can be deleted"""
        result: bool = self.contact_list.delete_contact("John Doe")
        self.assertTrue(result)

    def test_delete_contact_not_found(self) -> None:
        """Checks that deletion fails if the contact is not found"""
        result: bool = self.contact_list.delete_contact("Nonexistent")
        self.assertFalse(result)

    def test_get_contact(self) -> None:
        """Checks if a contact can be retrieved by alias"""
        contact: Contact | None = self.contact_list.get_contact("John Doe")
        self.assertEqual(contact, self.contact1)

    def test_get_contact_not_found(self) -> None:
        """Checks that None is returned if the contact is not found"""
        contact: Contact | None = self.contact_list.get_contact("SomeRandomName")
        self.assertEqual(contact, None)

    def test_add_contact_after_deletion(self) -> None:
        """Checks if a deleted contact can be added again"""
        self.contact_list.delete_contact("John Doe")
        result: bool = self.contact_list.add_contact(self.contact1)
        self.assertTrue(result)

    def test_delete_contact_twice(self) -> None:
        """Checks that deleting the same contact twice fails the second time"""
        self.contact_list.delete_contact("John Doe")
        result: bool = self.contact_list.delete_contact("John Doe")
        self.assertFalse(result)

    def test_update_contact_only_alias(self) -> None:
        """Checks that only the alias can be updated when phone number is unchanged"""
        result: bool = self.contact_list.update_contact("John Doe", new_alias="Johnny", new_phone_number=None)
        self.assertTrue(result)

    def test_update_contact_only_phone_number(self) -> None:
        """Checks that only the phone number can be updated when alias is unchanged"""
        result: bool = self.contact_list.update_contact("John Doe", new_alias=None, new_phone_number=111111111)
        self.assertTrue(result)


if __name__ == '__main__':
    main(verbosity=2)
