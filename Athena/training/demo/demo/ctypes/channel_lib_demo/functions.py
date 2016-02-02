"""Python wrappers for the functions in functions.c."""

import sys
from ctypes import cdll, c_char_p, c_int, c_void_p, c_uint8
import numpy
from numpy.ctypeslib import ndpointer


class ChannelClosedError(ValueError):
    pass

    
# The functions channel_init(), channel_calibrate(), channel_write() 
# and channel_close() form a "suite" of related functions.  It is natural
# to wrap these together in a class.  Note the following:
# 1. The function channel_init() is called in the class's __init__() method,
#    so a user of this object never actually sees the call to channel_init().
# 2. The channel_data memory is saved in the class, so the user never has
#    to be aware of this.  This eliminates one argument from the Python
#    versions of the calibrate(), write() and get_status() functions.
# 3. The C function channel_get_status() is just a "getter".  We'll implement
#    this as a read-only property of the class (instead of a function).
# 4. The C function channel_write() expects an array of unsigned chars.
#    We'll create a wrapper for this function that can accept a Python string
#    or a numpy array of type numpy.uint8.
# 5. We provide a close() method, but in the __del__() method, we check
#    if the channel has been closed, and if it hasn't, we close it.
#
# We have not created a ctypes wrapper for the channel_data structure
# itself, so we do not expose the fields in this structure to python.
# With a little more work, we could expose the contents of the memory
# as, for example, attributes of the class.


class Channel(object):

    def __init__(self, name="<default>"):

        # 'dll' is the shared library, loaded as a module using ctypes.
        self._dll = self._load_dll()

        # 'channel_data' is a ctypes c_void_p pointer.
        self._channel_data = self._dll.channel_init(name)

    def __del__(self):
        self.close()

    def _load_dll(self):
        """Load the 'functions' shared library using ctypes, and configure the
        argtypes and restype of the functions in the module.

        Returns the shared library module.
        """

        # Load the shared library.  The filename is platform-dependent.        
        if sys.platform == 'darwin':
            dll = cdll.LoadLibrary('libfunctions.dylib')
        elif sys.platform == 'win32':
            dll = cdll.LoadLibrary('libfunctions.dll')
        else:
            dll = cdll.LoadLibrary('./libfunctions.so')

        # Configure the argument types and return types of the functions
        # in the shared library.

        dll.channel_init.argtypes = [c_char_p]
        dll.channel_init.restype = c_void_p

        dll.channel_calibrate.argtypes = [c_void_p, c_int]
        dll.channel_calibrate.restype = c_int

        dll.channel_get_status.argtypes = [c_void_p]
        dll.channel_get_status.restype = c_int

        dll.channel_write.argtypes = [c_void_p, c_int,
                                      ndpointer(c_uint8, ndim=1, flags='C')]
        dll.channel_write.restype = c_int

        dll.channel_close.argtypes = [c_void_p]
        dll.channel_close.restype = c_int
        
        return dll

    def calibrate(self, param):
        if self._channel_data is None:
            raise ChannelClosedError("channel is closed.")
        status = self._dll.channel_calibrate(self._channel_data, param)
        return status

    def _get_status(self):
        if self._channel_data is None:
            raise ChannelClosedError("channel is closed.")
        status = self._dll.channel_get_status(self._channel_data)
        return status

    status = property(_get_status, doc="Get the channel status.")

    def write(self, data):
        """data can be a string, a list of numbers, or a numpy array.

        In the latter two cases, the values are converted to unsigned
        8 bit values.
        """

        # Future enhancement: allow data to be a 'bytes' data type
        # (Python 2.6+ and Python 3).

        if isinstance(data, str):
            data_array = numpy.fromstring(data, dtype=numpy.uint8)
            n = len(data)
            result = self._dll.channel_write(self._channel_data, n, data_array)
        else:
            # Warning: this will silently convert the data elements in
            # the list or array to unsigned 8 bit ints. For example,
            # 6.78 becomes 6, 1000.0 becomes 232, and -6.78 becomes 250.
            data_array = numpy.asarray(data, dtype=numpy.uint8).ravel()
            n = data_array.size
            result = self._dll.channel_write(self._channel_data, n,
                                                                data_array)
        return result

    def close(self):
        if self._channel_data is not None:
            self._dll.channel_close(self._channel_data)
            self._channel_data = None

