#############################################################################
# property_1.py
#
# 1. get/set Property example.
#############################################################################

from traits.api import HasTraits, Property, Any

class Foo(HasTraits):

	# A property trait.
	value = Property
	
	# A "shadow" value to hold the variable
	_the_shadow = Any

	#########################################################################
	# Protected Interfrace
	#########################################################################
	
	# get/set methods #######################################################
	
	def _get_value(self):
		print "get value"
		return self._the_shadow
		
	def _set_value(self, value):
		print "set value"
		self._the_shadow = value 

#############################################################################
# Demo Code
#############################################################################

foo = Foo()
foo.value = 1.0
value = foo.value
