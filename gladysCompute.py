import io

import gladysSatellite as satellite

"""
       Student: Anh Tong 
       Module: gladysCompute
       Description: This module does computes the distance between
       current position and the destination position using the provided 
       formulas

"""

def gpsAverage (x, y):
    """
         document your function definition here. what does it do?
         compute the gpsAverage formula
    """
    latitude = satellite.gpsValue(x, y, 'latitude')
    longtitude = satellite.gpsValue(x, y, 'longitude')
    altitude = satellite.gpsValue(x, y, 'altitude')
    time = satellite.gpsValue(x, y, 'time')

    gpsValuesSum = latitude + longtitude + altitude + time
    average = gpsValuesSum / 4

    return average


def distance (current, destination):
    """
        document your funciton definition here. what does it do?
        return the average to the gladysUserInterface module

    """
    currGpsAverage = gpsAverage(current[0], current[1])
    destGpsAverage = gpsAverage(destination[0], destination[1])
    dist = (currGpsAverage ** 2 + destGpsAverage ** 2) ** 0.5

    return dist