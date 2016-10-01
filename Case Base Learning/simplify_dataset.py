# open required files
import pandas as pd
import numpy as np

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/answer1_9.csv'

df = pd.read_csv(file_name)
print "DONE Reding CSV"

result = df[['id','Demanda_uni_equil']]
result.to_csv('G:/Academic/Data Mining/Bimbo/Training Set/simpified_answer9.csv',index = False)
#for df in pd.read_csv(file_name,sep=',', header = None, chunksize=1):
 #   print df.as_matrix()
'''
file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek4.csv'

df = pd.read_csv(file_name)
print "DONE Reding CSV"

result = df[['Canal_ID','Ruta_SAK','Producto_ID','Cliente_ID','Agencia_ID','Demanda_uni_equil']]
result.to_csv('G:/Academic/Data Mining/Bimbo/Training Set/simplifiedWeek4.csv',index = False)

print 'Success'

#'Ruta_SAK','Producto_ID','Cliente_ID','Agencia_ID'
'''