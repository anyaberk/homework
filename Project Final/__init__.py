from PyQt5.QtWidgets import QAction, QMessageBox


def classFactory(iface):
    from .kpt_geocode import KptGeocodePlugin
    return KptGeocodePlugin(iface)


