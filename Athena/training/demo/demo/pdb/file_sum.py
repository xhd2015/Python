"""
This module defines the FileSum class which maintaines the sum of every
number in a file (It might actually be useful for something, who knows?).
"""


class FileSum(object):
    """
    This class maintains the sum of every number in a particular data file
    """

    def __init__(self, file_name):
        self.sum = 0
        self.fileName = file_name

    def convert_to_number(self, item):
        """
        Return an actual number type extracted from a string,
        or the original string if not possible.
        """
        try:
            return int(item)
        except ValueError:
            try:
                return float(item)
            except ValueError:
                return item
                #return 0

    def get_numbers_in_file(self):
        """
        Returns a list of all the numbers in the file
        """
        retList = []
        fileHandle = open(self.fileName, "r")

        for token in fileHandle.read().split():
            number = self.convert_to_number(token)
            retList.append(number)

        fileHandle.close()
        return retList

    def calculate_sum(self):
        """
        Compute the sum of every number in the file.
        """
        self.sum = 0
        numberList = self.get_numbers_in_file()

        for number in numberList:
            self.sum += number


def test(file_name):
    """
    Compute the sum of every number in the file passed in.
    """
    fs = FileSum(file_name)
    fs.calculate_sum()

    print "The sum of all numbers in %d is %s" % (file_name, fs.sum)
    #print "The sum of all numbers in %s is %s" % (file_name, fs.sum)


#
# run the test func on the file specified by the first arg
# is this module is run as a script
#
if __name__ == "__main__":
    import sys
    import pdb

    if len(sys.argv) != 2:
        print "Usage: %s <file>" % sys.argv[0]
        sys.exit(1)

    test(sys.argv[1])
