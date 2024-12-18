import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e): #type: ignore
        context = QMenu(self)
        context.addAction(QAction("Hallo", self))
        context.addAction(QAction("DUHU", self))
        context.addAction(QAction("HELP", self))
        context.addAction(QAction("QUIT", self))

        context.exec(e.globalPos())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
