
# Include the header file "string.h"
cdef extern from "string.h":
    cdef extern  int strlen(char *c)


def get_len(char *message):
    """Return the length of a string."""
    return strlen(message)
