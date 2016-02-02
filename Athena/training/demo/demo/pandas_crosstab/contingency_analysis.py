"""
Demonstrate a 2x2 contingency table analysis using Pandas and scipy.stats.

The file "survey.csv" contains the results of a survey of 680 people.
The file records the gender of the person, and whether or not they liked
a certain new movie.  The question to be investigated is simply whether or
not there is signficant difference in the responses depending on gender.

We'll make a 2x2 contingency table (also known as a cross-tab), and
test if such a table would arise at random if the gender and movie
preference were independent.
"""

import pandas as pd
from scipy.stats import chi2_contingency

# Read the file into a DataFrame.
df = pd.read_csv('survey.csv')

# Use the Pandas crosstab function to form the contingency table.
ct = pd.crosstab(df['gender'], df['liked'])

print "There are {:d} responses in the survey.".format(len(df))
print "The contingency table:"
print
print ct
print

# Compute the chi2 statistics and p-value.
chi2, p, dof, expd = chi2_contingency(ct.as_matrix())

print "The p-value is {:g}".format(p)

# Can we reject the null hypothesis?
if p < 0.05:
    print "At the 5% level, we reject the null hypothesis"
else:
    print "At the 5% level, we cannot reject the null hypothesis"
print "that gender and movie preference are independent."
