import numpy as np;
import pandas as pd;
from scipy import stats;
from matplotlib import pyplot as plot;

jared_data = pd.read_csv('jared-data.csv');

# Read in cost per click data
jared_cost_per_click = jared_data['price_per_click'];

# Use scipy to calculate the median age of cost per click
mode_cost_per_click = stats.mode(jared_cost_per_click);
mode_cost_per_click_raw = mode_cost_per_click[0][0];
mode_cost_per_click_amount = mode_cost_per_click[1][0];
median_cost_per_click = np.median(jared_cost_per_click);
mean_cost_per_click = np.average(jared_cost_per_click);

print(
	"The mode = " + str(mode_cost_per_click_raw) +
	", amout of times it occurs = " + str(mode_cost_per_click_amount) +
	", the mean = " + str(round(mean_cost_per_click, 3)) +
	", the median = " + str(round(median_cost_per_click, 3))
);

plot.hist(jared_cost_per_click, range=(0.000, 0.200), bins=14, edgecolor='red');
plot.title("Jared's cost per piece data");
plot.xlabel("Price Per Piece");
plot.ylabel("Count");
plot.axvline(
	mean_cost_per_click, color='r', linestyle='solid', linewidth=3, label="Mean"
);
plot.axvline(
	median_cost_per_click, color='y', linestyle='dotted', linewidth=3, label="Median"
);
plot.axvline(
	mode_cost_per_click_raw, color='orange', linestyle='dashed', linewidth=3, label="Mode"
);
plot.legend();
plot.show();




##
