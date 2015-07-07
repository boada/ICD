import numpy as np
import pylab as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator
from colsort import colsort

# Mass vs ICD plot I-H
f1 = plt.figure(1,figsize=(8,8))
f1s1 = f1.add_subplot(111)
#f1s1 = f1.add_subplot(211)
#f1s2 = f1.add_subplot(212)

# Mass vs ICD plot Z-H
f2 = plt.figure(2,figsize=(8,8))
f2s1 = f2.add_subplot(111)
#f2s1 = f2.add_subplot(211)
#f2s2 = f2.add_subplot(212)

# Mass vs ICD plot J-H
f3 = plt.figure(3,figsize=(8,8))
f3s1 = f3.add_subplot(111)
#f3s1 = f3.add_subplot(211)
#f3s2 = f3.add_subplot(212)

# Mass vs color plot I-H
f4 = plt.figure(4,figsize=(8,8))
f4s1 = f4.add_subplot(111)

# Mass vs color plot J-H
f5 = plt.figure(5,figsize=(8,8))
f5s1 = f5.add_subplot(111)

# Mass vs color plot Z-H
f6 = plt.figure(6,figsize=(8,8))
f6s1 = f6.add_subplot(111)

# Histogram I-H
f7 = plt.figure(7,figsize=(8,8))
f7s1 = f7.add_subplot(311)
f7s2 = f7.add_subplot(312)
f7s3 = f7.add_subplot(313)

# Histogram Z-H
f8 = plt.figure(8,figsize=(8,8))
f8s1 = f8.add_subplot(311)
f8s2 = f8.add_subplot(312)
f8s3 = f8.add_subplot(313)

# Histogram J-H
f9 = plt.figure(9,figsize=(8,8))
f9s1 = f9.add_subplot(311)
f9s2 = f9.add_subplot(312)
f9s3 = f9.add_subplot(313)

# Histogram Data
IH_low = []
IH_med = []
IH_high = []
ZH_low = []
ZH_med = []
ZH_high = []
JH_low = []
JH_med = []
JH_high = []

galaxies = np.loadtxt('tilvi_matched.txt')

for i in range(len(galaxies)):
	# ICD vs Mass Plots
	if galaxies[i][12] > 30.0:
		if 1 >=10.0:
			f1s1.plot(galaxies[i][9],galaxies[i][10],c='#FFAB19',marker='o')
		else:
			f1s1.plot(galaxies[i][9],galaxies[i][10],c='#196DFF',marker='o')
	elif 20.0 < galaxies[i][12] and galaxies[i][12] < 30.0 :
		f1s1.plot(galaxies[i][9],galaxies[i][10],c='0.8',marker='s',alpha=0.4)
	else:
		f1s1.plot(galaxies[i][9],galaxies[i][10],c='0.8',marker='.',alpha=0.4)
			
	if galaxies[i][15] > 30.0:
		if 1 >=10.0:	
			f2s1.plot(galaxies[i][9],galaxies[i][13],c='#FFAB19',marker='o')
		else:
			f2s1.plot(galaxies[i][9],galaxies[i][13],c='#196DFF',marker='o')
	elif 20.0 < galaxies[i][15] and galaxies[i][15] < 30.0 :
		f2s1.plot(galaxies[i][9],galaxies[i][13],c='0.8',marker='s',alpha=0.4)
	else:
		f2s1.plot(galaxies[i][9],galaxies[i][13],c='0.8',marker='.',alpha=0.4)

	if galaxies[i][18] > 30.0:
		if 1 >=10.0:
			f3s1.plot(galaxies[i][9],galaxies[i][16],c='#FFAB19',marker='o')
		else:
			f3s1.plot(galaxies[i][9],galaxies[i][16],c='#196DFF',marker='o')
	elif 20.0 < galaxies[i][18] and galaxies[i][18] < 30.0 :
		f3s1.plot(galaxies[i][9],galaxies[i][16],c='0.8',marker='s',alpha=0.4)
	else:
		f3s1.plot(galaxies[i][9],galaxies[i][16],c='0.8',marker='.',alpha=0.4)

		# Color vs Mass Plots
	if galaxies[i][12] >30.0:
		if 1 >=10.0:
			f4s1.plot(galaxies[i][9],galaxies[i][4]-galaxies[i][7],c='#FFAB19',marker='o',markersize=9)
		if galaxies[i][10] > 0.1:
			f4s1.plot(galaxies[i][9],galaxies[i][4]-galaxies[i][7],c='None',marker='s',markersize=10)
		else:
			f4s1.plot(galaxies[i][9],galaxies[i][4]-galaxies[i][7],c='#196DFF',marker='*')
	elif 20.0 < galaxies[i][12] and galaxies[i][12] < 30.0 :
		f4s1.plot(galaxies[i][9],galaxies[i][4]-galaxies[i][7],c='0.8',marker='s',alpha=0.4)
	else:	
		f4s1.plot(galaxies[i][9],galaxies[i][4]-galaxies[i][7],c='0.8',marker='.',alpha=0.4)
	if galaxies[i][15] >30.0:
		if 1 >=10.0:
			f5s1.plot(galaxies[i][9],galaxies[i][5]-galaxies[i][7],c='#FFAB19',marker='o',markersize=9)
		if galaxies[i][13] > 0.05:
			f5s1.plot(galaxies[i][9],galaxies[i][5]-galaxies[i][7],c='None',marker='s',markersize=10)
		else:
			f5s1.plot(galaxies[i][9],galaxies[i][5]-galaxies[i][7],c='#196DFF',marker='*')
	elif 20.0 < galaxies[i][15] and galaxies[i][15] < 30.0 :
		f5s1.plot(galaxies[i][9],galaxies[i][5]-galaxies[i][7],c='0.8',marker='s',alpha=0.4)
	else:	
		f5s1.plot(galaxies[i][9],galaxies[i][5]-galaxies[i][7],c='0.8',marker='.',alpha=0.4)

	if galaxies[i][18] >30.0:
		if 1 >=10.0:
			f6s1.plot(galaxies[i][9],galaxies[i][6]-galaxies[i][7],c='#FFAB19',marker='o',markersize=9)
		if galaxies[i][16] > 0.03:
			f6s1.plot(galaxies[i][9],galaxies[i][6]-galaxies[i][7],c='None',marker='s',markersize=10)
		else:
			f6s1.plot(galaxies[i][9],galaxies[i][6]-galaxies[i][7],c='#196DFF',marker='*')
	elif 20.0 < galaxies[i][18] and galaxies[i][18] < 30.0 :
		f6s1.plot(galaxies[i][9],galaxies[i][6]-galaxies[i][7],c='0.8',marker='s',alpha=0.4)
	else:
		f6s1.plot(galaxies[i][9],galaxies[i][6]-galaxies[i][7],c='0.8',marker='.',alpha=0.4)


	# Make Histogram Data 
	if 3e7 < galaxies[i][9] and galaxies[i][9] < 1e10:
		if galaxies[i][12] > 30.0:
			IH_low.append(galaxies[i][10])
		if galaxies[i][15] > 30.0:
			ZH_low.append(galaxies[i][13])
		if galaxies[i][18] > 30.0:
			JH_low.append(galaxies[i][16])
	elif 1e10 < galaxies[i][9] and galaxies[i][9] < 1e11:
		if galaxies[i][12] > 30.0:
			IH_med.append(galaxies[i][10])
		if galaxies[i][15] > 30.0:
			ZH_med.append(galaxies[i][13])
		if galaxies[i][18] > 30.0:
			JH_med.append(galaxies[i][16])
	elif 1e11 < galaxies[i][9] and galaxies[i][9] < 1e12:
		if galaxies[i][12] > 30.0:
			IH_high.append(galaxies[i][10])
		if galaxies[i][15] > 30.0:
			ZH_high.append(galaxies[i][13])
		if galaxies[i][18] > 30.0:
			JH_high.append(galaxies[i][16])
		
# Make the Histogram Plots
'''
h, binedg = np.histogram(IH_low,25)
wid = binedg[1:] - binedg[:-1]
f7s1.bar(binedg[:-1],h/float(len(IH_low)+len(IH_med)+len(IH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(IH_med,25)
wid = binedg[1:] - binedg[:-1]
f7s2.bar(binedg[:-1],h/float(len(IH_low)+len(IH_med)+len(IH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(IH_high,25)
wid = binedg[1:] - binedg[:-1]
f7s3.bar(binedg[:-1],h/float(len(IH_low)+len(IH_med)+len(IH_high)),width=wid,alpha=0.5,color='b')

h, binedg = np.histogram(ZH_low,25)
wid = binedg[1:] - binedg[:-1]
f8s1.bar(binedg[:-1],h/float(len(ZH_low)+len(ZH_med)+len(ZH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(ZH_med,25)
wid = binedg[1:] - binedg[:-1]
f8s2.bar(binedg[:-1],h/float(len(ZH_low)+len(ZH_med)+len(ZH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(ZH_high,25)
wid = binedg[1:] - binedg[:-1]
f8s3.bar(binedg[:-1],h/float(len(ZH_low)+len(ZH_med)+len(ZH_high)),width=wid,alpha=0.5,color='b')

h, binedg = np.histogram(JH_low,25)
wid = binedg[1:] - binedg[:-1]
f9s1.bar(binedg[:-1],h/float(len(JH_low)+len(JH_med)+len(JH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(JH_med,25)
wid = binedg[1:] - binedg[:-1]
f9s2.bar(binedg[:-1],h/float(len(JH_low)+len(JH_med)+len(JH_high)),width=wid,alpha=0.5,color='b')
h, binedg = np.histogram(JH_high,25)
wid = binedg[1:] - binedg[:-1]
f9s3.bar(binedg[:-1],h/float(len(JH_low)+len(JH_med)+len(JH_high)),width=wid,alpha=0.5,color='b')
'''
#f7s1.hist(IH_low,25,histtype='step')
#f7s1.hist(IH_med,25,histtype='step')
#f7s1.hist(IH_high,25,histtype='step')

#f8s1.hist(ZH_low,25,histtype='step')
#f8s1.hist(ZH_med,25,histtype='step')
#f8s1.hist(ZH_high,25,histtype='step')

#f9s1.hist(JH_low,25,histtype='step')
#f9s1.hist(JH_med,25,histtype='step')
#f9s1.hist(JH_high,25,histtype='step')

###################################
###################################
### FINISH PLOTS ... LABELS etc ###
###################################
###################################

############
# FIGURE 1 #
############
plt.figure(1)

plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1,hspace=0.0)

f1s1.set_xscale('log')
f1s1.set_xlim(3e7,1e12)
f1s1.set_ylim(-0.1,0.4)
f1s1.hlines(0.0,3e7,1e12)
f1s1.tick_params(axis='both',pad=7)
# remove extra ticks
#f1s1.xaxis.set_major_formatter(plt.NullFormatter())

#f1s2.set_xscale('log')
#f1s2.set_xlim(3e7,1e12)
#f1s2.set_ylim(-0.1,0.4)
#f1s2.hlines(0.0,3e7,1e12)
#f1s2.tick_params(axis='both',pad=7)

# labels
f1xl =plt.figtext(0.5,0.025,r"$Log_{10}(M_{\odot})$",fontsize=20,ha='center')
f1yl =plt.figtext(0.025,0.5,r"$\xi[I,H]$",fontsize=20,ha='center',rotation='vertical')
#f1s1l =plt.figtext(0.25,0.8,"$1.5 \leq z \leq 2.5$",fontsize=16,ha='center')
#f1s2l =plt.figtext(0.25,0.4,"$2.5 \leq z \leq 3.5$",fontsize=16,ha='center')
plt.savefig('figure1.png')
############
# FIGURE 2 # 
############
plt.figure(2)

plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1,hspace=0.0)

f2s1.set_xscale('log')
f2s1.set_xlim(3e7,1e12)
f2s1.set_ylim(-0.1,0.3)
f2s1.hlines(0.0,3e7,1e12)
f2s1.tick_params(axis='both',pad=7)
# remove extra ticks
#f2s1.xaxis.set_major_formatter(plt.NullFormatter())

#f2s2.set_xscale('log')
#f2s2.set_xlim(3e7,1e12)
#f2s2.set_ylim(-0.1,0.3)
#f2s2.hlines(0.0,3e7,1e12)
#f2s2.tick_params(axis='both',pad=7)

# labels
f2xl =plt.figtext(0.5,0.025,r"$Log_{10}(M_{\odot})$",fontsize=20,ha='center')
f2yl =plt.figtext(0.025,0.5,r"$\xi[Z,H]$",fontsize=20,ha='center',rotation='vertical')
#f2s1l =plt.figtext(0.25,0.8,"$1.5 \leq z \leq 2.5$",fontsize=16,ha='center')
#f2s2l =plt.figtext(0.25,0.4,"$2.5 \leq z \leq 3.5$",fontsize=16,ha='center')
plt.savefig('figure2.png')

############
# FIGURE 3 #
############
plt.figure(3)

plt.subplots_adjust(left=0.1,right=0.9,top=0.9,bottom=0.1,hspace=0.0)

f3s1.set_xscale('log')
f3s1.set_xlim(3e7,1e12)
f3s1.set_ylim(-0.1,0.2)
f3s1.hlines(0.0,3e7,1e12)
f3s1.tick_params(axis='both',pad=7)
# remove extra ticks
#f3s1.xaxis.set_major_formatter(plt.NullFormatter())

#f3s2.set_xscale('log')
#f3s2.set_xlim(3e7,1e12)
#f3s2.set_ylim(-0.1,0.2)
#f3s2.hlines(0.0,3e7,1e12)
#f3s2.tick_params(axis='both',pad=7)

# labels
f3xl =plt.figtext(0.5,0.025,r"$Log_{10}(M_{\odot})$",fontsize=20,ha='center')
f3yl =plt.figtext(0.025,0.5,r"$\xi[J,H]$",fontsize=20,ha='center',rotation='vertical')
#f3s1l =plt.figtext(0.25,0.8,"$1.5 \leq z \leq 2.5$",fontsize=16,ha='center')
#f3s2l =plt.figtext(0.25,0.4,"$2.5 \leq z \leq 3.5$",fontsize=16,ha='center')
plt.savefig('figure3.png')

############
# FIGURE 4 #
############
plt.figure(4)

f4s1.set_xscale('log')
f4s1.set_xlim(3e7,1e12)
f4s1.set_ylim(0,4.5)
f4s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
f4s1.set_ylabel("$(I-H)_{Observed}$",fontsize=20)
f4s1.tick_params(axis='both',pad=7)
plt.savefig('figure4.png')

############
# FIGURE 5 #
############
plt.figure(5)

f5s1.set_xscale('log')
f5s1.set_xlim(3e7,1e12)
f5s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
f5s1.set_ylabel("$(Z-H)_{Observed}$",fontsize=20)
f5s1.tick_params(axis='both',pad=7)
plt.savefig('figure5.png')

############
# FIGURE 6 #
############
plt.figure(6)

f6s1.set_xscale('log')
f6s1.set_xlim(3e7,1e12)
f6s1.set_ylim(-0.5,2)
f6s1.set_xlabel(r"$Log_{10}(M_{\odot})$",fontsize=20)
f6s1.set_ylabel("$(J-H)_{Observed}$",fontsize=20)
f6s1.tick_params(axis='both',pad=7)
plt.savefig('figure6.png')

############
# FIGURE 7 #
############
plt.figure(7)

f7s1.tick_params(axis='both',pad=7)
f7s2.tick_params(axis='both',pad=7)
f7s3.tick_params(axis='both',pad=7)
f7s3.set_xlabel(r"$\xi[I,H]$",fontsize=20)
f7s2.set_ylabel("N",fontsize=20)
plt.savefig('figure7.png')

############
# FIGURE 8 #
############
plt.figure(8)

f8s1.tick_params(axis='both',pad=7)
f8s2.tick_params(axis='both',pad=7)
f8s3.tick_params(axis='both',pad=7)
f8s3.set_xlabel(r"$\xi[Z,H]$",fontsize=20)
f8s2.set_ylabel("N",fontsize=20)
plt.savefig('figure8.png')

############
# FIGURE 9 #
############
plt.figure(9)

f9s1.tick_params(axis='both',pad=7)
f9s2.tick_params(axis='both',pad=7)
f9s3.tick_params(axis='both',pad=7)
f9s3.set_xlabel(r"$\xi[J,H]$",fontsize=20)
f9s2.set_ylabel("N",fontsize=20)
plt.savefig('figure9.png')

#pp.close()
plt.show()	
