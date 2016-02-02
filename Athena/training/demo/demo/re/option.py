import re

#
# this re will match a line of the form:
#
# '19437    Base Corvette Sport Coupe    22,129'
#
# as well as...
#
# 'Genuine Leather Seats    3,729'
#
# and will assign the 1st number, text description, and 2nd number to groups
#
OPTCODE_GROUP = 2
OPTNAME_GROUP = 3
OPTQUAN_GROUP = 4
optionPatt = re.compile( "(([0-9A-Z]*)    )?(.+)    ([0-9,]+)" )


#
# run test if this module is run as a script
#
if( __name__ == "__main__" ) :
    import sys

    if( len( sys.argv ) > 1 ) :

	fileHandle = open( sys.argv[1], "r" )
	for line in fileHandle.readlines() :
	    optionMatch = optionPatt.match( line )
	    if( optionMatch ) :
		print "CODE: %s" % optionMatch.group( OPTCODE_GROUP )
		print "NAME: %s" % optionMatch.group( OPTNAME_GROUP )
		print "QUANTITY: %s" % optionMatch.group( OPTQUAN_GROUP )

    else :
	line = '19437    Base Corvette Sport Coupe    22,129'
	optionMatch = optionPatt.match( line )
	if( optionMatch ) :
	    print "CODE: %s" % optionMatch.group( OPTCODE_GROUP )
	    print "NAME: %s" % optionMatch.group( OPTNAME_GROUP )
	    print "QUANTITY: %s" % optionMatch.group( OPTQUAN_GROUP )

	else :
	    print "RE did not match!"


