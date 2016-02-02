import re

#
# this re will match a line of the form:
#
# 'Wheelbase: 98" 	Track: 58.7" Front / 59.4" Rear 	Height: 47.8" Coupe'
#
# and will assign the wheelbase number (no quote), track front, track rear,
# and height to groups
#
WHEELB_GROUP = 1
TRACKF_GROUP = 3
TRACKR_GROUP = 5
HEIGHT_GROUP = 7
data1Patt = re.compile( "Wheelbase: ([\d,]+(.[\d]+)?)\"\s+Track: ([\d,]+(.[\d]+)?)\" Front \/ ([\d,]+(.[\d]+)?)\" Rear\s+Height: ([\d,]+(.[\d]+)?)\".*" )


#
# run test if this module is run as a script
#
if( __name__ == "__main__" ) :
    import sys

    if( len( sys.argv ) > 1 ) :

	fileHandle = open( sys.argv[1], "r" )
	for line in fileHandle.readlines() :
	    data1Match = data1Patt.match( line )
	    if( data1Match ) :
		print "WHEELBASE: %s" % data1Match.group( WHEELB_GROUP )
		print "FRONT TRACK: %s" % data1Match.group( TRACKF_GROUP )
		print "REAR TRACK: %s" % data1Match.group( TRACKR_GROUP )
		print "HEIGHT: %s" % data1Match.group( HEIGHT_GROUP )

    else :
	line = 'Wheelbase: 98" 	Track: 58.7" Front / 59.4" Rear 	Height: 47.8" Coupe'
	data1Match = data1Patt.match( line )
	if( data1Match ) :
	    print "WHEELBASE: %s" % data1Match.group( WHEELB_GROUP )
	    print "FRONT TRACK: %s" % data1Match.group( TRACKF_GROUP )
	    print "REAR TRACK: %s" % data1Match.group( TRACKR_GROUP )
	    print "HEIGHT: %s" % data1Match.group( HEIGHT_GROUP )

	else :
	    print "RE did not match!"


