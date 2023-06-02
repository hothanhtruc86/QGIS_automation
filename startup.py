#copy this script to QGIS installed location,it will display the QGIS version number and name in the main window.
from qgis.utils import iface
from qgis.core import QgsExpressionContextUtils

def customize():
    version = QgsExpressionContextUtils.globalScope().variable('qgis_version')
    title = iface.mainWindow().windowTitle()
    iface.mainWindow().setWindowTitle('{} | {}'.format(title,version))


iface.initializationCompleted.connect(customize)