from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton, QHBoxLayout, QDateEdit
from PyQt5.QtCore import QDate

class EditContactForm(QDialog):
    def __init__(self, contact=None, parent=None):
        super().__init__(parent)
        self.contact = contact
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add/Edit Contact")
        self.setGeometry(400, 200, 400, 300)

        layout = QFormLayout()

        self.surname_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.birthday_input = QDateEdit(self)
        self.birthday_input.setCalendarPopup(True)
        self.birthday_input.setDate(QDate(2000, 1, 1))  # Дата по умолчанию
        self.phone_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.vk_input = QLineEdit(self)

        layout.addRow("Surname:", self.surname_input)
        layout.addRow("Name:", self.name_input)
        layout.addRow("Birthday:", self.birthday_input)
        layout.addRow("Phone:", self.phone_input)
        layout.addRow("E-mail:", self.email_input)
        layout.addRow("vk.com:", self.vk_input)

        # Логируем для отладки
        print(f"Инициализация формы. Контакт передан: {self.contact}")

        # Проверяем, если контакт передан, заполняем поля данными контакта
        if self.contact:
            print(f"Заполняем форму данными контакта: {self.contact}")
            self.surname_input.setText(self.contact.last_name)
            self.name_input.setText(self.contact.first_name)
            self.birthday_input.setDate(QDate.fromString(self.contact.birth_date, 'yyyy-MM-dd'))
            self.phone_input.setText(self.contact.phone)
            self.email_input.setText(self.contact.email)
            self.vk_input.setText(self.contact.vk_id)
        else:
            # Логируем, что контакт не передан (новый контакт)
            print("Контакт не передан, создается новый контакт.")
            # Оставляем поля пустыми для нового контакта
            self.surname_input.clear()
            self.name_input.clear()
            self.birthday_input.setDate(QDate(2000, 1, 1))  # Дата по умолчанию
            self.phone_input.clear()
            self.email_input.clear()
            self.vk_input.clear()

        # Кнопки OK и Cancel
        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel", self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addRow(button_layout)

        self.setLayout(layout)

    def get_contact_data(self):
        """Возвращаем данные контакта из формы."""
        contact_data = {
            'last_name': self.surname_input.text(),
            'first_name': self.name_input.text(),
            'birth_date': self.birthday_input.date().toString('yyyy-MM-dd'),
            'phone': self.phone_input.text(),
            'email': self.email_input.text(),
            'vk_id': self.vk_input.text(),
        }
        print(f"Данные контакта из формы: {contact_data}")  # Логирование для отладки
        return contact_data
