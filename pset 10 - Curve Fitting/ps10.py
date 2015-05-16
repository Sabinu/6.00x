# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps09 import *

pylab.rcParams['lines.linewidth']  =  2  # set line width
pylab.rcParams['axes.titlesize']   = 10  # set font size for titles
pylab.rcParams['axes.labelsize']   = 10  # set font size for labels on axes
pylab.rcParams['xtick.major.size'] =  2  # set size of numbers on x-axis
pylab.rcParams['ytick.major.size'] =  2  # set size of numbers on y-axis
pylab.rcParams['font.family'] = 'Verdana'


# PROBLEM 1
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    numViruses = [100, 100, 100, 100]
    # numViruses = [100, 200, 300, 400]

    maxPop = [1000, 1000, 1000, 1000]
    # maxPop = [1000, 1500, 2000, 2500]

    maxBirthProb = [0.1, 0.1, 0.1, 0.1]
    # maxBirthProb = [0.1, 0.2, 0.3, 0.4]

    clearProb = [0.05, 0.05, 0.05, 0.05]
    # clearProb = [0.05, 0.10, 0.15, 0.20]

    time_before = [300, 150, 75, 0]
    # time_before = [150, 150, 150, 150]

    time_after = 150

    time_steps = [v + time_after for v in time_before]

    for condition in range(4):
        popul = [0 for i in range(time_steps[condition])]
        f_pop = []
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb = maxBirthProb[condition],
                                      clearProb    = clearProb[condition],
                                      resistances  = {'guttagonol': False},
                                      mutProb      = 0.005)
                for i in range(numViruses[condition])]
            pat = TreatedPatient(viruses=viruses, maxPop=maxPop[condition])

            for t in range(time_before[condition]):
                popul[t] += pat.update()
            pat.addPrescription('guttagonol')

            t_after = [t + time_before[condition] for t in range(time_after)]
            for t in t_after:
                final_pop = pat.update()
                popul[t] += final_pop
                if t == time_steps[condition] - 1:
                    f_pop.append(final_pop)

        pylab.figure('Histograms')
        pylab.subplot(2, 2, condition+1)
        pylab.title('Delayed Treatment: {}'.format(time_before[condition]))
        pylab.hist(f_pop, bins=50, label='{}'.format(time_before[condition]))
        pylab.xlabel('total virus population')
        pylab.ylabel('trials'.format(numTrials))
        pylab.legend(loc='best')

        pylab.figure('Graphs')
        means = [p/numTrials for p in popul]
        pylab.subplot(2, 2, condition+1)
        pylab.title('Delayed Treatment: {}'.format(time_before[condition]))
        pylab.plot(means, 'r-', label = 'Virus Pop')
        pylab.xlabel('Time Steps')
        pylab.ylabel('Virus Population')
        pylab.legend(loc='best')
    pylab.show()


# PROBLEM 2
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = [100, 100, 100, 100]
    maxPop = [1000, 1000, 1000, 1000]
    maxBirthProb = [0.1, 0.1, 0.1, 0.1]
    clearProb = [0.05, 0.05, 0.05, 0.05]
    time_inter = [300, 150, 75, 0]
    time_bafter = 150

    time_steps = [v + 2 * time_bafter for v in time_inter]

    for condition in range(4):
        popul = [0 for i in range(time_steps[condition])]
        f_pop = []
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb = maxBirthProb[condition],
                                      clearProb    = clearProb[condition],
                                      resistances  = {'guttagonol': False,
                                                      'grimpex':    False},
                                      mutProb      = 0.005)
                for i in range(numViruses[condition])]
            pat = TreatedPatient(viruses=viruses, maxPop=maxPop[condition])

            for t in range(time_bafter):
                popul[t] += pat.update()
            pat.addPrescription('guttagonol')

            t_after_1 = [t + time_bafter for t in range(time_inter[condition])]
            for t in t_after_1:
                popul[t] += pat.update()
            pat.addPrescription('grimpex')

            t_after_2 = [t + time_bafter + time_inter[condition] for t in range(time_bafter)]
            for t in t_after_2:
                final_pop = pat.update()
                popul[t] += final_pop
                if t == time_steps[condition] - 1:
                    f_pop.append(final_pop)

        pylab.figure('Histograms')
        pylab.subplot(2, 2, condition+1)
        pylab.title('Delayed Treatment: {}'.format(time_inter[condition]))
        pylab.hist(f_pop, bins=50, label='{}'.format(time_inter[condition]))
        pylab.xlabel('total virus population')
        pylab.ylabel('trials'.format(numTrials))
        pylab.legend(loc='best')

        pylab.figure('Graphs')
        means = [p/numTrials for p in popul]
        pylab.subplot(2, 2, condition+1)
        pylab.title('Delayed Treatment: {}'.format(time_inter[condition]))
        pylab.plot(means, 'r-', label = 'Virus Pop')
        pylab.xlabel('Time Steps')
        pylab.ylabel('Virus Population')
        pylab.legend(loc='best')
    pylab.show()

if __name__ == '__main__':
    # simulationDelayedTreatment(50)
    # simulationTwoDrugsDelayedTreatment(150)
    pass