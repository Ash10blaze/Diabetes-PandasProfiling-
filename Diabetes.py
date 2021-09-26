#importing libraries
import pandas as pd 
from pandas_profiling import ProfileReport
#reading the csv file
data=pd.read_csv('diabetes_data.csv')
print(data)

#generating report 
profile=ProfileReport(data)
profile.to_file(output_file="diabetesinfo.html")