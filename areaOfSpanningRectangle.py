import pointLib
from findReferenceSlope import findReferenceSlope
from Vector import Vector
from Vector import magnitudeAndSlopeToVector
from changeOfBases import changeOfBases
from findNewCoordinateAxes import findNewCoordinateAxes

#this one is going to be tricky

def areaOfSpanningRectangle( x, y, r, meanVector, pr, pp ):

    tuv, nuv = findNewCoordinateAxes( pr )

    #the function requires all the points, the new origin, and each of the axes
    #t >> all points tranformed with respect to tuv
    #n >> all points transformed with respect to nuv
    t, n = changeOfBases( x, y, pp, tuv, nuv )

    #if n contains a negative value, then the rotation is invalid
    for i in range( 0, n.size ):
        if n[i] < 0:
            #POTENTIAL BUG
            #I need a better way to handle this
            return 1000000

    ze = pointLib.zenith( n, r )
    na = pointLib.nadir( n, r )
    lf = pointLib.leftmost( t, r )
    rg = pointLib.rightmost( t, r )

    height = max( ze ) - min( na )
    base = max( rg ) - min( lf )
    #print('height: ' + str(height) + ' base: ' + str(base))

    return height * base
