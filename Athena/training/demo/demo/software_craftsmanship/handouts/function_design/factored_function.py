import numpy
    
#----------------------------------------------------------------------
# Standard Basket Reports. 
#----------------------------------------------------------------------

def summarize_price_statistics(basket):

    basket_stats = basket_price_statistics(basket)
    instrument_min, instrument_max = min_max_instrument_mean(basket_stats)
    mean_max, std = basket_stats[instrument_max]
    mean_min, std = basket_stats[instrument_min]
    
    print "Summary:"
    print "Maximum Mean Price: %s, %3.2f" % (instrument_max, mean_max)        
    print "Minimum Mean Price: %s, %3.2f" % (instrument_min, mean_min)        
    format_str = "%10s %6.2f %6.2f"
    print
    print "All Instruments:" 
    print "%10s %6s %6s" % ("Instrument", "Mean", "Std")
    for instrument, stats in basket_stats.items():
        mean,std = stats
        print "%10s %6.2f %6.2f" % (instrument, mean, std)


#-----------------------------------------------------------------------
# Basket Statistics Routines 
#-----------------------------------------------------------------------

def basket_price_statistics(basket):
    basket_stats = {}
    for instrument, prices in basket.items():
        mean = numpy.mean(prices)
        std = numpy.std(prices)
        basket_stats[instrument] = [mean, std]    

    return basket_stats

def min_max_instrument_mean(basket_stats):
    mean_max = 1e-20
    instrument_max = None
    mean_min = 1e20
    instrument_min = None    
    for instrument, stats in basket_stats.items():
        mean, std = stats
        if mean > mean_max:
            mean_max = mean
            instrument_max = instrument
        if mean < mean_min:
            mean_min = mean
            instrument_min = instrument
    
    return instrument_min, instrument_max


#-----------------------------------------------------------------------
# Input/Output Routines: Read baskets/Insturments from files.
#-----------------------------------------------------------------------

def basket_from_file_names(file_names):
    basket_prices = {}
    for file_name in file_names:
        file = open(file_name, 'r')
        instrument, prices = read_price_file(file)
        basket_prices[instrument] = prices
    
    return basket_prices
    
def read_price_file(file):
    # read instrument from header
    instrument = file.readline().strip()            
    # Read data into a numeric array.
    price_text = file.read()
    price_list = [float(value) for value in price_text.split()]
    price_array = numpy.array(price_list)        
    
    return instrument, price_array

            
if __name__ == "__main__":
    file_names = ['acme.txt','generic_inc.txt', 'foo.txt']
    basket = basket_from_file_names(file_names)
    summarize_price_statistics(basket)    
                        