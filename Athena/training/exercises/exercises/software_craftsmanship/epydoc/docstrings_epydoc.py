"""

"""

_whendict = {'end':0,
             'begin':1,
             0:0,
             1:1}


def future_value(r, n, pmt, pv=0.0, when='begin'):
    """
    future value in time value of money equations

    Future value (at the end of the final period) of making n payments,
    pmt, at an interest rate of r per payment starting with a present value
    of pv.

    The when argument must be 'begin' (1) or 'end' (0) and
    determines whether or not the payment is made at the beginning
    (default) of the period or at the end. 
    """
    when = _whendict[when]
    return -pv*(1+r)**n - pmt*(1+r*when)/r * ((1+r)**n - 1)
    


def present_value(r, n, pmt, fv=0.0, when='end'):
    """present value in time value of money equations

    The present value of an annuity (or a one-time future value
    to be realized later) when the interest rate is r per period, there
    are n periods, and the fixed payment per period is pmt. The final
    value is the amount that should be available after the final period.

    The when argument must be 'begin' (1) or 'end' (0) and determines
    whether or not the payment is made at the beginning or end (default)
    of the period. 
    """
    when = _whendict[when]
    return -(fv + pmt*(1+r*when)/r * ((1+r)**n - 1)) / (1+r)**n



def payment(r, n, pv, fv=0.0, when='end'):
    """payment in time value of money equations
    
    Calculate the payment required to convert the present value,
    pv, into the future value, fv, when the interest rate is r and
    the number of payments is n

    The when argument must be 'begin' (1) or 'end' (0) and determines
    whether or not the payment is made at the beginning or end (default)
    of the period. 
    """
    when = _whendict[when]
    return -(fv + pv*(1+r)**n) * r / (1+r*when) / ((1+r)**n - 1)
