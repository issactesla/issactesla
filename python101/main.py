import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlob as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()






