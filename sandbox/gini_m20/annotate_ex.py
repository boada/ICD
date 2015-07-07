#!/usr/bin/env python
# File: annotate_ex.py
# Created on: Mon 09 Apr 2012 09:29:47 AM CDT
# Last Change: Mon 09 Apr 2012 09:32:38 AM CDT
# Purpose of script: <+INSERT+>
# Author: Steven Boada

import numpy as np
import matplotlib.pyplot as plt

N = 10
data = np.random.random((N, 4))
labels = ['point{0}'.format(i) for i in range(N)]
plt.subplots_adjust(bottom = 0.1)
plt.scatter(data[:, 0], data[:, 1], marker = 'o', c = data[:, 2], s =
        data[:,3]*1500,
cmap = plt.get_cmap('Spectral'))
for label, x, y in zip(labels, data[:, 0], data[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (-20, 20),textcoords = 'offset\
            points', ha ='right', va = 'bottom',bbox = dict(boxstyle =
            'round,pad=0.5', fc ='yellow', alpha = 0.5), arrowprops =
            dict(arrowstyle ='->', connectionstyle='arc3,rad=0'))
plt.show()
