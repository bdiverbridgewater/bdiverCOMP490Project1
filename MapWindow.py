import io
from PySide6.QtWidgets import QWidget, QVBoxLayout
import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster


class Comp490MapWindow(QWidget):
    def __init__(self, data_to_display):
        super().__init__()
        self.data_to_display = data_to_display
        self.map = self.build_map()
        self.setup_window()

    def setup_window(self):
        self.layout = QVBoxLayout(self)
        self.webview = QWebEngineView()

        self.webview.setHtml(self.map.getvalue().decode("utf-8"))
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        self.resize(800, 800)
        self.show()

    def build_map(self):
        """Initial demo a mangling of this answer from stackoverflow
                        https://stackoverflow.com/questions/58590199/how-to-show-folium-map-inside-a-pyqt5-gui"""
        # what a terrible variable name - I might have to cite myself in a future class

        address = 'Brockton, MA'
        geolocator = Nominatim(user_agent="BDiverCOMP490BSU")
        bos_location = geolocator.geocode(address)
        temp_demo_map = folium.Map(
            location=[bos_location.latitude, bos_location.longitude], zoom_start=13
        )
        in_memory_file = io.BytesIO()
        # modified from folium docs
        # https://python-visualization.github.io/folium/latest/user_guide/plugins/marker_cluster.html
        map_data_markers = MarkerCluster().add_to(temp_demo_map)
        for data in self.data_to_display:
            job_location = data[3]
            job_company = data[2]
            job_loc_geocoded = geolocator.geocode(job_location, timeout=100)
            # this might need try/catch for small towns
            if job_loc_geocoded is not None:
                folium.Marker(
                    location=[job_loc_geocoded.latitude, job_loc_geocoded.longitude],
                    popup=job_company
                ).add_to(map_data_markers)
        temp_demo_map.save(in_memory_file, close_file=False)
        return in_memory_file
