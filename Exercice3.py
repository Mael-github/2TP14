from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("Charging...")

        icon = QIcon("C:\Documents\PyCharm Projects\i57h6bid9hud67.png")
        layout = QGridLayout()
        label = QLabel("Hello")
        Bardeprogression = QProgressBar()
        ligne = QLineEdit()
        bouton = QPushButton("Try to click here :)")

        layout.addWidget(label)
        layout.addWidget(Bardeprogression)
        layout.addWidget(ligne)
        layout.addWidget(bouton)

        Bardeprogression.setValue(50)
        bouton.setToolTip("Maybe there")
        self.setWindowIcon(icon)
        label.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

if __name__ == "__main__":
   app = QApplication([])
   window = Window()
   window.show()
   app.exec_()
