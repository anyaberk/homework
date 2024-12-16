from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import QgsMessageLog, Qgis
from qgis.gui import QgsFileWidget
from PyQt5 import QtWidgets



from .kpt_geocode_dialog import kptGeocodeDialog


class KptGeocodePlugin:

  def __init__(self, iface):
    self.iface = iface
    self.pluginIsActive = False

  def initGui(self):
    self.action = QAction("KPT Geocode plugin",
                          self.iface.mainWindow())
    self.action.setObjectName("testAction")
    self.action.setWhatsThis("Configuration for geocoding plugin")
    self.action.setStatusTip("This is status tip")
    self.action.triggered.connect(self.run)


    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("KPT Geocode plugin", self.action)


  def unload(self):
    self.iface.removePluginMenu("KPT Geocode plugin", self.action)
    self.iface.removeToolBarIcon(self.action)

  def run(self):
    self.pluginIsActive = True
    self.pluginDialog = kptGeocodeDialog()
    self.pluginDialog.csv_input.setFilter("CSV (*.csv)")
    self.pluginDialog.geocoding_output.setFilter("CSV (*.csv)")

    if self.pluginDialog.exec_() == QtWidgets.QDialog.Accepted:
      data = self.pluginDialog.get_data()
      csv_input = data['csv_input']
      key = data['api_key']
      geocoding_csv = data['geocoding_output']
      QgsMessageLog.logMessage(f'csv_input: {csv_input}', 'GEOCODING LOG', Qgis.Info)
      QgsMessageLog.logMessage(f'api key: {key}', 'GEOCODING LOG', Qgis.Info)
      QgsMessageLog.logMessage(f'geocoding_csv: {geocoding_csv}', 'GEOCODING LOG', Qgis.Info)

      self.kpt_geocoding(csv_input, key, geocoding_csv)


  def  kpt_geocoding(self, kpt_csv, key, geocoding_csv):
    import numpy as np
    import pandas as pd
    import re
    import requests
    df = pd.read_csv(kpt_csv, encoding='UTF-8', sep=',')
    df['id'] = range(0, len(df))
    # df_trimmed = df[110:111]
    FiasAddrs = df['FiasAddrs']
    QgsMessageLog.logMessage(f'df адреса: {FiasAddrs}', 'GEOCODING LOG', Qgis.Info)
    API_KEY = key
    url = 'https://catalog.api.2gis.com/3.0/items/geocode'
    ids = []
    id = 0
    full_name = []
    lon = []
    lat = []
    for addr in FiasAddrs:
      ids.append(int(id))
      QgsMessageLog.logMessage(f'адреса: {addr}', 'GEOCODING LOG', Qgis.Info)
      if pd.notna(addr):
        params = {
          'q': re.sub(
            r'Российская Федерация\s*,?\s*|Сахалинская область\s*,?\s*|\bгородской округ\s*,?\s*|ул\.\s*|\bд\.\s*|\s+',
            ' ', addr),
          'fields': 'items.point',
          'key': API_KEY,
          'type': 'building'
        }
        QgsMessageLog.logMessage(f'параметры запроса: {params}', 'GEOCODING LOG', Qgis.Info)
        response = requests.get(url, params=params)
        a=response.json()['result']['items'][0]
        QgsMessageLog.logMessage(f'AAA: {a}', 'GEOCODING LOG', Qgis.Info)
        if response.status_code == 200:
          try:
            data = response.json()['result']['items'][0]
            full_name.append(data['full_name'])
            lon.append(data['point']['lon'])
            lat.append(data['point']['lat'])
          except IndexError:
            full_name.append(np.nan)
            lon.append(np.nan)
            lat.append(np.nan)
        else:
          print(f"Ошибка: {response.status_code} - {response.text}")
          full_name.append(np.nan)
          lon.append(np.nan)
          lat.append(np.nan)
      id += 1



    data = {
      'id': ids,
      '2GIS_name': full_name,
      'lat': lat,
      'lon': lon
    }
    QgsMessageLog.logMessage(f'Результаты геокодирования: {data}', 'GEOCODING LOG', Qgis.Info)

    df_2 = pd.DataFrame(data)
    merged_df = pd.merge(df, df_2, on='id', how='left')
    QgsMessageLog.logMessage(f'Результаты геокодирования полные: {merged_df}', 'GEOCODING LOG', Qgis.Info)
    if geocoding_csv:
      merged_df.to_csv(geocoding_csv, index=False, encoding='utf-8')
      QgsMessageLog.logMessage(f'Файл сохранён: {geocoding_csv}', 'GEOCODING LOG', Qgis.Info)
    else:
      QgsMessageLog.logMessage('Сохранение файла отменено: путь не указан.', 'GEOCODING LOG', Qgis.Warning)




