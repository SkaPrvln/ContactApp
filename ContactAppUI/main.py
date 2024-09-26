import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class ContactAppUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ContactAppUI")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        label = QLabel("Hello, this is your ContactApp UI!", self)
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactAppUI()
    window.show()
    sys.exit(app.exec_())
