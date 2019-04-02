import numpy as np;
import pandas as pd;

jared_data = pd.read_csv('jared-data.csv');
jared_profit_loss = jared_data['profit_loss_amount'];
jared_profit_loss_mean = np.average(jared_profit_loss);
jared_mean_sales = '';

x = 'hello ';
x += x;

print(x + 'world');
print('jared first sale = ' + str(jared_profit_loss[1]));
print('jared profit loss average = ' + str(jared_profit_loss_mean));









# end of file