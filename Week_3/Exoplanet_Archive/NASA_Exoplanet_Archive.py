
"""Creating visuals using NASA's Exoplanet Archive"""

import matplotlib.pyplot as plot
import pandas as pd

""" Mass v. Radii plot """

data1 = pd.read_csv('archive_mass_radii.csv')

plot.plot(data1['pl_radj'],data1['pl_bmassj'],'k.')
plot.ylabel('Planet Mass')
plot.xlabel('Planet Radii')
plot.title('Exoplanet Radii v. Mass')
plot.savefig('data1_graph')
plot.show()

""" Orbital Period v. Semi-Major Axis plot """

data2 = pd.read_csv('archive_orbitalperiod_smaxis.csv')

plot.plot(data2['pl_orbper'], data2['pl_orbsmax'], 'k.')
plot.xlabel('Orbital Period')
plot.ylabel('Semi-Major Axis')
plot.title('Semi-Major Axis vs Orbital Period')
plot.savefig('data2_graph')
plot.show()

""" Orbital Period v. Orbital Eccentricity plot """

data3 = pd.read_csv('archive_orbitalperiod_eccentricity.csv')

plot.plot(data3['pl_orbper'], data3['pl_orbeccen'], 'k.')
plot.xlabel('Orbital Period')
plot.ylabel('Orbital Eccentricity')
plot.title('Orbital Period vs Orbital Eccentricity')
plot.savefig('data3_graph')
plot.show()

input()
