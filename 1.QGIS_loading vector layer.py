import os # nhập thư viện để làm việc với chưc năng liên quan đến hiệu 
data_dir = 'G:/test repeatSfM to exportDEM/QGIS'#đặt đường dẫn tới vị trí lưu 

filename = 'obsevation points.shp'#biến lưu tên layer cần 
uri = os.path.join(data_dir, filename)#kết hợp đường dẫn và tên layer cần mở,có thể thay đổi tên layer khi cần mở layer khác năm cùng 
iface.addVectorLayer(uri, 'obsevation points', 'ogr')#thêm 1 lớp vector vào giao diện QGIS, 'ogr' là định dạng vector
#Add another vector layer to QGIS 
filename = 'target area.shp'
uri = os.path.join(data_dir, filename)
iface.addVectorLayer(uri, 'target area', 'ogr')
# change a layer name 
layer = iface.activeLayer()
name = layer.name()
layer.setName('sf_' + name)

    