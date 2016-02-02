""" Data processing module containing functions that convert string data into 
more manageable list of transactions.
"""

def process_log(log):
    """ Process a warehouse log"""
    # Remove any leading and trailing whitespace from the string::

    warehouse_log = log.strip()

    # Create a list of transactions from the log with part as string.
    # and count as integer::
    
    transactions = []
    for line in warehouse_log.split("\n"):
        part, count = line.split()
        transaction = (part, int(count))
        transactions.append(transaction)

    return transactions