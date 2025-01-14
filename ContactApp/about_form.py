from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class AboutForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("ContactsApp v1.0"))
        layout.addWidget(QLabel("Приложение для твоих контактова"))
        self.setLayout(layout)
