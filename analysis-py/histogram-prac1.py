import numpy as np
import pandas as panda
from matplotlib import pyplot as plot


jared_data = panda.read_csv('jared-data.csv')

cost_per_click = jared_data['price_per_click']

h = np.histogram(cost_per_click, range=(0,0.15), bins=3)

print(h)

plot.hist(cost_per_click, bins=15, range=(0.00,0.15), edgecolor='darkred')
plot.title('Cost Per Click')
plot.xlabel('Job CPC')
plot.ylabel('Count')
plot.show()






##