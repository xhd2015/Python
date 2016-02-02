import re

#
# this re will match a line of the form:
#
# 'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'
#
# and need not assign any text to groups...just match
#
abbrevPatt = re.compile( "([A-Z]{2}=[A-Za-z0-9\s]+, )*([A-Z]{2}=[A-Za-z0-9\s]+)" )

#
# this function returns a dictionary of abbreviation keys to description values:
#
# {"MT" : "Manual Transmission", "AT" : "Automatic Transmission", ...}
#
# given a string:
#
# 'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'
#
# NOTE: 'Trans' must be substituted with 'Transmission'!
#
def getAbbrevDict( line ) :

    retDict = {}
    line = re.sub( "\n", "", line )

    for pair in re.split( ", ", line ) :

	(key, val) = re.split( "=", pair )
	retDict[key] = re.sub( "Trans", "Transmission", val )

    return retDict


#
# run test if this module is run as a script
#
if( __name__ == "__main__" ) :
    import sys

    if( len( sys.argv ) > 1 ) :

	fileHandle = open( sys.argv[1], "r" )
	for line in fileHandle.readlines() :
	    if( abbrevPatt.match( line ) ) :
		abbrevDict = getAbbrevDict( line )
		for item in abbrevDict.items() :
		    print "%s: %s" % item

    else :
	line = 'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'
	if( abbrevPatt.match( line ) ) :
	    abbrevDict = getAbbrevDict( line )
	    for item in abbrevDict.items() :
		print "%s: %s" % item

	else :
	    print "RE did not match!"

