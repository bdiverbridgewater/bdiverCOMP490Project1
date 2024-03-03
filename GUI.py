import sys
from FirstWindow import FirstWindow
import PySide6.QtWidgets
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface


def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = FirstWindow(data)
    assert my_window is not None
    sys.exit(qt_app.exec())


def start_gui(data):
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.Software)
    display_data(data)
