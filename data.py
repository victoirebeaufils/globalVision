import cdsapi
import os

from netCDF4 import Dataset

def ktoc(temp):
    return temp - 273.15

def ktof(temp):
    return (ktoc(temp) + 9 / 5) + 32


class Data:
    time = 0
    lons = []
    lats = []
    ssts = []



    def temp():


        cat = ""

        root = Dataset("20140420120000-ESACCI-L4_GHRSST-SST-GMPE-GLOB_CDR2.0-v02.0-fv01.0.nc",
            "r", format="NETCDF4")

        time = root['time'][0]
        lons = root['lon']
        lats = root['lat']
        ssts = root['analysed_sst']

        #cat = tmp.format(lon = root['lon'])



       # cat = "{seconds:d}".format(seconds=time)

        for i in range(100,len(lons)-1,50):
            for j in range(100,len(lats)-1,20):

                if (ssts[0,j,i] != '--'):
                    cat = cat + "{lon:.1f}, {lat:.1f}, {sst:.1f}:".format(lon=lons[i],
                        lat=lats[j],
                        sst=ktoc(ssts[0,j,i]))
                    print (ssts[0,j,i])

        # root.close() ## uncomment to close, might break data access in __init__.py

        return cat
