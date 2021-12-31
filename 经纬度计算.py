from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):# 经度1 纬度1 经度2 纬度2
    lon1,lat1,lon2,lat2 = map(radians,[lon1,lat1,lon2,lat2])# 转弧度
    r = 1000*6371.137
    s = sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2
    dis = 2*r*asin(sqrt(s))
    return dis