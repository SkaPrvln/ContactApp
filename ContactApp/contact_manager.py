from ContactApp.contact import Contact

class ContactManager:
    def __init__(self):
        self._contacts = []  # Приватное поле для хранения списка контактов

    # Метод для добавления контакта
    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise TypeError("Can only add instances of Contact class.")
        self._contacts.append(contact)

    # Метод для вывода всех контактов
    def list_contacts(self):
        if not self._contacts:
            return "No contacts available."
        return "\n".join(str(contact) for contact in self._contacts)

    # Свойство для получения количества контактов
    @property
    def contact_count(self):
        return len(self._contacts)
