from model.contact import Contact
from unittest import TestCase, main


class TestContact(TestCase):
    def setUp(self) -> None:
        """Creates three Contact instances for testing"""
        self.c1: Contact = Contact("Test_1", 111111)
        self.c2: Contact = Contact("Test_1", 111111)
        self.c3: Contact = Contact("Test_2", 222222)

    def test_equal_contacts(self) -> None:
        """Checks that two contacts with same alias and phone number are equal"""
        self.assertEqual(self.c1, self.c2)

    def test_different_contacts(self) -> None:
        """Checks that contacts with different alias or phone number are not equal"""
        self.assertNotEqual(self.c1, self.c3)

    def test_str_representation(self) -> None:
        """Checks the string representation of a contact (__str__)"""
        expected: str = "Test_1 - 111111"
        self.assertEqual(str(self.c1), expected)

    def test_repr_representation(self) -> None:
        """Checks the official representation of a contact (__repr__)"""
        expected: str = "Contact('Test_1', 111111)"
        self.assertEqual(repr(self.c1), expected)


if __name__ == "__main__":
    main(verbosity=2)
