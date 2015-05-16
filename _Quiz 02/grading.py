import random
import pylab

pylab.rcParams['lines.linewidth']  =  2  # set line width
pylab.rcParams['axes.titlesize']   = 10  # set font size for titles
pylab.rcParams['axes.labelsize']   = 10  # set font size for labels on axes
pylab.rcParams['xtick.major.size'] =  2  # set size of numbers on x-axis
pylab.rcParams['ytick.major.size'] =  2  # set size of numbers on y-axis
pylab.rcParams['font.family'] = 'Verdana'

def sampleQuizzes():
    trials = 10000
    count = 0
    for t in range(trials):
        mid_1 = random.randint(50, 80)
        mid_2 = random.randint(60, 90)
        final = random.randint(55, 95)

        final_grade = mid_1 * 0.25 + mid_2 * 0.25 + final * 0.50

        if final_grade >= 70 and final_grade <= 75:
            count += 1

    return round(count / float(trials), 2)


def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """
    scores = []
    for t in range(numTrials):
        mid_1 = random.randint(50, 80)
        mid_2 = random.randint(60, 90)
        final = random.randint(55, 95)
        final_grade = mid_1 * 0.25 + mid_2 * 0.25 + final * 0.50
        scores.append(final_grade)
    return scores

def plotQuizzez():
    scores = generateScores(10000)

    pylab.figure('plot Quizzez')
    pylab.title('Distribution of Scores')
    pylab.hist(scores, bins=7)
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

if __name__ == '__main__':
    # print(sampleQuizzes())
    plotQuizzez()