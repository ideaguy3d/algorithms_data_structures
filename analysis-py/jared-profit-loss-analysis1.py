import numpy as np;
import pandas as pd;

from matplotlib import pyplot as plot;


jared_data = pd.read_csv('jared-data.csv');
jared_profit_loss = jared_data['profit_loss_amount'];
jared_profit_loss_mean = np.average(jared_profit_loss);
jared_median_profit_loss = np.median(jared_profit_loss);
jared_profit_loss_sorted = np.sort(jared_profit_loss);

print('jared first profit loss = ' + str(jared_profit_loss[1]));
print('jared profit loss mean = ' + str(round(jared_profit_loss_mean,2)));

print('jared median sale =');
print(jared_median_profit_loss);

print('jared sorted profit loss');
print(jared_profit_loss_sorted);

plot.hist(jared_profit_loss, range=(-10000, 10000), bins=20, edgecolor='red');
plot.title("Profit Loss data from Jareds' sales");
plot.xlabel('Sales Amount');
plot.ylabel('Count');
plot.axvline(
	jared_profit_loss_mean,
	color='r',
	linestyle='solid',
	linewidth=2,
	label="Mean"
);

plot.axvline(
	jared_median_profit_loss,
	color='g',
	linestyle='dotted',
	linewidth=2,
	label='Median'
);

plot.legend();

plot.show();

# end of file