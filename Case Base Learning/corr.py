import pandas as pd
import numpy as np

df = pd.read_csv('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek3.csv')
print "DONE Reding CSV"

print(df.corr())