import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from ContactApp.logic import ContactManager, Contact  # Импортируем классы из логики

class ContactAppUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ContactAppUI")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Использование логики классов
        manager = ContactManager()
        manager.add_contact(Contact("Alice", "123456"))
        manager.add_contact(Contact("Bob", "654321"))

        label = QLabel(manager.list_contacts(), self)
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactAppUI()
    window.show()
    sys.exit(app.exec_())
