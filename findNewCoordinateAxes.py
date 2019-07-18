
from findReferenceSlope import findReferenceSlope
from Vector import Vector
from Vector import magnitudeAndSlopeToVector


def findNewCoordinateAxes( pr ):

  reference_slope = findReferenceSlope( pr )

  #tuv >> tangent unit vector along the reference line
  tuv = magnitudeAndSlopeToVector( 1, reference_slope )

  #nuv >> normal unit vector
  #perpendicular to tuv and also points towards the inside of the points
  #towards the inside is the opposite of pr
  nuv = Vector( -1 * pr.t, -1 * pr.n ).unitVector()

  return ( tuv, nuv )
