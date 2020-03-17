import sys
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def exponential(x, a, b):
    return a * np.exp(b * x)

def graph(func, x_range, color, curr_popt):
   x = np.arange(*x_range)
   y = func(x)
   plt.plot(x, y, color, label='a=%5.6f, b=%5.6f' % tuple([curr_popt[0], curr_popt[1]]))


days = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
infections = np.array([2, 4, 6, 9, 13, 21, 30, 39, 41, 59, 78, 112, 169, 245,
                       331, 448])

day = int(sys.argv[1]) + 1

axes = plt.gca()
axes.set_xlim([0, 30])
axes.set_ylim([0, 1000])
axes.set_title('Day ' + str(day - 1) + ' since 1st infection')

popt, pcov = curve_fit(exponential, days[0:day], infections[0:day])

graph(lambda x: popt[1] * (np.power(x, popt[0])), (0,30), 'b', popt)

exp_popt = [2.718281828459045235360287471352662497757247093, 1]

graph(lambda x: 1 * np.power(x, 2.718281828459045235360287471352662497757247093), (0, 30), 'g', exp_popt)

plt.xlabel('Days since 1st infection')
plt.ylabel('Number of confirmed infections')
plt.grid(True)
plt.legend()
plt.savefig('graphics/day_' + str(day - 1) + '.png')

