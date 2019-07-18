
#positive displacement spanning rectangle
#negative displacement spanning rectangle
def compareSpaningRectangles(current, pdsr, ndsr):

    if pdsr.area < ndsr.area:
        if pdsr.area < current.area:
            return pdsr
        else:
            return current
    else:
        if ndsr.area < current.area:
            return ndsr
        else:
            return current

#this class is intended to package all the parametrization vectors into one structure
#this facilitates copying and comparing this vectors
class SpanningRectangle:

    def __init__( self, pc, pr, pp, area = None ):
        self.pc = pc
        self.pr = pr
        self.pp = pp
        self.area = area


    def __eq__(self, other):

        if self.pc == other.pc:
            if self.pr == other.pr:
                if self.pp == other.pp:
                    return True

        return False


    def magnitudeOfRadius( self ):
        return self.pr.magnitude()


    def copy( self ):

        if self.area != None:
            return SpanningRectangle( self.pc, self.pr, self.pp, self.area )
        else:
            return SpanningRectangle( self.pc, self.pr, self.pp )


    def __str__( self ):

        output = 'pc: ' + str(self.pc) + ' pr: ' + str(self.pr) + ' pp: ' + str(self.pp)

        if self.area != None:
            output += ' area: ' + str(self.area)

        return output
