class Project:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_all_contacts(self):
        return self.contacts

    def get_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
