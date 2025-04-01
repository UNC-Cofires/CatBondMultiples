import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# fix date index on the cat bond data file
# the issue is that the indices were entered as dates, but
# excel converted all the date years to 2025, and recorded the
# actual year as the date day-of-month. The index months are all corrected
# this script loads the data, rearranges the date, and rewrites the file

# read the excel file into a pandas DataFrame
cat_bond_data = pd.read_excel('cat_bond_database.xlsx', index_col = 0)
# convert the incorrect index values (string) to a datetime value
cat_bond_data.index = pd.to_datetime(cat_bond_data.index)
new_index = [] # save values for corrected index
for col in cat_bond_data:
  print(col)
for index, row in cat_bond_data.iterrows():
  # use index day-of-month (+2000) as the updated year
  # use index month as the updated month (this part is correct)
  # assign all index values a day-of-month of 1
  corrected_date = datetime.datetime(index.day + 2000, index.month, 1)
  new_index.append(corrected_date)

# create dataframe using corrected datetime index
corrected_dataframe = cat_bond_data.set_index(pd.Index(new_index))
# write to file
corrected_dataframe.to_csv('corrected_cat_bond_data.csv')