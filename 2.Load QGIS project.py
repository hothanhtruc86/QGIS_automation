import os # nhập thư viện để làm việc với chưc năng liên quan đến hệ điều hành

#load QGIS project
data_dir = 'G:/test repeatSfM to exportDEM/QGIS/GSD20'#đặt đường dẫn tới vị trí lưu project 

project = QgsProject.instance() #tạo một biến project để lưu thể hiện của lớp QgsProject. Lớp QgsProject
#đại diện cho một dự án trong QGIS và cung cấp các phương thức để quản lý và làm việc với dự án.
project_name = '230525GSD20.qgz'
project_path = os.path.join(data_dir, project_name) #join path and name
project.read(project_path)