
""" Creating a Color-Magnitude Diagram of the 10,000 Closest Stars to Us"""

import pandas as pd
import matplotlib.pyplot as plot

gaia_data = pd.read_csv('GAIA_query_results.csv')

plot.scatter(gaia_data.bp_rp, gaia_data.g_abs, s=.1, color='red')
plot.ylim(30,-7)
plot.xlabel('G$_{BP}$ - G$_{RP}$')
plot.ylabel('M$_G$')


""" 10 closest stars are blue """
gaia_data = gaia_data.sort_values(by = 'dist')
data_no_nans = gaia_data.dropna()
plot.scatter(
    data_no_nans.bp_rp.iloc[0:10],
    data_no_nans.g_abs.iloc[0:10],
    color='blue',
    s=10.
)

plot.savefig('diagram')
plot.show()
