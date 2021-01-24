import cdsapi
import os
import csv

from netCDF4 import Dataset



class Data:
    time = 0
    lons = []
    lats = []
    ssts = []
    def temp():
        c = cdsapi.Client()

        c.retrieve(
            'satellite-sea-surface-temperature-ensemble-product',
            {
                'variable': 'all',
                'format': 'tgz',
                'day': '20',
                'year': '2014',
                'month': '04',
            },
            'download.tar.gz')
        os.system("tar -xf download.tar.gz")

        cat = ""

        root = Dataset("20140420120000-ESACCI-L4_GHRSST-SST-GMPE-GLOB_CDR2.0-v02.0-fv01.0.nc",
            "r", format="NETCDF4")

        time = root['time'][0]
        lons = root['lon']
        lats = root['lat']
        ssts = root['analysed_sst']

        #cat = tmp.format(lon = root['lon'])



        cat = "{seconds:d}<br>".format(seconds=time)

        ###DATA ACCESS LOOP
        for i in range(100,len(lons)-1,20):
            for j in range(100,len(lats)-1,15):
                if (ssts[0,j,i] != '--'):
                    cat = cat + "{lon:.4f}, {lat:.4f}, {sst:.4f}<br>".format(lon=lons[i],
                        lat=lats[j],
                        sst=ssts[0,j,i])
                    print (ssts[0,j,i])

        # root.close() ## uncomment to close, might break data access in __init__.py

        return cat

    def ktoc(temp):
        return temp - 273.15

    def ktof(temp):
        return (ktoc(temp) + 9 / 5) + 32
