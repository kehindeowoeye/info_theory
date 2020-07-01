
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg',warn=False, force=True)
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_excel('leoacc.xls')
dataset1 = pd.read_csv('allofme.csv',header=None)

gg = [0,24.8274709796276, 9.76419549099265, 7.53316938572087, 23.4590014305755, 44.4636735316916, 78.0303946542421 ,61.8847035897775 ,49.3465899044765, 11.9003503796810 ,10.1202202779346 ,37.0456302575635 ,18.4545898018475 ,14.8592370544505 ,15.8318086320045, 9.87225665128495 ,12.0219222215805 ,63.5652950177032 ,56.7283647065929, 88.8540541570796, 85.0251547752903 ,19.2181606535386, 10.3009034009990, 22.5782512333683 ,26.6221039152842 ,34.0264788367751 , 8.12363526794107 ,14.5215363931191, 54.7535827555964 ,77.6473023628699 ,49.4080237529207 ,53.1099463187654, 11.8682649132475 ,22.5236110934979, 28.7416735723136 ,33.1915264150978, 20.7602157292723]


#mean_difference
gg1 = [0, 0.0648923343852, 1.04844913928, 6.4635828797, 1.13730365035, -1.15746491145, -1.20085456363, -1.31105193218, -1.30338627833, 5.51893489126, 3.75341849248, 0.579020658842, -1.13307376036, -0.75154490437, 2.05562710867, 7.70832975761, 0.692733655318, -0.916917832791, -1.20255970786, -1.08800776086, -0.982089638165, 4.54795882395, 4.63159306776, 0.15747960584, 1.1780898053, -0.545597827449, 6.63931286326, 2.63646666493, -1.08251166183, -1.21859785505, -1.0923756016, -1.69949298098, 7.50272903689, 1.80261648754, -0.020516994692, -1.14533771252, -0.236517461612]


#earthmovers
gg2 = [0, 4.681003094, 14.26696873,2.345355034,7.666278839,3.24113822,2.935671329,3.59589529,4.316565514,2.037414789,1.723061919,3.790375471,3.41133523,8.087892532,3.802878141,2.5105474,17.3896389,3.101680756,3.171005964,3.633864164,4.244091511,3.284430504,1.057719946,6.821717262,3.05200839,3.782210827,3.540627956,12.95762825,3.901407957,3.416476488,3.610556602,2.079312563,1.266817689,3.694871902,9.416055679,3.566326618,5.360048771]




fig = plt.figure()


ax1 = fig.add_subplot(411)
ax1.plot((dataset[667:24642]))
x_tick_labels = ['Apr', 'Dec', 'Apr', 'Dec', 'Apr', 'Dec']
ax1.set_ylabel('Dist. covered(Km)')
#ax1.set_xticks([1998,7326,9990,15318,17982,23310])
ax1.set_xticks([2664,7992,10656,15984,18648,23976])
ax1.set_xticklabels(x_tick_labels)

for label in ax1.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)



ax2 = fig.add_subplot(412)
ax2.plot(gg[1:len(gg)])
x_tick_labels = ['Apr', 'Dec', 'Apr', 'Dec', 'Apr', 'Dec']
ax2.set_xticks([3 ,11, 15, 23, 27,  35])
ax2.set_xticklabels(x_tick_labels)

for label in ax2.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax2.set_xlabel('Month of the Year')
ax2.set_ylabel('KL Div.')
fig.subplots_adjust(hspace=0.5)

ax3 = fig.add_subplot(413)
ax3.plot(gg1[1:len(gg)])
ax3.set_xticks([3 ,11, 15, 23, 27,  35])
ax3.set_xticklabels(x_tick_labels)
#ax3.set_xlabel('Month of the Year')
ax3.set_ylabel('Mean difference')
fig.subplots_adjust(hspace=0.5)

ax4 = fig.add_subplot(414)
ax4.plot(gg2[1:len(gg)])
ax4.set_xticks([3 ,11, 15, 23, 27,  35])
ax4.set_xticklabels(x_tick_labels)
for label in ax4.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax4.set_xlabel('Month of the Year')
ax4.set_ylabel('EMD')
fig.subplots_adjust(hspace=0.5)
plt.savefig('tkvulturedivergence.eps',format='eps',dpi=1000)

plt.show()
 
ax1.plot((dataset[667:24642]))
ax2.plot(gg)
ax3.plot(gg1)
ax4.plot(gg2)

plt.show()




dataset1 = pd.read_csv('allofme.csv',header=None)
fig = plt.figure()

x_tick_labels = ['Apr', 'Dec', 'Apr', 'Dec', 'Apr', 'Dec']
ax1 = fig.add_subplot(4 ,3 ,1)
ax1.plot(dataset1.iloc[:,0])
ax1.set_xticks([3 ,11, 15, 23, 27,  35])
ax1.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax1.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax1.set_ylabel('KL Div.')
ax1.set_title("(A)",y=-0.09)
#ax1.set_xlabel('Month of the Year')
#plt.savefig('feb.eps',format='eps',dpi=1000)

#fig = plt.figure()
ax2 = fig.add_subplot(4 ,3 ,2)
ax2.plot(dataset1.iloc[:,1])
ax2.set_xticks([3 ,11, 15, 23, 27,  35])
ax2.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax2.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax2.set_ylabel('KL Div.')
ax2.set_title("(B)",y=-0.09)
#ax2.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=3.0)
#plt.savefig('mar.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax3 = fig.add_subplot(4 ,3 ,3)
ax3.plot(dataset1.iloc[:,2])
ax3.set_xticks([3 ,11, 15, 23, 27,  35])
ax3.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax3.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax3.set_ylabel('KL Div.')
ax3.set_title("(C)",y=-0.09)
#ax3.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('apr.eps',format='eps',dpi=1000)

#fig = plt.figure()
ax4 = fig.add_subplot(4 ,3 ,4)
ax4.plot(dataset1.iloc[:,3])
ax4.set_xticks([3 ,11, 15, 23, 27,  35])
ax4.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax4.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax4.set_ylabel('KL Div.')
ax4.set_title("(D)",y=-0.09)
#ax4.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('may.eps',format='eps',dpi=1000)


#fig = plt.figure()
ax5 = fig.add_subplot(4 ,3 ,5)
ax5.plot(dataset1.iloc[:,4])
ax5.set_xticks([3 ,11, 15, 23, 27,  35])
ax5.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax5.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax5.set_ylabel('KL Div.')
ax5.set_title("(E)",y=-0.09)
#ax5.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('jun.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax6 = fig.add_subplot(4 ,3 ,6)
ax6.plot(dataset1.iloc[:,5])
ax6.set_xticks([3 ,11, 15, 23, 27,  35])
ax6.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax6.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax6.set_ylabel('KL Div.')
ax6.set_title("(F)",y=-0.09)
#ax6.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('jul.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax7 = fig.add_subplot(4 ,3 ,7)
ax7.plot(dataset1.iloc[:,6])
ax7.set_xticks([3 ,11, 15, 23, 27,  35])
ax7.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax7.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax7.set_ylabel('KL Div.')
ax7.set_title("(G)",y=-0.09)
#ax7.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('aug.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax8 = fig.add_subplot(4 ,3 ,8)
ax8.plot(dataset1.iloc[:,7])
ax8.set_xticks([3 ,11, 15, 23, 27,  35])
ax8.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax8.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax8.set_ylabel('KL Div.')
ax8.set_title("(H)",y=-0.09)
#ax8.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('sep.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax9 = fig.add_subplot(4 ,3 ,9)
ax9.plot(dataset1.iloc[:,8])
ax9.set_xticks([3 ,11, 15, 23, 27,  35])
ax9.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax9.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax9.set_ylabel('KL Div.')
ax9.set_title("(I)",y=-0.09)
#ax9.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('oct.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax10 = fig.add_subplot(4 ,3, 10)
ax10.plot(dataset1.iloc[:,9])
ax10.set_xticks([3 ,11, 15, 23, 27,  35])
ax10.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax10.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
ax10.set_ylabel('KL Div.')
ax10.set_title("(J)",y=-0.09)
#ax10.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)
#plt.savefig('nov.eps',format='eps',dpi=1000)

#fig = plt.figure()

ax11 = fig.add_subplot(4, 3 ,11)
ax11.plot(dataset1.iloc[:,10])
ax11.set_xticks([3 ,11, 15, 23, 27,  35])
ax11.set_xticklabels(x_tick_labels,fontsize=6)
for label in ax11.yaxis.get_ticklabels()[::2]:
    label.set_visible(False)
#ax11.set_ylabel('KL Div.')
ax11.set_title("(K)",y=-0.09)
#ax11.set_xlabel('Month of the Year')
fig.subplots_adjust(hspace=0.5)

plt.savefig('other_eleven.eps',format='eps',dpi=1000)


plt.show()














