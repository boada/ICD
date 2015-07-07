#File: gini_plot.py
#Created: Mon 12 Mar 2012 03:00:01 PM CDT
#Last Change: Tue 26 Jun 2012 10:48:25 AM CDT
#Author: Steven Boada

import numpy as np
import pylab as pyl

gini = np.loadtxt('gdss_e4_f160_m25.morph')
icd = np.loadtxt('icd_1.5_3.5_gsd_full_ston.txt')

f1 = pyl.figure(1,figsize=(6,4))
f1s1 = f1.add_subplot(111)
f2 = pyl.figure(2,figsize=(6,4))
f2s1 = f2.add_subplot(111)
f3 = pyl.figure(3,figsize=(6,4))
f3s1 = f3.add_subplot(111)

for i in range(len(icd)):
	for j in range(len(gini)):
		if icd[i][0] == gini[j][0]:
			if icd[i][11] > 30.0: # STON_I
				f1s1.plot(gini[i][20],gini[i][19],
                		c='#F28500',marker='o')#,markersize=8)
                    		#f1s1.plot(gini[i][20],gini[i][19])
                		#if icd[i][9]> 0.1:
                			#f1s1.plot(gini[i][20],gini[i][19],
                			#c='#F28500',marker='s')#,markersize=8)
                		#elif icd[i][9]>0.05:
                			#f1s1.plot(gini[i][20],gini[i][19],
                			#c='#AAF0D1',marker='o')#,markersize=7)
                		#elif icd[i][9]>0.01:
                			#f1s1.plot(gini[i][20],gini[i][19],
                			#c='#B0E0E6',marker='o')#,markersize=7)
                		#else:
                			#f1s1.plot(gini[i][20],gini[i][19],
                			#c='0.8',marker='.')#,markersize=7)
                    	#elif 20.0 < icd[i][11] and icd[i][11] < 30.0: # STON_I
                		#f1s1.plot(gini[i][20],gini[i][19],
               			#c='0.8',marker='s',alpha=0.4)
                	#else:
                		#f1s1.plot(gini[i][20],gini[i][19],
                		#c='0.8',marker='.',alpha=0.4)

			if icd[i][15] > 30.0: # STON_Z
				if icd[i][9]> 0.1:
                        		f2s1.plot(gini[i][20],gini[i][19],
					c='#F28500',marker='s')#,markersize=8)
                		elif icd[i][9]>0.05:
					f2s1.plot(gini[i][20],gini[i][19],
					c='#AAF0D1',marker='o')#,markersize=7)
                		elif icd[i][9]>0.01:
					f2s1.plot(gini[i][20],gini[i][19],
					c='#B0E0E6',marker='o')#,markersize=7)
                		else:
					f2s1.plot(gini[i][20],gini[i][19],
					c='.8',marker='.')#,markersize=7)
                    #elif 20.0 < icd[i][15] and icd[i][15] < 30.0: # STON_Z
                #f2s1.plot(gini[i][20],gini[i][19],
                #c='0.8',marker='s',alpha=0.4)
                #else:
                #f2s1.plot(gini[i][20],gini[i][19],
                #c='0.8',marker='.',alpha=0.4)

			if icd[i][19] > 30.0: # STON_J
				if icd[i][9]> 0.1:
                        		f3s1.plot(gini[i][20],gini[i][19],
					c='#F28500',marker='s')#,markersize=8)
                		elif icd[i][9]>0.05:
					f3s1.plot(gini[i][20],gini[i][19],
						c='#AAF0D1',marker='o')#,markersize=7)
                		elif icd[i][9]>0.01:
					f3s1.plot(gini[i][20],gini[i][19],
					c='#B0E0E6',marker='o')#,markersize=7)
                		else:
					f3s1.plot(gini[i][20],gini[i][19],
					c='.8',marker='.')#,markersize=7)
                    #elif 20.0 < icd[i][19] and icd[i][19] < 30.0: # STON_J
                #f3s1.plot(gini[i][20],gini[i][19],
                #c='0.8',marker='s',alpha=0.4)
                #else:
                #f3s1.plot(gini[i][20],gini[i][19],
                #c='0.8',marker='.',alpha=0.4)


m1 = np.arange(-3.0,0.0,0.1)
m2 = np.arange(-3.0,-1.68,0.1)

pyl.figure(1)
f1s1.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f1s1.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)

pyl.subplots_adjust(bottom=0.15)
f1s1.set_xlim(-3,0)
f1s1.set_ylim(0.3,0.8)
ax = pyl.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f1s1.tick_params(axis='both',pad=7)
f1s1.set_xlabel(r"$M_{20}$",fontsize=18)
f1s1.set_ylabel("G",fontsize=18)

f1l1 = pyl.figtext(0.45,0.7,'Merger',fontsize=18)
f1l2 = pyl.figtext(0.7,0.5,'E/S0/Sa',fontsize=18)
f1l3 = pyl.figtext(0.6,0.25,'Sb-Ir',fontsize=18)

#f1s1.legend()


pyl.figure(2)
f2s1.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f2s1.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)
pyl.subplots_adjust(bottom=0.15)

f2s1.set_xlim(-3,0)
f2s1.set_ylim(0.3,0.8)
ax = pyl.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f2s1.tick_params(axis='both',pad=7)
f2s1.set_xlabel(r"$M_{20}$",fontsize=18)
f2s1.set_ylabel("G",fontsize=18)


pyl.figure(3)
f3s1.plot(m1,-0.14*m1+0.33,'--',color='g',lw=2)
f3s1.plot(m2,0.14*m2+0.80,'.',color='r',lw=2)
pyl.subplots_adjust(bottom=0.15)

f3s1.set_xlim(-3,0)
f3s1.set_ylim(0.3,0.8)
ax = pyl.gca()
ax.set_xlim(ax.get_xlim()[::-1])
f3s1.tick_params(axis='both',pad=7)
f3s1.set_xlabel(r"$M_{20}$",fontsize=18)
f3s1.set_ylabel("G",fontsize=18)

pyl.show()
