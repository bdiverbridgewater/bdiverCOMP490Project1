from PySide6.QtWidgets import QWidget, QLabel, QLineEdit


class Comp490DataDemoWindow(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Job")
        self.setGeometry(750, 100, 900, 200)  # put the new window next to the original one wider than it is tall
        label = QLabel(self)
        label.setText("Job Title:")
        label.move(50, 50)
        job_title = QLineEdit(self.data[1], self)
        job_title.move(120, 50)
        label = QLabel("Company:", self)
        label.move(50, 100)
        company = QLineEdit(str(self.data[2]), self)
        company.move(120, 100)
        label = QLabel("Location:", self)
        label.move(250, 100)
        location = QLineEdit(str(self.data[3]), self)
        location.move(330, 100)
        label = QLabel("Description:", self)
        label.move(460, 100)
        description = QLineEdit(str(self.data[4]), self)
        description.move(540, 100)
        label = QLabel("Related Link:", self)
        label.move(670, 100)
        related_link = QLineEdit(str(self.data[5]), self)
        related_link.move(750, 100)
        label = QLabel("Work From Home:", self)
        label.move(880, 100)
        related_link = QLineEdit(str(self.data[5]), self)
        related_link.move(960, 100)
