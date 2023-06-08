import os
from qgis.core import QgsMapSettings, QgsProject
from PyQt5.QtGui import QImage, QPainter

data_dir = 'G:/test repeatSfM to exportDEM/QGIS/DEM deformation observation'
project_name = 'GSD15.qgz'
project_path = os.path.join(data_dir, project_name)

# Read the QGIS project
project = QgsProject.instance()
project.read(project_path)

##Rastor calculation
import processing

# Set the input raster files and output file path
input_raster1 = 'path/to/input_raster1.tif'
input_raster2 = 'path/to/input_raster2.tif'
output_raster = 'path/to/output_raster.tif'

# Set the raster calculation expression
# Example: Add the values of input_raster1 and input_raster2
expression = 'A + B'

# Set the additional parameters (if required)
parameters = {
    'A': input_raster1,
    'B': input_raster2,
    'OUTPUT': output_raster,
    'EXPRESSION': expression,
    'FORMAT': 'GTiff',
    'OPTIONS': '',
}

# Run the gdal_calc algorithm
processing.run('gdal:rastercalculator', parameters)