__author__ = 'Sabinu'

import pylab


#   Constant for Springy Bodies
def Kai(d, m):
    return (m * 9.81) / d

dist = [0.0865, 0.1015, 0.1106, 0.1279, 0.4416, 0.4304, 0.437]
mass = [0.1000, 0.1500, 0.2000, 0.2500, 0.9000, 0.9500, 1.000]

k = []

for i in range(len(dist)):
    k.append(Kai(dist[i], mass[i]))

for i in range(len(k)):
    print str(i) + ':', k[i]

pylab.hist(k, len(dist))
pylab.title('Mean = ' + str(sum(k) / len(k)))

pylab.figure()
pylab.plot(k)
pylab.title('Mean = ' + str(sum(k) / len(k)))

pylab.show()