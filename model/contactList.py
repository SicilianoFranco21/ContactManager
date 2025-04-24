from model.contact import Contact


class ContactList:
    def __init__(self) -> None:
        self._contacts: list[Contact] = []

    @property
    def contacts(self) -> list[Contact]:
        return self._contacts

    def add_contact(self, contact: Contact) -> bool:
        if contact in self._contacts:
            return False
        self._contacts.append(contact)
        return True

    def get_contact(self, alias: str) -> Contact | None:
        for contact in self._contacts:
            if contact.alias == alias:
                return contact

    def get_contacts(self) -> list[Contact]:
        return self._contacts

    def update_contact(self, alias: str, new_alias: str | None, new_phone_number: int | None) -> bool:
        updated: bool = False
        for contact in self._contacts:
            if contact.alias == alias:
                if (new_alias is not None) and (contact.alias != new_alias):
                    contact.alias = new_alias
                    updated = True
                if (new_phone_number is not None) and (contact.phone_number != new_phone_number):
                    contact.phone_number = new_phone_number
                    updated = True
                return updated
        return updated

    def delete_contact(self, alias: str) -> bool:
        for contact in self._contacts:
            if contact.alias == alias:
                self._contacts.remove(contact)
                return True
        return False
