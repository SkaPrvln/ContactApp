from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class EditForm(QWidget):
    def __init__(self, contact=None, parent=None):
        super().__init__(parent)
        self.contact = contact
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First Name")
        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Last Name")
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.last_name_input)

        # Добавим поля для остальных данных контакта (номер телефона, email и т.д.)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_contact)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_contact(self):
        # Логика для сохранения данных контакта
        pass
