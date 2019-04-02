import numpy as np;
import pandas as pd;

from matplotlib import pyplot as plt;

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




# end of file