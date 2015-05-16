import random
import pylab

# Global Variables
MAXRABBITPOP, CURRENTRABBITPOP, CURRENTFOXPOP = 1000, 500, 30
# MAXRABBITPOP, CURRENTRABBITPOP, CURRENTFOXPOP = 1000, 50, 300


def rabbitGrowth():
    """ rabbitGrowth is called once at the beginning of each time step.
        It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.
        The global variable CURRENTRABBITPOP is modified by this procedure.
        For each rabbit, based on the probabilities in the problem set write-up,
          a new rabbit may be born.
        Nothing is returned.
    """
    global CURRENTRABBITPOP

    for r in range(CURRENTRABBITPOP):
        rabb_repr_prob = 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)
        if random.random() < rabb_repr_prob:
            # print('Rabbit born: {}'.format(round(rabb_repr_prob, 2)))
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ foxGrowth is called once at the end of each time step.
        It makes use of the global variables: CURRENTFOXPOP & CURRENTRABBITPOP,
            and both may be modified by this procedure.
        Each fox, based on the probabilities in the problem statement, may eat
          one rabbit (but only if there are more than 10 rabbits).
        If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.
        If it does not eat a rabbit, then with a 1/10 prob it dies.
        Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for f in range(CURRENTFOXPOP):
        fox_eats_prob = CURRENTRABBITPOP/float(MAXRABBITPOP)
        if random.random() < fox_eats_prob and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            prob_fox_repr = 1 / float(3)
            if random.random() < prob_fox_repr:
                CURRENTFOXPOP += 1
        else:
            prob_fox_dies = 1 / float(10)
            # prob_fox_dies = 9 / float(10)
            if random.random() < prob_fox_dies and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """ Runs the simulation for `numSteps` time steps.
        Returns a tuple of two lists: (rabbit_populations, fox_populations)
          where rabbit_populations is a record of the rabbit population at the
          END of each time step, and fox_populations
          is a record of the fox population at the END of each time step.
        Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for i in range(numSteps):
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)


def plotPopulations(numSteps):
    """ Plots populations of Foxes & Rabbits for given timesteps. """
    rab_pop, fox_pop = runSimulation(numSteps)
    # for i in range(len(rab_pop)):
    #     print(rab_pop[i], fox_pop[i])

    r_style = 'bo'    # blue - continuous line
    f_style = 'ro'    # red  - continuous line

    pylab.figure('Fox / Rabit Populations')

    pylab.plot(rab_pop, r_style, label='Rabbit Pop')
    pylab.plot(fox_pop, f_style, label='Fox Pop')

    pylab.title('Fox / Rabit Populations: {} timesteps'.format(numSteps))
    pylab.xlabel('Time Steps')
    pylab.ylabel('Population')
    pylab.legend(loc='best')

    degree = 2
    rab_coeff = pylab.polyfit(range(len(rab_pop)), rab_pop, degree)
    pylab.plot(pylab.polyval(rab_coeff, range(len(rab_pop))), 'b-')
    fox_coeff = pylab.polyfit(range(len(fox_pop)), fox_pop, degree)
    pylab.plot(pylab.polyval(fox_coeff, range(len(fox_pop))), 'r-')

    pylab.show()

if __name__ == '__main__':
    numSteps = 200
    plotPopulations(numSteps)
