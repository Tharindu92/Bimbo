# open required files

'''import pandas as pd
import numpy as np
import csv
import math

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/sortedWeek3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek3.csv'

count = 0
csvFile = open(file_name,'r')
csvFile2 = open(file_name,'r')
medianDemandFile = open(write_file, 'w')
#with open(file_name,'rb') as csvFile:
reader = csv.reader(csvFile, delimiter=',', quotechar='\n')
prevRow = None

for row in reader:
    demandValues = []
    if (count == 0):
        count = count + 1
        rowString = 'Canal_ID,Ruta_SAK,Producto_ID,Cliente_ID,Agencia_ID,Demanda_uni_equil\n'
        medianDemandFile.write(rowString)
        continue
    elif (count == 1):
        count = count + 1
    else:
        if row[0] == prevRow[0] and \
           row[1] == prevRow[1] and \
           row[2] == prevRow[2] and \
           row[3] == prevRow[3] and \
           row[4] == prevRow[4]:
            continue
    reader2 = csv.reader(csvFile2, delimiter=',', quotechar='\n')
    demandValues.append(row[5])
    for row2 in reader2:
        #print row2
        if row[0] == row2[0] and \
           row[1] == row2[1] and \
           row[2] == row2[2] and \
           row[3] == row2[3] and \
           row[4] == row2[4]:
            #print row2
            demandValues.append(row2[5])
        break
    demandValues.sort()
    size = len(demandValues)
    if(size == 1):
        midVal = 0
    elif (size%2 == 0):
        midVal = (size/2) -1
    else:
        midVal = ((size + 1)/2) -1
    prevRow = row
    #print row
    #print size
    #print midVal
    #print demandValues
    row[5] = demandValues[midVal]
    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]) + ',' + str(row[5]) + '\n'
    medianDemandFile.write(rowString)


print 'Success'

#'Canal_ID','Ruta_SAK','Producto_ID','Cliente_ID','Agencia_ID' '''

import csv
import numpy as np

def splitCases (file_name, write_file,file_name2,weight,avg_weight):
    count = 0
    csvFile = open(file_name, 'r')
    csvFile2 = open(file_name2, 'r')
    medianDemandFile = open(write_file, 'w')
    # with open(file_name,'rb') as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='\n')
    prevRow = None

    for row in reader:
        demandValues = []
        if (count == 0):
            count = count + 1
            rowString = 'Canal_ID,Ruta_SAK,Producto_ID,Cliente_ID,Demanda_uni_equil\n'
            medianDemandFile.write(rowString)
            continue
        elif (count == 1):
            count = count + 1
        else:
            if row[0] == prevRow[0] and \
                            row[1] == prevRow[1] and \
                            row[2] == prevRow[2]:
                continue
        reader2 = csv.reader(csvFile2, delimiter=',', quotechar='\n')
        demandValues.append(int(row[3]))
        for row2 in reader2:
            # print row2
            if row[0] == row2[0] and \
                            row[1] == row2[1] and \
                            row[2] == row2[2]:
                # print row2
                demandValues.append(int(row2[3]))
        demandValues.sort()
        size = len(demandValues)
        if (size == 1):
            midVal = 0
        elif (size % 2 == 0):
            midVal = (size / 2) - 1
        else:
            midVal = ((size + 1) / 2) - 1
        prevRow = row
        # print row
        # print size
        # print midVal
        # print demandValues
        row[3] = demandValues[midVal]
        rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + '\n'
        medianDemandFile.write(rowString)
    return

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek3_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek3_4_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek4_3.csv'

splitCases(file_name, write_file,file_name2,1,1)

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek3_4_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek4_5_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek5_3.csv'

splitCases(file_name, write_file,file_name2,1.5,1)

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek4_5_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek5_6_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek6_3.csv'

splitCases(file_name, write_file,file_name2,2,1.25)

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek5_6_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek6_7_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek7_3.csv'

splitCases(file_name, write_file,file_name2,2.5,1.625)

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek6_7_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek7_8_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek8_3.csv'

splitCases(file_name, write_file,file_name2,3,2.0625)

file_name = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek7_8_3.csv'
write_file = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek8_9_3.csv'
file_name2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek9_3.csv'

splitCases(file_name, write_file,file_name2,3.5,2.53125)
#11065600

print 'Success'