from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QSpinBox

app = QApplication([])
mainWidget = QWidget()

layout = QVBoxLayout()

label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
button2 = QPushButton("Ceci est un deuxième QPushButton")

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(button2)

mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()
