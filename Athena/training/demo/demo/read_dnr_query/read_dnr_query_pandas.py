
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Timestamp format.
fmt = "%Y%j+%H%M"

df = pd.read_table('data.txt', sep='\s+', skiprows=22, skip_footer=1,
                    names=['time', 'temp', 'sal', 'ph', 'depth'],
                    parse_dates=True,
                    date_parser=lambda s: datetime.strptime(s, fmt),
                    index_col=0)

df['depth'].plot()
plt.show()
