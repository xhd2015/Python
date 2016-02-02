
##############################
###### Future Value  #########
##############################


# Calculate the future value after 60 months of a deposit of
# $100 made every month at an annual interest rate of 3.25% (0.0325).
# Assume that there is no beginning amount.

# Specific values
when = 1       # deposit at beginning of month.
pmt = -100     # recurring deposit
pv = 0         # initial savings
n = 60         # 60 months
r = 0.0325/12  # monthly interest rate

fv = -pv*(1+r)**n - pmt*(1+r*when)/r * ((1+r)**n - 1)

print "future value is ", fv


##############################
###### Present Value #########
##############################

# Calculate the cost today of an annuity that would pay out $500/month
# for 10 years (120 months) at an annual interest rate of 6% (0.06) and
# would be worth $1000 after the final payment.

# Specific values
when = 0     # end of month payment 
fv = 1000    # $1000 left at the end
pmt = 500    # monthly payment
r = 0.06/12  # monthly interest rate
n = 10*12    # 10 years

pv = -(fv + pmt*(1+r*when)/r * ((1+r)**n - 1)) / (1+r)**n

print "present value", pv


#########################
###### Payment  #########
#########################


# Calculate the payment that will be needed to borrow $300,000 at 6.5% (0.065)
# annual interest for 15 years.

# Specific values
when = 0     # end of month payment
fv = 0       # no future value at the end
n = 15*12    # 15 years
r = 0.065/12 # monthly interest
pv = 300000  # amount received

pmt = -(fv + pv*(1+r)**n) * r / (1+r*when) / ((1+r)**n - 1)

print "Payment is ", pmt


