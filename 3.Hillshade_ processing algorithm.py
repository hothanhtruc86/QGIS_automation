import os # nhập thư viện để làm việc với chưc năng liên quan đến hệ điều hành

#load raster for hillshade function 
data_dir = 'G:/test repeatSfM to exportDEM/reference_DEM/GSD20'#đặt đường dẫn tới vị trí lưu raster

filename = 'GSD20_referenceDEM.tif'
DEM = os.path.join(data_dir, filename)
iface.addRasterLayer(DEM, 'srtm', 'gdal')# displace raster , 'gdal' is raster file
#output directory definition
output_name = 'hillshade.tif'
output_path = os.path.join(data_dir, output_name)

processing.run("native:hillshade", 
    {'INPUT':'G:/test repeatSfM to exportDEM/reference_DEM/GSD20/GSD20_referenceDEM.tif',
    'Z_FACTOR':1,'AZIMUTH':300,
    'V_ANGLE':40,'OUTPUT':output_path})

iface.addRasterLayer(output_path, 'hillshade', 'gdal')