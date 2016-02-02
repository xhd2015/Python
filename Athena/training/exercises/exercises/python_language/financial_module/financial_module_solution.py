"""
Financial Module
----------------

Background
~~~~~~~~~~

The future value (fv) of money is related to the present value (pv)
of money and any recurring payments (pmt) through the equation::

    fv + pv*(1+r)**n + pmt*(1+r*when)/r * ((1+r)**n - 1) = 0
     
or, when r == 0::

    fv + pv + pmt*n == 0

Both of these equations assume the convention that cash in-flows are
positive and cash out-flows are negative.  The additional variables in
these equations are:

* n: number of periods for recurring payments
* r: interest rate per period
* when: When payments are made:
    
  - (1) for beginning of the period
  - (0) for the end of the period
  
The interest calculations are made through the end of the
final period regardless of when payments are due. 

Problem
~~~~~~~

Take the script financial_calcs.py and use it to construct a module with
separate functions that can perform the needed calculations with
arbitrary inputs to solve general problems based on the time value
of money equation given above. 

Use keyword arguments in your functions to provide common default
inputs where appropriate.

Bonus
~~~~~

1) Document your functions.
2) Add a function that calculates the number of periods from the other variables.
3) Add a function that calculates the rate from the other variables.

"""


def future_value(r, n, pmt, pv=0.0, when=1):
    """Future value in "time value of money" equations.
    
    * r: interest rate per payment (decimal fraction)
    * n: number of payments
    * pv: present value
    * when: when payment is made, either 1 (begining of period, default) or 
      0 (end of period)

    """
    return -pv*(1+r)**n - pmt*(1+r*when)/r * ((1+r)**n - 1)
    


def present_value(r, n, pmt, fv=0.0, when=0):
    """Present value in "time value of money" equations.

    The present value of an annuity (or a one-time future value
    to be realized later) 
    
    * r: interest rate per period (decimal fraction)
    * n: number of periods
    * pmt: the fixed payment per period
    * fv: the amount that should be available after the final period.
    * when: when payment is made, either 1 (begining of period) or 
      0 (end of period, default)
    """
    return -(fv + pmt*(1+r*when)/r * ((1+r)**n - 1)) / (1+r)**n



def payment(r, n, pv, fv=0.0, when=0):
    """Payment in "time value of money" equations.
    
    Calculate the payment required to convert the present value into the future
    value.
    
    * r: interest rate per period (decimal fraction)
    * n: number of periods
    * pv: present value
    * fv: the amount that should be available after the final period.
    * when: when payment is made, either 1 (begining of period) or 
      0 (end of period, default)

    """
    return -(fv + pv*(1+r)**n) * r / (1+r*when) / ((1+r)**n - 1)

	
# Future Value Example.
yearly_rate = .0325
monthly_rate = yearly_rate / 12
monthly_periods = 5 * 12 # 5 years
monthly_payment = -100 # $100 per period.
print "future value is ", future_value(monthly_rate, monthly_periods,
										monthly_payment)


# Present Value Example.
yearly_rate = .06
monthly_rate = yearly_rate / 12
monthly_periods = 10 * 12 # 10 years
monthly_income = 500 
fv = 1000
pv = present_value(monthly_rate, monthly_periods, monthly_income, 
				   fv=fv)
print "present value is ", pv

# Loan Payment
yearly_rate = .065
monthly_rate = yearly_rate / 12
monthly_periods = 15 * 12 # 15 years
loan_amount = 300000   
print "payment is ", payment(monthly_rate, monthly_periods, loan_amount)

