import re

#
# this re will match a line of the form:
#
# 'Length: 182.5" 	Width: 69" 	Curb Weight: 3,245 lbs.'
#
# and will assign the length number (no quote) width, and weight to groups
#
LENGTH_GROUP = 1
WIDTH_GROUP = 3
WEIGHT_GROUP = 5
data2Patt = re.compile( "Length: ([\d,]+(.[\d]+)?)\"\s+Width: ([\d,]+(.[\d]+)?)\"\s+Curb Weight: ([\d,]+(.[\d]+)?).*" )


#
# run test if this module is run as a script
#
if( __name__ == "__main__" ) :
    import sys

    if( len( sys.argv ) > 1 ) :

	fileHandle = open( sys.argv[1], "r" )
	for line in fileHandle.readlines() :
	    data2Match = data2Patt.match( line )
	    if( data2Match ) :
		print "LENGTH: %s" % data2Match.group( LENGTH_GROUP )
		print "WIDTH: %s" % data2Match.group( WIDTH_GROUP )
		print "WEIGHT: %s" % data2Match.group( WEIGHT_GROUP )

    else :
	line = 'Length: 182.5" 	Width: 69" 	Curb Weight: 3,245 lbs.'
	data2Match = data2Patt.match( line )
	if( data2Match ) :
	    print "LENGTH: %s" % data2Match.group( LENGTH_GROUP )
	    print "WIDTH: %s" % data2Match.group( WIDTH_GROUP )
	    print "WEIGHT: %s" % data2Match.group( WEIGHT_GROUP )

	else :
	    print "RE did not match!"


