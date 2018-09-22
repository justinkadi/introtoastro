
""" Creating a Color-Magnitude Diagram of the 10,000 Closest Stars to Us"""

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

gaia_data = pd.read_csv('GAIA_query_results.csv')

plot.figure()

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


""" Challenge question """

new_data = pd.read_csv('GAIA_challenge_results.csv')

plot.figure()

heatmap, xedges, yedges = np.histogram2d(
    new_data.bp_rp.values,
    new_data.g_abs.values,
    bins=100
)

extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

heatmap = np.ma.masked_where(heatmap == 0.0, heatmap)

color_map = plot.cm.hot
color_map.set_bad(color='white')

plot.imshow(
    np.sqrt(heatmap.T),
    extent=extent,
    cmap=color_map,
    aspect=(extent[1]-extent[0])/(extent[3]-extent[2]),
    origin='lower'
)
plot.colorbar()
plot.xlabel('G$_{BP}$ - G$_{RP}$')
plot.ylabel('M$_G$')
plot.gca().invert_yaxis()

plot.savefig('challenge_diagram')
plot.show()
