import re

#
# This re will match a line of the form:
#
# 'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'
#
abbrev_patt = re.compile("[A-Z][A-Z]=.*(, +[A-Z][A-Z]=.*)*$")


def get_abbrev_dict(line) :
    """
    This function returns a dictionary of abbreviation keys to description values:
    
        {"MT" : "Manual Transmission", "AT" : "Automatic Transmission", ...}
        
    given a string:

        'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'

    NOTE: 'Trans' must be substituted with 'Transmission'!
    """
    ret_dict = {}
    line = line.replace('\n', '')

    for pair in line.split(', '):
        (key, val) = pair.split("=")
        ret_dict[key] = re.sub("Trans$", "Transmission", val)

    return ret_dict


#
# Run test if this module is run as a script.
#
if __name__ == "__main__":

    import sys

    if len(sys.argv) > 1:
        # Read the string from a file.
        file_handle = open(sys.argv[1], "r")
        for line in file_handle:
            if abbrev_patt.match(line):
                abbrev_dict = get_abbrev_dict(line)
                for item in abbrev_dict.items() :
                    print "%s: %s" % item
    else:
        # Use this string as a test case:
        line = 'MT=Manual Trans, AT=Automatic Trans, PS=Power Steering, AC=Air Conditioning, AH=Aluminum Head, IG=Transistor Ignition, HC=Heavy Duty Clutch, UU=Uncertain Usage'
        if abbrev_patt.match(line):
            abbrev_dict = get_abbrev_dict(line)
            for item in abbrev_dict.items():
                print "%s: %s" % item
        else:
            print "RE did not match!"
