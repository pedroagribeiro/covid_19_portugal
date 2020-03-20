import sys
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


def exponential(x, a, b):
    return a * np.exp(b * x)

def graph(func, x_range, color, curr_popt):
   x = np.arange(*x_range)
   y = func(x)
   plt.plot(x, y, color, label='a=%5.6f, b=%5.6f' % tuple([curr_popt[0],
                                                           curr_popt[1]]))


day = int(sys.argv[1]) + 1

days = np.array(list(range(day)))


infecoes = pd.read_csv("confirmados.csv")



axes = plt.gca()
axes.set_xlim([0, 30])
axes.set_ylim([0, 10000])
axes.set_title('Day ' + str(day - 1) + ' since 1st infection')

popt, pcov = curve_fit(exponential, days[0:day], infecoes["Confirmados"][0:day])

graph(lambda x: popt[1] * (np.exp(x * popt[0])), (0,30, 0.01), 'b', popt)

exp_popt = [np.e, 1]

graph(lambda x: np.exp(x), (0, 30), 'g', exp_popt)

plt.xlabel('Days since 1st infection')
plt.ylabel('Number of confirmed infections')
plt.grid(True)
plt.legend()
plt.savefig('graphics/day_' + str(day - 1) + '.png')

