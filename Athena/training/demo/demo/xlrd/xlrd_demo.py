"""
Use xlrd to pull data out of an Excel spreadsheet.
Some of the data is plotted with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
from xlrd import open_workbook, XL_CELL_NUMBER


# First we'll read the data of interest from the spreadsheet.
# The data that we want is in the rows where the first column
# contains a number.  From these rows, we get the country name,
# human devlelopment index, life expectancy at birth and gross
# national income per capita.  In this loop, we simple make
# a list of tuples containing this data.
wb = open_workbook('HDR_2011_Statistical_Tables.xls')
sheet1 = wb.sheet_by_name("1")
data_list = []
for r in range(sheet1.nrows):
    c0 = sheet1.cell(r, 0)
    if c0.ctype == XL_CELL_NUMBER:
        country = sheet1.cell(r, 1).value
        hdi = sheet1.cell(r, 3).value
        life_expectancy_at_birth = sheet1.cell(r, 5).value
        gross_national_income_per_capita = sheet1.cell(r, 11).value
        data_list.append((country.encode('utf-8'),
                          hdi,
                          life_expectancy_at_birth,
                          gross_national_income_per_capita))

# Now we'll put the data into two useful forms: a numpy structured array,
# and a dictionary whose keys are country names.
# First get the maximum length of the country names.
maxlen = max(len(data[0]) for data in data_list)
# Create the data type for the structured array.
dt = np.dtype([('country', 'S%d' % maxlen),
               ('hdi', np.float),
               ('life_expectancy', np.float),
               ('gnipc', np.float)])
# Create the structured array.
data_array = np.array(data_list, dtype=dt)

# Make a dictionary whose keys are the country names.
country_data = {}
for data in data_list:
    country_data[data[0]] = data[1:]

# Scatter plot, life expectancy vs. gross national income per capita
plt.semilogx(data_array['gnipc'], data_array['life_expectancy'], 'bo')

# Label a selection of the data points.
labels = [
    ('Norway', (12,18)),
    ('Congo (Democratic Republic of the)', (-30,-45)),
    ('Liberia', (-35, 30)),
    ('Cuba', (-25, 20)),
    ('Japan', (-55, -5)),
    ('United States', (40,-30)),
    ('Qatar', (20,10)),
    ('Equatorial Guinea', (24, -25)),
    ('Gabon', (24, -20)),
    ('Russian Federation', (24,-20)),
    ]
bbox_args = dict(boxstyle="round", fc="0.8")
arrow_args = dict(arrowstyle='->')
for label, offset in labels:
    values = country_data[label]
    an = plt.annotate(label, (values[2], values[1]),
                    xytext=offset,
                    textcoords='offset points',
                    bbox=bbox_args,
                    arrowprops=arrow_args)
    an.draggable()
    
# Finish off the plot.
plt.xlabel("Gross national income per capita (PPP$) (log scale)")
plt.ylabel("Life expectancy at birth (years)")
plt.xlim(100, 500000)
plt.ylim(40, 85)
plt.grid(True)
plt.show()
