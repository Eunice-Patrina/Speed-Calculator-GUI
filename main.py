from PyQt6.QtWidgets import (QWidget, QLabel, QGridLayout, QLineEdit, QApplication,
                             QPushButton, QComboBox)
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        hour_label = QLabel("Time(hours)")
        self.hour_line_edit = QLineEdit()

        self.metric_select = QComboBox()
        self.metric_select.addItems(["Metric(km)", "imperial(miles)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)

        grid.addWidget(self.metric_select, 0, 2)

        grid.addWidget(hour_label, 1, 0)
        grid.addWidget(self.hour_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)

    def calculate(self):
        speed = float(self.distance_line_edit.text() )/ float(self.hour_line_edit.text())

        if(self.metric_select.currentText() == "Metric(km)"):
            speed = round(speed, 2)
            unit = "km/h"
        else:
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.output_label.setText(f"Average Speed {speed} {unit}")

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())