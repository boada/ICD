#File: gini_plot.py
#Created: Mon 12 Mar 2012 03:00:01 PM CDT
#Last Change: Mon 12 Mar 2012 03:49:05 PM CDT
#Author: Steven Boada

import numpy as np
import pylab as plt

gini = np.loadtxt('gdss_e4_f160_m25.morph')
icd = np.loadtxt('icd_1.5_3.5_gsd_full_ston.txt')

f1 = plt.figure(1,figsize=(8,8))
f1s1 = f1.add_subplot(111)
f2 = plt.figure(2,figsize=(8,8))
f2s1 = f2.add_subplot(111)
f3 = plt.figure(3,figsize=(8,8))
f3s1 = f3.add_subplot(111)

for i in range(len(icd)):
	for j in range(len(gini)):
		if icd[i][0] == gini[j][0]:
			if icd[i][11] > 30.0: # STON_I
				if icd[i][9]> 0.1:
					f1s1.plot(gini[i][20],gini[i][19],
					c='#FE4C00',marker='s',markersize=8)
				elif icd[i][9]>0.05:
					f1s1.plot(gini[i][20],gini[i][19],
					c='#FFB236',marker='o',markersize=7)
                		elif icd[i][9]>0.01:
					f1s1.plot(gini[i][20],gini[i][19],
					c='#BD83F7',marker='o',markersize=7)
                		else:
					f1s1.plot(gini[i][20],gini[i][19],
					c='#03469E',marker='o',markersize=7)
        		elif 20.0 < icd[i][11] and icd[i][11] < 30.0: # STON_I
				f1s1.plot(gini[i][20],gini[i][19],
				c='0.8',marker='s',alpha=0.4)
        		else:
				f1s1.plot(gini[i][20],gini[i][19],
				c='0.8',marker='.',alpha=0.4)
                	

			if icd[i][15] > 30.0: # STON_Z
				if icd[i][9]> 0.1:
                        		f2s1.plot(gini[i][20],gini[i][19],
					c='#FE4C00',marker='s',markersize=8)
                		elif icd[i][9]>0.05:
					f2s1.plot(gini[i][20],gini[i][19],
					c='#FFB236',marker='o',markersize=7)
                		elif icd[i][9]>0.01:
					f2s1.plot(gini[i][20],gini[i][19],
					c='#BD83F7',marker='o',markersize=7)
                		else:
					f2s1.plot(gini[i][20],gini[i][19],
					c='#03469E',marker='o',markersize=7)
        		elif 20.0 < icd[i][15] and icd[i][15] < 30.0: # STON_Z
				f2s1.plot(gini[i][20],gini[i][19],
					c='0.8',marker='s',alpha=0.4)
        		else:
				f2s1.plot(gini[i][20],gini[i][19],
					c='0.8',marker='.',alpha=0.4)

			if icd[i][19] > 30.0: # STON_J
				if icd[i][9]> 0.1:
                        		f3s1.plot(gini[i][20],gini[i][19],
						c='#FE4C00',marker='s',markersize=8)
                		elif icd[i][9]>0.05:
					f3s1.plot(gini[i][20],gini[i][19],
						c='#FFB236',marker='o',markersize=7)
                		elif icd[i][9]>0.01:
					f3s1.plot(gini[i][20],gini[i][19],
						c='#BD83F7',marker='o',markersize=7)
                		else:
					f3s1.plot(gini[i][20],gini[i][19],
						c='#03469E',marker='o',markersize=7)
        		elif 20.0 < icd[i][19] and icd[i][19] < 30.0: # STON_J
				f3s1.plot(gini[i][20],gini[i][19],
					c='0.8',marker='s',alpha=0.4)
        		else:
				f3s1.plot(gini[i][20],gini[i][19],
					c='0.8',marker='.',alpha=0.4)


m1 = np.arange(-3.0,0.0,0.1)
m2 = np.arange(-3.0,-1.68,0.1)

plt.figure(1)
f1s1.plot(m1,-0.14*m1+0.33,'--',color='g')
f1s1.plot(m2,0.14*m2+0.80,'.',color='r')

f1s1.set_xlim(-3,0)
f1s1.set_ylim(0.3,0.8)
ax = plt.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f1s1.tick_params(axis='both',pad=7)
f1s1.set_xlabel(r"$M_{20}$",fontsize=20)
f1s1.set_ylabel("G",fontsize=20)
f1s1.legend()


plt.figure(2)
f2s1.plot(m1,-0.14*m1+0.33,'--',color='g')
f2s1.plot(m2,0.14*m2+0.80,'.',color='r')

f2s1.set_xlim(-3,0)
f2s1.set_ylim(0.3,0.8)
ax = plt.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f2s1.tick_params(axis='both',pad=7)
f2s1.set_xlabel(r"$M_{20}$",fontsize=20)
f2s1.set_ylabel("G",fontsize=20)


plt.figure(3)
f3s1.plot(m1,-0.14*m1+0.33,'--',color='g')
f3s1.plot(m2,0.14*m2+0.80,'.',color='r')

f3s1.set_xlim(-3,0)
f3s1.set_ylim(0.3,0.8)
ax = plt.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f3s1.tick_params(axis='both',pad=7)
f3s1.set_xlabel(r"$M_{20}$",fontsize=20)
f3s1.set_ylabel("G",fontsize=20)

plt.show()
