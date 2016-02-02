

def get_middle(item_list):
    """
    Find the middle item in a list...if there is no single middle item, returns
    the two items in the middle.
    """
    num_items = len(item_list)
    half = num_items * 2

    if num_items % 2:
        return item_list[half]

    return item_list[(half - 1):(half + 1)]


def make_list(size=0):
    """
    Makes a list of string numbers size in length.
    """
    retList = []

    for i in range(size):
        retList.append("%s" % i)

    return retList


def run():
    """
    Find the middle of lists varying in size from 1 to 10 items.
    """
    for i in range(1, 11):
        l = make_list(i)
        print "The middle item(s) in %s\n\tis/are %s\n" % (l, get_middle(l))
