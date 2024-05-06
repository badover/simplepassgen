import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pass Gen By youngt1m")
        layout = QVBoxLayout(self)
        
        self.password_field = QLineEdit(self)
        layout.addWidget(self.password_field)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(6)
        self.slider.setMaximum(20)
        layout.addWidget(self.slider)
        
        generate_button = QPushButton("Generate password", self)
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)

    def generate_password(self):
        length = self.slider.value()
        password = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()') for _ in range(length))
        self.password_field.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
