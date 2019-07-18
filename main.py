
import numpy as np
import mainLib
import pointLib
from findReferenceSlope import findReferenceSlope
from Vector import Vector
from Vector import magnitudeAndSlopeToVector
from math import tan

#this variable is the number of times the approximation is going to be improved
EPOCHS = 10
#this variable controls how fast the parametrization radius is rotated
alpha = 0.524078
#this variable controls how fast the aproximations are improved
beta = 2

print('START OF PROGRAM')

inputFile = open('rectangles4.txt', 'r')

( x, y, r ) = mainLib.parseInputFileToMatrix( inputFile )

#no need for the input file any more
inputFile.close()

( x_avg, y_avg ) = pointLib.meanPoint( x, y )

meanVector = Vector( x_avg, y_avg )

#the parametrization vectors are used to compute the distaces of key points relative to
#one side of a spanning rectangle
#pc >> parametrization center
#pr >> parametrization radius
#pp >> parametrization point
i_fur, pc, pr, pp  = mainLib.findParametrizationVectors( meanVector, x, y, r )

#magnitude of parametrization radius
#stored in a variable for convenience. Its going to be used over and over
mpr = r[i_fur]

#An initial value
minArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, pr, pp )
bestKnownRectangle = mainLib.SpanningRectangle(pc, pr, pp, minArea)
print('initial area:' + str( minArea ) )

#HERE IS WHERE THE LOOP TAKES PLACE

#flag to control execution
keepGoing = True

while( keepGoing ):

    tuv, nuv = mainLib.findNewCoordinateAxes( bestKnownRectangle.pr )
    print('bkr: (' + str(alpha) + ") " + str(bestKnownRectangle))

    #positive Displacement Along The Paprametrization Line
    pdapl = tuv ** alpha

    #positive displacement parametrization vector
    #positive displacement parametrization point
    pdprv, pdpp = mainLib.findRotatedParametrizationVectors( bestKnownRectangle.pc, bestKnownRectangle.magnitudeOfRadius(), bestKnownRectangle.pp, pdapl )

    positiveDisplacementArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, pdprv, pdpp )

    #positive Displacement Spanning Rectangle
    pdsr = mainLib.SpanningRectangle( bestKnownRectangle.pc, pdprv, pdpp, positiveDisplacementArea )

    #negative Displacement Along The Paprametrization Line
    ndapl = tuv ** ( -1 * alpha )


    #negative displacement parametrization vector
    #negative displacement parametrization point
    ndprv, ndpp = mainLib.findRotatedParametrizationVectors( bestKnownRectangle.pc, bestKnownRectangle.magnitudeOfRadius(), bestKnownRectangle.pp, ndapl )

    negativeDisplacementArea = mainLib.areaOfSpanningRectangle( x, y, r, meanVector, ndprv, ndpp )

    #negative Displacement Spanning Rectangle
    ndsr = mainLib.SpanningRectangle( bestKnownRectangle.pc, ndprv, ndpp, negativeDisplacementArea )

    newRectangle = mainLib.compareSpaningRectangles( bestKnownRectangle, pdsr, ndsr )

    if newRectangle == bestKnownRectangle:
        EPOCHS = EPOCHS - 1
        alpha = alpha/beta

    bestKnownRectangle = newRectangle.copy()

    print("| " + str(EPOCHS) + '| (' + str(alpha) + ") " + str(bestKnownRectangle))

    if EPOCHS <= 0:
        keepGoing = False

    print('=================================')




print('\nEND OF PROGRAM')
