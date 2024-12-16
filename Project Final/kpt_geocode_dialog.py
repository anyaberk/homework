import os
from qgis.PyQt import QtGui, uic, QtWidgets
from qgis.PyQt.QtCore import pyqtSignal, Qt
from qgis.gui import QgsFileWidget
from PyQt5 import QtWidgets


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'kpt_geocode_dialog.ui'))


class kptGeocodeDialog(QtWidgets.QDialog, FORM_CLASS):
    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(kptGeocodeDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.get_data)

    def get_data(self):
        csv_input = self.findChild(QgsFileWidget, 'csv_input').filePath()
        key = self.findChild(QtWidgets.QLineEdit, 'api_key').text()
        geocoding_csv = self.findChild(QgsFileWidget, 'geocoding_output').filePath()

        return {
            'csv_input': csv_input,
            'api_key': key,
            'geocoding_output': geocoding_csv
        }

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
