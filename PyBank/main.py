import os
import csv
import pandas as pd

csvpath = os.path.join('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyBank\\resources\\budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

data_file_df = pd.read_csv(csvpath)
data_file_df.head()

print (data_file_df.groupby('Date').nunique())