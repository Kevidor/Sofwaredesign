from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calc_buttons = {1:"1", 2:"2", 3:"3", 4:"+", 5:"4", 6:"5", 7:"6", 8:"-", 9:"7", 10:"8", 11:"9", 12:"*", 13:"0", 14:".", 15:"=", 16:"/"}
        self.result = 0
        self.string_buffer = ""

        self.setWindowTitle("Calc stands for Calculator. I'm using slang")

        # Create and set layout
        layout = QGridLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)  

        # Create widgets
        self.label = QLabel("Kevkev's own Calc")
        layout.addWidget(self.label, 0, 0, 1, 3)

        #Create Calc Buttons
        for i in self.calc_buttons:
            button = QPushButton(str(self.calc_buttons[i]))
            button.setFixedSize(50, 50)
            button.clicked.connect(self.button_clicked)
            row = ((i - 1) // 4) + 1
            col = (i - 1) % 4
            layout.addWidget(button, row, col)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_clicked(self):
        clicked_button = self.sender()
        button_text = clicked_button.text() # type: ignore
        if button_text == "=":
            self.result = eval(self.string_buffer)
            self.string_buffer = str(self.result)
            self.label.setText(str(self.result))
        else:
            self.string_buffer += str(button_text)
            self.label.setText(self.string_buffer)

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
