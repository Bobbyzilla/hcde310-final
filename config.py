import os

class Config:
    googlemapsAPIkey = os.environ.get('AIzaSyCA67C_oA1VdbCZ90LYvI5_7IWBe3i_2CM')
    yelpfusionAPIkey = os.environ.get('Z8bqP64fyxDEDXlsmo5mlDOhFa12UGVlN8I2tFzu4c55XVTMTnTZYrkK4L7fwT94qeOOQiZvSrDPjAuKRcx4lxDFdb1lXqmeshj23H93fU40udwT7kpHBKfP-gIQZHYx')
    sqlalchemyDB = 'sqlite:///restaurant.db'
    sqlalchemytrack = False