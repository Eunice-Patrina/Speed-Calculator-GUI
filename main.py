from PyQt6.QtWidgets import (QWidget, QLabel, QGridLayout, QLineEdit, QApplication,
                             QPushButton, QComboBox)
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        hour_label = QLabel("Time(hours)")
        self.hour_line_edit = QLineEdit()

        metric_select = QComboBox()
        metric_select.addItems(["Metric(km)", "imperial(miles)"])
        self.selected_unit = metric_select.currentText()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)

        grid.addWidget(metric_select, 0, 2)

        grid.addWidget(hour_label, 1, 0)
        grid.addWidget(self.hour_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)

    def calculate(self):
        speed = float(self.distance_line_edit.text() )/ float(self.hour_line_edit.text())
        self.output_label.setText(f"Average Speed {speed} {self.selected_unit}")

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())