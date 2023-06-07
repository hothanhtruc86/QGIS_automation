import os
from qgis.core import QgsMapSettings, QgsProject
from PyQt5.QtGui import QImage, QPainter

data_dir = 'G:/test repeatSfM to exportDEM/QGIS/DEM deformation observation'
project_name = 'GSD15.qgz'
project_path = os.path.join(data_dir, project_name)

# Read the QGIS project
project = QgsProject.instance()
project.read(project_path)

# Create output directory
output_dir = os.path.join(data_dir, 'exported_layers')
os.makedirs(output_dir, exist_ok=True)

# Loop through the layers
for layer_id, layer in project.mapLayers().items():
    layer_name = layer.name()
    print(f'Exporting layer: {layer_name}')

    # Create a QgsMapSettings object
    ms = QgsMapSettings()
    ms.setLayers([layer])

    # Set the extent
    rect = layer.extent()
    rect.scale(1.1)
    ms.setExtent(rect)

    # Set the output size
    image_size = QSize(3000, 3000)
    ms.setOutputSize(image_size)

    # Create a QImage object
    image = QImage(image_size, QImage.Format_ARGB32_Premultiplied)
    image.setDotsPerMeterX(1)
    image.setDotsPerMeterY(1)

    # Create a QPainter object
    painter = QPainter(image)
    painter.setRenderHint(QPainter.Antialiasing)

    # Setup QGIS map renderer
    render = QgsMapRendererCustomPainterJob(ms, painter)
    render.start()
    render.waitForFinished()

    # End painting
    painter.end()

    # Save the image
    output_path = os.path.join(output_dir, f'{layer_name}_render.tif')
    image.save(output_path)

    print(f'Exported layer {layer_name} to: {output_path}')

print('Done')
