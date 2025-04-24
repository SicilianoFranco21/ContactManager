class Contact:
    def __init__(self, alias: str, phone_number: int) -> None:
        self._alias = alias
        self._phone_number = phone_number
    
    @property
    def alias(self) -> str:
        return self._alias

    @alias.setter
    def alias(self, new_alias: str) -> None:
        self._alias = new_alias
    
    @property
    def phone_number(self) -> int:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number: str) -> None:
        self._phone_number = new_phone_number
    
    def __eq__(self, other: 'Contact') -> bool:
        if isinstance(other, Contact):
            return self.alias == other.alias and self.phone_number == other.phone_number
        return False
    
    def __str__(self) -> str:
        return f"{self.alias} - {self.phone_number}"
    
    def __repr__(self) -> str:
        return f"Contact('{self.alias}', {self.phone_number})"