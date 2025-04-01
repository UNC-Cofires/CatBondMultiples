# CatBondMultiples
For analysis of cat bond data

## Getting Started
 This script uses data from the artemis cat bond deal directory
 * (https://www.artemis.bm/deal-directory/)    
 Data transcribed into the file cat_bond_database.xlsx by William Ratcliffe
 

### Dependencies

Python Libraries:

* numpy
* pandas
* datetime
* matplotlib

### Executing program

To fix date index on cat_bond_database.xlsx, run:   

```
python -W ignore fix_datetime_index.py
```
This will create corrected_cat_bond_data.csv, which is used to make figures by running:

```
python -W ignore plot_cat_bond_data.py 2024
```

