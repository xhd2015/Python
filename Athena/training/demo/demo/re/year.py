import re

#
# this re will match a line of the form:
#
# '1969 Options:'
#
# and will assign the year to a group for extracting
#
YEAR_GROUP = 1
yearPatt = re.compile( "(\d{4}) Options:" )


#
# run test if this module is run as a script
#
if( __name__ == "__main__" ) :
    import sys

    if( len( sys.argv ) > 1 ) :

	fileHandle = open( sys.argv[1], "r" )
	for line in fileHandle.readlines() :
	    yearMatch = yearPatt.match( line )
	    if( yearMatch ) :
		print "YEAR: %s" % yearMatch.group( YEAR_GROUP )

    else :
	line = '1969 Options:'
	yearMatch = yearPatt.match( line )
	if( yearMatch ) :
	    print "YEAR: %s" % yearMatch.group( YEAR_GROUP )

	else :
	    print "RE did not match!"


