from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Two Grids Side by Side")

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create two separate grid layouts
        grid_layout_1 = self.create_grid("Left Grid")
        grid_layout_2 = self.create_grid("Right Grid")

        # Add both grids to a horizontal layout
        h_layout = QHBoxLayout()
        h_layout.addLayout(grid_layout_1)
        h_layout.addLayout(grid_layout_2)

        # Apply the horizontal layout to the central widget
        central_widget.setLayout(h_layout)

    def create_grid(self, title: str) -> QGridLayout:
        """Creates a grid layout with a label and some buttons."""
        grid_layout = QGridLayout()

        # Add a label at the top of the grid
        label = QLabel(title)
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        label.setFixedHeight(40)
        grid_layout.addWidget(label, 0, 0, 1, 3)  # Spanning all columns

        # Add buttons to the grid
        for i in range(1, 10):
            button = QPushButton(str(i))
            row = (i - 1) // 3 + 1  # Start from row 1 to leave room for the label
            col = (i - 1) % 3
            grid_layout.addWidget(button, row, col)

        # Add a large button at the bottom spanning all columns
        zero_button = QPushButton("0")
        grid_layout.addWidget(zero_button, 4, 0, 1, 3)  # Spanning all three columns

        return grid_layout


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
