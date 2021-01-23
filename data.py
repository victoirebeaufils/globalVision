import cdsapi
import os
import csv

from netCDF4 import Dataset


class Data:
    def temp():
        c = cdsapi.Client()

        c.retrieve(
            'satellite-sea-surface-temperature-ensemble-product',
            {
                'variable': 'all',
                'format': 'tgz',
                'day': '20',
                'year': '2016',
                'month': '04',
            },
            'download.tar.gz')
        os.system("tar -xf download.tar.gz")

        tmp = "{lon:.2f}"
        cat = ""

        root = Dataset("20160420120000-ESACCI-L4_GHRSST-SST-GMPE-GLOB_CDR2.0-v02.0-fv01.0.nc",
            "r", format="NETCDF4")

        time = root['time'][0]
        lons = root['lon']
        lats = root['lat']
        ssts = root['analysed_sst']

        #cat = tmp.format(lon = root['lon'])

        root.close()

        return cat
