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
"""
        c.retrieve("insitu-glaciers-elevation-mass",
            {
                "variable": "all",
                "product_type": "elevation_change",
                "file_version": "20170405",
                "format": "tgz"
            },
            "download.tar.gz")

"""
        os.system("tar -xf download.tar.gz")

        cat = ""
        """
        with open('_C3S_ELEVATION_CHANGE_DATA_20170405.csv', newline='', encoding='unicode_escape') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cat = cat + row['PU;NAME;WGMS_ID;SURVEY_ID;SURVEY_DATE;REFERENCE_DATE;AREA_SURVEY_YEAR;AREA_CHANGE;ELEV_CH;ELEV_CH_UNC;INVESTIGATOR;SPONS_AGENCY;REFERENCE;REMARKS']
        """

        return cat
