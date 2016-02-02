"""
parses data files containing statistics on 3rd generation Corvettes.

The data files contain information about various options available, their order
codes, and how many were ordered for the particular model year.  This module
will parse the data files and save the information to various data structures
which can be accessed through the various API calls this module provides.
"""

import re
import types

print "HELLO WORLD"

#
# import the various re compiled pattern objects and constant
# group numbers into this namespace
#
from year import YEAR_GROUP, yearPatt
from data1 import WHEELB_GROUP, TRACKF_GROUP, TRACKR_GROUP, HEIGHT_GROUP, data1Patt
from data2 import LENGTH_GROUP, WIDTH_GROUP, WEIGHT_GROUP, data2Patt
from option import OPTCODE_GROUP, OPTNAME_GROUP, OPTQUAN_GROUP, optionPatt
from abbrev import abbrevPatt, getAbbrevDict


class VetteData :
    """
    This class maintains information about a particular Corvette model year,
    extracted from a specific data file
    """

    def __init__( self, data_file ) :
	self._dataFile = data_file
	self.year = 0
	self.options = []
	self.abbrevs = {}
	self.dimensions = {}

    def get_year( self ) :
	return int( self.year )

    def get_dimension( self, dim ) :
	return float( self.dimensions.get( dim, -1.0 ) )

    def get_options( self ) :
	return self.options

    def get_option( self, opt_code ) :
	"""
	look for the option in the list (linear search!) and return
	the option obj, else add a blank option and return it
	"""
	for opt in self.options :
	    if( opt.code == opt_code ) :
		return opt

	newOpt = VetteOption()
	self.options.append( newOpt )

	return newOpt

    def lookup_abbrev( self, abbrev ) :
	return self.dimensions.get( dim, "" )

    def load_data( self ) :
	"""
	parses the data file and sets the various fields ...this is a separate
	method rather than loading the data in the constructor so that if an
	error occurs during parsing, an object will have been constructed and it
	can be debugged, queried, etc.
	"""
	#
	# error if file cannot be read
	#
	try :
	    fileObj = open( self._dataFile, "r" )
	except :
	    raise RuntimeError, "could not read file: %s" % self._dataFile

	#
	# readlines() will return a list of lines (strings) for processing
	#
	for line in fileObj.readlines() :
	    #
	    # if the line is an option, create a new option obj, populate it with
	    # the values in the line and add it to the list of options
	    #
	    optionMatch = optionPatt.match( line )
	    if( optionMatch ) :

		newOpt = VetteOption()

		newOpt.set_code( (optionMatch.group( OPTCODE_GROUP ) or "NOCODE") )
		newOpt.set_desc( optionMatch.group( OPTNAME_GROUP ) )
		newOpt.set_quantity( optionMatch.group( OPTQUAN_GROUP ) )

		self.options.append( newOpt )
		continue
	    #
	    # simply extract specific fields from the other types of lines and
	    # set the data members in this class
	    #
	    yearMatch = yearPatt.match( line )
	    if( yearMatch ) :
		self.year = yearMatch.group( YEAR_GROUP )
		continue

	    data1Match = data1Patt.match( line )
	    if( data1Match ) :
		self.dimensions["wheelbase"] = \
		    data1Match.group( WHEELB_GROUP )
		self.dimensions["trackFront"] = \
		    data1Match.group( TRACKF_GROUP )
		self.dimensions["trackRear"] = \
		    data1Match.group( TRACKR_GROUP )
		self.dimensions["height"] = \
		    data1Match.group( HEIGHT_GROUP )
		continue

	    data2Match = data2Patt.match( line )
	    if( data2Match ) :
		self.dimensions["length"] = \
		    data2Match.group( LENGTH_GROUP )
		self.dimensions["width"] = \
		    data2Match.group( WIDTH_GROUP )
		self.dimensions["weight"] = \
		    re.sub( ",", "", data2Match.group( WEIGHT_GROUP ) )
		continue
	    #
	    # if the list of abbreviations is matched, pass the line to the function
	    # which converts the line to a dictionary and save it to the data member
	    #
	    if( abbrevPatt.match( line ) ) :
		self.abbrevs = getAbbrevDict( line )
		continue
	#
	# this is done automatically when the file obj goes out-of-scope
	#
	fileObj.close()



class VetteOption :
    """
    This class maintains information about a particular option for a Corvette
    """

    def __init__( self ) :
	self.code = -1
	self.desc = ""
	self.quan = -1

    def set_code( self, code ) :
	if( type( code ) != types.StringType ) :
	    raise TypeError, "code must be a string"
	self.code = code

    def set_desc( self, desc ) :
	if( type( desc ) != types.StringType ) :
	    raise TypeError, "desc must be a string"
	self.desc = desc

    def set_quantity( self, quan ) :
	if( type( quan ) == types.StringType ) :
	    quan = re.sub( ",", "", quan )
	    quan = int( quan )
	elif( type( quan ) != types.IntType ) :
	    raise TypeError, "quan must be an integer or string rep of an integer"

	self.quan = quan

    def get_code( self ) :
	return self.code

    def get_desc( self ) :
	return self.desc

    def get_quantity( self ) :
	return int( self.quan )


def test() :
    """
    return a string suitable for printing which contains information extracted
    from the data files
    """

    retString = ""
    #
    # assume data files 68-73.dat are present in the cwd...crash if not
    #
    for year in range( 68, 73 ) :

	dataFile = "%s.dat" % year

	vs = VetteData( dataFile )
	vs.load_data()

	retString += "YEAR: %s\n" % vs.year
	retString += "WHEELBASE: %s WEIGHT: %s\n" % \
		     (vs.dimensions["wheelbase"], vs.dimensions["weight"])

	retString += "ABBREVS: "
	for (abbrev, desc) in vs.abbrevs.items() :
	    retString += "%s: %s\n         " % (abbrev, desc)
	retString += "\n"

	for o in vs.options[0:10] :
	    retString += "%s \"%s\" %s\n" % (o.code, o.desc, o.quan)

	retString += "\n\n"

    return retString


#
# if run as a script, print test result string
#
if( __name__ == "__main__" ) :
    print test()
