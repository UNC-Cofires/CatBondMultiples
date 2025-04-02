import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# this script plots cat bond multiple timeseries,
# using color to denote the expected loss of the bond
fig, ax = plt.subplots()

# read cat bond data
cat_bond_data = pd.read_csv('corrected_cat_bond_data.csv', index_col = 0)
# set datetime index
cat_bond_data.index = pd.to_datetime(cat_bond_data.index)

# cutoffs for plotting 'groups', along with colors to plot
cutoffs = [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03]
colors_lines = ['crimson', 'darkorange', 'yellow', 'steelblue', 'green', 'purple', 'navy']

# loop through cutoffs
for idx in range(0, len(cutoffs)):
  # find only cat bonds that fit into cutoff grup
  if idx == len(cutoffs) - 1:
    el_band = cat_bond_data['Expected Loss'] >= cutoffs[idx]
    label_use = '> '+ str(int(cutoffs[idx]*1000)/10) +'% EL'
  else:
    el_band = np.logical_and(cat_bond_data['Expected Loss'] >= cutoffs[idx], cat_bond_data['Expected Loss'] < cutoffs[idx + 1])
    label_use = '> ' + str(int(cutoffs[idx]*1000)/10) + '% & < ' + str(int(cutoffs[idx + 1]*1000)/10) + '% EL'
  loss_class = cat_bond_data[el_band]
  
  # calculate multiples
  multiples = loss_class['Coupon Rate']/loss_class['Expected Loss']
  # plot + format
  ax.plot(loss_class.index, multiples, color = colors_lines[idx], marker = 'o', linewidth = 0.0, label = label_use, alpha = 0.4)
  ax.set_ylim([0, 15.0])
  ax.set_ylabel('Cat Bond Multiple')
  ax.legend()
plt.show()