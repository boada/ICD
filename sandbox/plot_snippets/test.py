#!/usr/bin/env python
# File: test.py
# Created on: Fri Aug  9 15:37:59 2013
# Last Change: Fri Aug  9 15:38:15 2013
# Purpose of script: <+INSERT+>
# Author: Steven Boada
from random import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import scoreatpercentile

x = np.array([random() for x in xrange(100)])

# percentiles of interest
perc = [min(x), scoreatpercentile(x,10), scoreatpercentile(x,25),
               scoreatpercentile(x,50), scoreatpercentile(x,75),
               scoreatpercentile(x,90), max(x)]
midpoint = 0 # time-series time

fig = plt.figure()
ax = fig.add_subplot(111)
# min/max
ax.broken_barh([(midpoint-.01,.02)], (perc[0],
perc[1]-perc[0]))
ax.broken_barh([(midpoint-.01,.02)], (perc[5],
perc[6]-perc[5]))
# 10/90
ax.broken_barh([(midpoint-.1,.2)], (perc[1],
perc[2]-perc[1]))
ax.broken_barh([(midpoint-.1,.2)],
(perc[4], perc[5]-perc[4]))
# 25/75
ax.broken_barh([(midpoint-.4,.8)],
(perc[2], perc[3]-perc[2]))
ax.broken_barh([(midpoint-.4,.8)],
(perc[3],
perc[4]-perc[3]))

ax.set_ylim(-0.5,1.5)
ax.set_xlim(-10,10)
ax.set_yticks([0,0.5,1])
ax.grid(True)
plt.show()
