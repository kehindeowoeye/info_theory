import numpy as np
import matplotlib.pyplot as plt




x3 = np.array([14.3609300000000,12.9309200000000,11.3753320000000,15.8505500000000,13.3773290000000,14.6710650000000])
x2 =np.array([9.58607, 8.79108, 7.970668, 7.33545, 9.005671, 9.495935]);
x2 = x2/5;
x3 = x3/6;
t = list(range(1,7))
ysize = [15,8,8,15,15,15]

my_xticks = ['1st','2nd','3rd','4th','5th','6th'];
#put.xtixks(t,my_xticks)


plt.xlim([0,7])
for i in range (0, len(x3)):
    plt.plot(t[i],x3[i], '-ob', label='Normal Sheep' ,markersize=ysize[i])

plt.plot(t, x3, linestyle="-", color="b")

for i in range (0, len(x3)):
    plt.plot(t[i],x2[i], '-or', label='Batten Sheep' ,markersize=ysize[i])

plt.plot(t, x2, linestyle="--", color="r")
plt.xlabel('Days')
plt.ylabel('Entropy(bits)')
plt.title('Mean variation in entropy over six days')
plt.xticks(t,my_xticks)

p1, = plt.plot(t, x3, linestyle="-", color="b")
p2, = plt.plot(t, x2, linestyle="--", color="r")
plt.legend([p1,p2],["Normal Sheep","Batten Sheep"])
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles,labels)

plt.savefig('f11.eps',format='eps',dpi=1000)
plt.show()








x3 = np.array([1525,1090,2227,1547,1605,2101])
x2 =np.array([2265, 2224, 3281, 5297, 2172, 2448]);

t = list(range(1,7))

my_xticks = ['1st','2nd','3rd','4th','5th','6th'];
#put.xtixks(t,my_xticks)


plt.xlim([0,7])
for i in range (0, len(x3)):
    plt.plot(t[i],x3[i], '-ob', label='Normal Sheep')

plt.plot(t, x3, linestyle="-", color="b")

for i in range (0, len(x3)):
    plt.plot(t[i],x2[i], '-or', label='Batten Sheep')

plt.plot(t, x2, linestyle="--", color="r")
plt.xlabel('Days')
plt.ylabel('Mean distance covered(m)')
plt.title('Mean distance covered over six days')
plt.xticks(t,my_xticks)

p1, = plt.plot(t, x3, linestyle="-", color="b")
p2, = plt.plot(t, x2, linestyle="--", color="r")
plt.legend([p1,p2],["Normal Sheep","Batten Sheep"])
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles,labels)

plt.savefig('f12.eps',format='eps',dpi=1000)
plt.show()




x3 = np.array([759,199,599,1107,1521,2110])
x2 =np.array([2400,1978,2210,9151,2010,3130]);

t = list(range(1,7))

my_xticks = ['1st','2nd','3rd','4th','5th','6th'];
#put.xtixks(t,my_xticks)


plt.xlim([0,7])
for i in range (0, len(x3)):
    plt.plot(t[i],x3[i], '-ob', label='Normal Sheep')

plt.plot(t, x3, linestyle="-", color="b")

for i in range (0, len(x3)):
    plt.plot(t[i],x2[i], '-or', label='Batten Sheep')

plt.plot(t, x2, linestyle="--", color="r")
plt.xlabel('Days')
plt.ylabel('Mean variance')
plt.title('Mean variance of distance covered over six days')
plt.xticks(t,my_xticks)



p1, = plt.plot(t, x3, linestyle="-", color="b")
p2, = plt.plot(t, x2, linestyle="--", color="r")
plt.legend([p1,p2],["Normal Sheep","Batten Sheep"])
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles,labels)

plt.savefig('f13.eps',format='eps',dpi=1000)
plt.show()


