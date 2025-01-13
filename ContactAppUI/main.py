import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QListWidget, QLabel, QLineEdit, QMessageBox,
                             QInputDialog, QMenuBar, QAction, QFormLayout, QDateEdit, QDialog, QMainWindow)
from PyQt5.QtCore import QDate
from ContactApp.contact import Contact
from ContactApp.contact_manager import ContactManager
from ContactApp.serializer import Serializer
from ContactApp.edit_form import EditContactForm


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contact_manager = ContactManager()  # Используем ContactManager для управления контактами
        self.init_ui()
        self.load_contacts()

    def init_ui(self):
        self.setWindowTitle("ContactsApp")
        self.setGeometry(100, 100, 800, 600)

        # Создание меню
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")

        # Пункты меню File
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Пункты меню Edit
        add_action = QAction("Add Contact", self)
        add_action.triggered.connect(self.add_contact)
        edit_action = QAction("Edit Contact", self)
        edit_action.triggered.connect(self.edit_contact)
        remove_action = QAction("Remove Contact", self)
        remove_action.triggered.connect(self.remove_contact)

        edit_menu.addAction(add_action)
        edit_menu.addAction(edit_action)
        edit_menu.addAction(remove_action)

        # Пункт меню Help
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

        # Основная часть окна
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout(main_widget)

        # Левая панель со списком контактов и поиском
        left_panel = QVBoxLayout()

        # Поисковое поле
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Find:")
        self.search_input.textChanged.connect(self.search_contacts)
        left_panel.addWidget(self.search_input)

        # Список контактов
        self.contacts_list = QListWidget(self)
        self.contacts_list.itemClicked.connect(self.display_contact)
        left_panel.addWidget(self.contacts_list)

        # Кнопки управления контактами (добавить, редактировать, удалить)
        button_layout = QHBoxLayout()

        self.add_button = QPushButton("+", self)
        self.add_button.clicked.connect(self.add_contact)
        button_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edit", self)
        self.edit_button.clicked.connect(self.edit_contact)
        button_layout.addWidget(self.edit_button)

        self.remove_button = QPushButton("-", self)
        self.remove_button.clicked.connect(self.remove_contact)
        button_layout.addWidget(self.remove_button)

        left_panel.addLayout(button_layout)
        layout.addLayout(left_panel)

        # Правая панель с подробной информацией о контакте
        right_panel = QFormLayout()

        self.surname_label = QLineEdit(self)
        self.name_label = QLineEdit(self)
        self.birthday_label = QDateEdit(self)
        self.birthday_label.setCalendarPopup(True)
        self.birthday_label.setDate(QDate(2000, 1, 1))
        self.phone_label = QLineEdit(self)
        self.email_label = QLineEdit(self)
        self.vk_label = QLineEdit(self)

        right_panel.addRow("Surname:", self.surname_label)
        right_panel.addRow("Name:", self.name_label)
        right_panel.addRow("Birthday:", self.birthday_label)
        right_panel.addRow("Phone:", self.phone_label)
        right_panel.addRow("E-mail:", self.email_label)
        right_panel.addRow("vk.com:", self.vk_label)

        layout.addLayout(right_panel)

        #Кнопка сохранения для сохранения изменений на панели справо
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_current_contact)
        right_panel.addRow("", self.save_button)

    def load_contacts(self):
        """Загрузка контактов из файла JSON"""
        try:
            contacts_data = Serializer.load_from_file(self.get_file_path())
            for contact_data in contacts_data['contacts']:
                contact = Contact(**contact_data)  # Передаем данные через **kwargs
                self.contact_manager.add_contact(contact)
                self.contacts_list.addItem(contact.last_name)
        except Exception as e:
            print(f"Error loading contacts: {e}")

    def save_contacts(self):
        """Сохранение контактов в JSON"""
        contacts_data = {
            "contacts": [contact.__dict__ for contact in self.contact_manager.list_contacts()]
        }
        Serializer.save_to_file(contacts_data, self.get_file_path())

    def get_file_path(self):
        """Получить путь к файлу JSON в папке My Documents"""
        return os.path.join(os.path.expanduser('~'), 'Documents', 'ContactsApp.json')

    def add_contact(self):
        """Добавление нового контакта"""
        try:
            # Создаем форму для добавления контакта
            form = EditContactForm(parent=self)

            # Если пользователь нажимает OK, получаем данные контакта
            if form.exec_() == QDialog.Accepted:
                # Получаем данные контакта из формы
                contact_data = form.get_contact_data()

                # Выводим данные для отладки
                print(f"Contact data: {contact_data}")

                try:
                    # Создаем новый объект контакта из полученных данных
                    new_contact = Contact(**contact_data)
                    # Добавляем контакт в менеджфффер контактов
                    self.contact_manager.add_contact(new_contact)
                    # Добавляем фамилию нового контакта в список контактов
                    self.contacts_list.addItem(new_contact.last_name)
                    # Сохраняем контакты в файл
                    self.save_contacts()
                except ValueError as e:
                    QMessageBox.warning(self, "Invalid Input", str(e))
        except Exception as e:
            # Ловим все возможные исключения и выводим сообщение об ошибке
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")

    def edit_contact(self):
        """Редактирование выбранного контакта"""
        selected_item = self.contacts_list.currentItem()
        if selected_item:
            # Ищем контакт по фамилии (или другому ключевому полю)
            contact = self.contact_manager.get_contact_by_name(selected_item.text())
            if contact:
                # Создаем форму редактирования с данными контакта
                form = EditContactForm(contact, self)
                # Если пользователь нажимает OK в форме редактирования
                if form.exec_() == QDialog.Accepted:
                    # Получаем обновленные данные контакта из формы
                    updated_data = form.get_contact_data()
                    try:
                        # Создаем новый объект контакта с обновленными данными
                        updated_contact = Contact(**updated_data)
                        # Обновляем контакт в менеджере
                        self.contact_manager.edit_contact(contact.last_name, updated_contact)
                        # Обновляем отображение информации о контакте
                        self.display_contact(selected_item)
                        # Сохраняем изменения
                        self.save_contacts()
                    except ValueError as e:
                        QMessageBox.warning(self, "Invalid Input", str(e))

    def remove_contact(self):
        """Удаление контакта"""
        selected_item = self.contacts_list.currentItem()
        if selected_item:
            reply = QMessageBox.question(self, 'Confirm',
                                         f"Do you really want to remove this contact: {selected_item.text()}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if self.contact_manager.remove_contact(selected_item.text()):
                    self.contacts_list.takeItem(self.contacts_list.row(selected_item))
                    self.clear_contact_info()
                    self.save_contacts()

    def display_contact(self, item):
        """Отображение информации о контакте"""
        contact = self.contact_manager.get_contact_by_name(item.text())
        if contact:
            self.surname_label.setText(contact.last_name)
            self.name_label.setText(contact.first_name)
            self.phone_label.setText(contact.phone)
            self.email_label.setText(contact.email)
            self.vk_label.setText(contact.vk_id)
            self.birthday_label.setDate(QDate.fromString(contact.birth_date, 'yyyy-MM-dd'))

    def clear_contact_info(self):
        """Очищаем поля информации о контакте"""
        self.surname_label.clear()
        self.name_label.clear()
        self.phone_label.clear()
        self.email_label.clear()
        self.vk_label.clear()
        self.birthday_label.setDate(QDate(2000, 1, 1))

    def search_contacts(self):
        """Поиск контактов"""
        search_text = self.search_input.text().lower()
        self.contacts_list.clear()
        for contact in self.contact_manager.list_contacts():
            if search_text in contact.last_name.lower() or search_text in contact.first_name.lower():
                self.contacts_list.addItem(contact.last_name)

    def show_about_dialog(self):
        """Открываем окно About"""
        QMessageBox.about(self, "About ContactsApp", "ContactsApp v1.0\nManage your contacts with ease.")

    def save_current_contact(self):
        selected_item = self.contacts_list.currentItem()
        if not selected_item:
            return

        contact = self.contact_manager.get_contact_by_name(selected_item.text())
        if not contact:
            return

        try:
            # Применяем валидацию из вашего класса Contact
            contact.last_name = self.surname_label.text()
            contact.first_name = self.name_label.text()
            # телефон, дата, имейл и т.д. тоже через сеттеры или через новый Contact(**updated_data)
            contact.phone = contact.validate_phone(self.phone_label.text())
            contact.birth_date = contact.validate_birth_date(
                self.birthday_label.date().toString("yyyy-MM-dd")
            )
            contact.email = contact.validate_email(self.email_label.text())
            contact.vk_id = self.vk_label.text()

            # Сохраняем
            self.save_contacts()
            QMessageBox.information(self, "Success", "Contact updated successfully.")
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Input", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
