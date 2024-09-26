import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMessageBox
from ContactApp.contact import Contact
from ContactApp.contact_manager import ContactManager
from ContactApp.serializer import Serializer

class ContactAppUI(QWidget):
    """
    Main window for the ContactApp user interface.
    """

    def __init__(self):
        """
        Initializes the ContactApp UI and displays contact information.
        """
        super().__init__()

        self.setWindowTitle("ContactAppUI")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.manager = ContactManager()

        try:
            # Создаем объекты для сериализации
            contact1 = Contact("Alice", "12345")
            contact2 = Contact("Bob", "54321")
            self.manager.add_contact(contact1)
            self.manager.add_contact(contact2)

            # Подготавливаем данные для сериализации
            data = {
                "contacts": [
                    {"name": contact1.name, "phone": contact1.phone},
                    {"name": contact2.name, "phone": contact2.phone}
                ]
            }

            # Сохраняем данные в файл
            Serializer.save_to_file(data, "contacts.json")

            # Загружаем данные из файла
            loaded_data = Serializer.load_from_file("contacts.json")

            # Выводим загруженные данные
            loaded_contacts = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in loaded_data['contacts']])
            label = QLabel(f"Loaded Contacts:\n{loaded_contacts}", self)
            layout.addWidget(label)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactAppUI()
    window.show()
    sys.exit(app.exec_())
