# open required files
import pandas as pd
import numpy as np

df = pd.read_csv('G:/Academic/Data Mining/Bimbo/Training Set/simpified_answer9.csv')
print "DONE Reding CSV"

result = df.sort('id')
result.to_csv('G:/Academic/Data Mining/Bimbo/Training Set/sortedAnswer9.csv',index = False)

print 'Success'