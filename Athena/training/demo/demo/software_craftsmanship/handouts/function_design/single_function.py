import numpy

def summary(file_names):

    price_dict = {}
    for file_name in file_names:
        file = open(file_name, 'r')
        # read instrument from header
        instrument = file.readline().strip()
        # Read data into a numeric array.
        price_text = file.read()
        price_list = [float(value) for value in price_text.split()]
        price_array = numpy.array(price_list)
        price_dict[instrument] = price_array
    stats_dict = {}
    for instrument, prices in price_dict.items():
        mean = numpy.mean(prices)
        std = numpy.std(prices)
        stats_dict[instrument] = [mean, std]
    mean_max = 1e-20
    instrument_max = None
    mean_min = 1e20
    instrument_min = None
    for instrument, stats in stats_dict.items():
        mean, std = stats
        if mean > mean_max:
            mean_max = mean
            instrument_max = instrument
        if mean < mean_min:
            mean_min = mean
            instrument_min = instrument
    print "Summary:"
    print "Maximum Mean Price: %s, %3.2f" % (instrument_max, mean_max)
    print "Minimum Mean Price: %s, %3.2f" % (instrument_min, mean_min)
    format_str = "%10s %6.2f %6.2f"
    print '-' * 25
    print "All Instruments:"
    print "%10s %6s %6s" % ("Instrument", "Mean", "Std")
    for instrument, stats in stats_dict.items():
        mean,std = stats
        print "%10s %6.2f %6.2f" % (instrument, mean, std)


if __name__ == "__main__":
    file_names = ['acme.txt','generic_inc.txt', 'foo.txt']
    summary(file_names)