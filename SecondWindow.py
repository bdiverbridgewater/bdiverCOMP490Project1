from PySide6.QtWidgets import QWidget, QLabel, QLineEdit


class Comp490DataDemoWindow(QWidget):

    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Job")
        self.setGeometry(750, 200, 900, 400)  # put the new window next to the original one wider than it is tall
        label = QLabel("Job ID:", self)
        label.move(50, 0)
        job_id = QLineEdit(self.data[0], self)
        job_id.move(300, 0)
        label = QLabel(self)
        label.setText("Job Title:")
        label.move(50, 30)
        job_title = QLineEdit(self.data[1], self)
        job_title.move(300, 30)
        label = QLabel("Company:", self)
        label.move(50, 60)
        company = QLineEdit(str(self.data[2]), self)
        company.move(300, 60)
        label = QLabel("Location:", self)
        label.move(50, 90)
        location = QLineEdit(str(self.data[3]), self)
        location.move(300, 90)
        label = QLabel("Description:", self)
        label.move(50, 120)
        description = QLineEdit(str(self.data[4]), self)
        description.move(300, 120)
        label = QLabel("Related Link:", self)
        label.move(50, 150)
        related_link = QLineEdit(str(self.data[5]), self)
        related_link.move(300, 150)
        label = QLabel("Work From Home:", self)
        label.move(50, 180)
        work_from_home = QLineEdit(str(self.data[6]), self)
        work_from_home.move(300, 180)
        label = QLabel("Time Since Posting:", self)
        label.move(50, 210)
        time_since_posting = QLineEdit(self.data[7], self)
        time_since_posting.move(300, 210)
        label = QLabel("Minimum Salary:", self)
        label.move(50, 240)
        minimum_salary = QLineEdit(str(self.data[8]), self)
        minimum_salary.move(300, 240)
        label = QLabel("Maximum Salary:", self)
        label.move(50, 270)
        maximum_salary = QLineEdit(str(self.data[9]), self)
        maximum_salary.move(300, 270)
