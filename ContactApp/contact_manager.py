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
        return self._contacts  # Возвращаем список контактов

    # Метод для поиска контакта по фамилии
    def get_contact_by_name(self, last_name):
        for contact in self._contacts:
            if contact.last_name.lower() == last_name.lower():
                return contact
        return None

    # Метод для удаления контакта
    def remove_contact(self, last_name):
        contact_to_remove = self.get_contact_by_name(last_name)
        if contact_to_remove:
            self._contacts.remove(contact_to_remove)
            return True
        return False

    # Метод для редактирования контакта
    def edit_contact(self, old_last_name, new_contact):
        contact_to_edit = self.get_contact_by_name(old_last_name)
        if contact_to_edit:
            contact_to_edit.first_name = new_contact.first_name
            contact_to_edit.last_name = new_contact.last_name
            contact_to_edit.phone = new_contact.phone
            contact_to_edit.email = new_contact.email
            contact_to_edit.birth_date = new_contact.birth_date
            contact_to_edit.vk_id = new_contact.vk_id
            return True
        return False

    # Свойство для получения количества контактов
    @property
    def contact_count(self):
        return len(self._contacts)
