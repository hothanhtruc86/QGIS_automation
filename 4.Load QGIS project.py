import os
#read a QGIS project

data_dir = 'G:/test repeatSfM to exportDEM/QGIS/DEM deformation observation'
project = QgsProject.instance()
project_name = 'GSD15.qgz'
project_path = os.path.join(data_dir, project_name)
project.read(project_path)