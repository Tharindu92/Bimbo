import csv

readFile1 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek3_5.csv'
readFile2 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek4_5.csv'
readFile3 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek5_5.csv'
readFile4 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek6_5.csv'
readFile5 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek7_5.csv'
readFile6 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek8_5.csv'
readFile7 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek9_5.csv'

medianFile1 = open(readFile1,'r')
medianFile2 = open(readFile2,'r')
medianFile3 = open(readFile3,'r')
medianFile4 = open(readFile4,'r')
medianFile5 = open(readFile5,'r')
medianFile6 = open(readFile6,'r')
medianFile7 = open(readFile7,'r')

assign_row3 = ['1','900','72','1327212','22362','6']
assign_row4 = ['1','900','72','1327212','22362','24']
assign_row5 = ['1','900','72','1327212','22362','14']
assign_row6 = ['1','900','72','1327212','22362','13']
assign_row7 = ['1','900','72','1327212','22362','7']
assign_row8 = ['1','900','72','1327212','22362','23']
assign_row9 = ['1','900','72','1327212','22362','22']
print 'read test file'

def evaluate(medianFile, assign_row,weight,avg_weight,readTest,writeFile):
    answerFile = open(writeFile, 'w')
    answerFile.write('Canal_ID,Ruta_SAK,Producto_ID,Cliente_ID,Agencia_ID,id,Demanda_uni_equil\n')
    test = open(readTest, 'r')
    testReader = csv.reader(test, delimiter=',', quotechar='\n')
    count = 0
    prevRow = []
    rowMedian5 = []
    test.seek(0)
    for row in testReader:
        answer = -1
        if not row[0] == 'Canal_ID':
            if (count == 0):
                prevRow = row
                rowMedian5 = assign_row
            if (count == 0):
                prevRow = row
            if row[6] != '-1':
                answer = int(row[6]) + int(rowMedian5[5])  / 2
                rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                    row[4]) + ',' + str(row[5]) + ',' + str(int(answer)) + '\n'
                answerFile.write(rowString)
                count = count + 1
                continue
            '''if row[0] == prevRow[0] and \
                            row[1] == prevRow[1] and \
                            row[2] == prevRow[2] and \
                            row[3] == prevRow[3] and \
                            row[4] == prevRow[4] and \
                            count > 0:
                answer = rowMedian5[5]
                rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                    row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
                answerFile.write(rowString)
                count = count + 1
                continue
            # medianFile5.seek(0)
            '''
            if not rowMedian5 == []:

                if row[0] == rowMedian5[0] and \
                                row[1] == rowMedian5[1] and \
                                row[2] == rowMedian5[2] and \
                                row[3] == rowMedian5[3] and \
                                row[4] == rowMedian5[4]:
                    answer = rowMedian5[5]
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
                elif row[0] == rowMedian5[0] and \
                                row[1] == rowMedian5[1] and \
                                row[2] == rowMedian5[2] and \
                                row[3] == rowMedian5[3] and \
                                int(row[4]) < int(rowMedian5[4]):
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
                elif row[0] == rowMedian5[0] and \
                                row[1] == rowMedian5[1] and \
                                row[2] == rowMedian5[2] and \
                                int(row[3]) < int(rowMedian5[3]):
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
                elif row[0] == rowMedian5[0] and \
                                row[1] == rowMedian5[1] and \
                                int(row[2]) < int(rowMedian5[2]):
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
                elif row[0] == rowMedian5[0] and \
                                int(row[1]) < int(rowMedian5[1]):
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
                elif int(row[0]) < int(rowMedian5[0]):
                    rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                        row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
                    answerFile.write(rowString)
                    count = count + 1
                    continue
            medianReader5 = csv.reader(medianFile, delimiter=',', quotechar='\n')
            for rowMedian5 in medianReader5:
                if not rowMedian5[0] == 'Canal_ID':
                    if row[0] == rowMedian5[0] and \
                                    row[1] == rowMedian5[1] and \
                                    row[2] == rowMedian5[2] and \
                                    row[3] == rowMedian5[3] and \
                                    row[4] == rowMedian5[4]:
                        answer = rowMedian5[5]
                        break
                    elif row[0] == rowMedian5[0] and \
                                    row[1] == rowMedian5[1] and \
                                    row[2] == rowMedian5[2] and \
                                    row[3] == rowMedian5[3] and \
                                    int(row[4]) < int(rowMedian5[4]):
                        break
                    elif row[0] == rowMedian5[0] and \
                                    row[1] == rowMedian5[1] and \
                                    row[2] == rowMedian5[2] and \
                                    int(row[3]) < int(rowMedian5[3]):
                        break
                    elif row[0] == rowMedian5[0] and \
                                    row[1] == rowMedian5[1] and \
                                    int(row[2]) < int(rowMedian5[2]):
                        break
                    elif row[0] == rowMedian5[0] and \
                                    int(row[1]) < int(rowMedian5[1]):
                        break
                    elif int(row[0]) < int(rowMedian5[0]):
                        break
            rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
            answerFile.write(rowString)
            count = count + 1
            prevRow = row
            if (count == 10):
                print str(count)
            if (count == 50):
                print str(count)
            if (count == 100):
                print str(count)
            if (count == 1000):
                print str(count)
            if (count == 10000):
                print str(count)
            if (count == 100000):
                print str(count)
            if (count % 1000000 == 0):
                print str(count)
    return
writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_3.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5.csv'
evaluate(medianFile1,assign_row3,1,1,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_4.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_3.csv'
evaluate(medianFile2,assign_row4,1.5,1,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_5.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_4.csv'
evaluate(medianFile3,assign_row5,2,1.25,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_6.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_5.csv'
evaluate(medianFile4,assign_row6,2.5,1.625,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_7.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_6.csv'
evaluate(medianFile5,assign_row7,3,2.0625,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_8.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_7.csv'
evaluate(medianFile6,assign_row6,3.5,2.53125,readTest,writeFile)

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_9.csv'
readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_8.csv'
evaluate(medianFile7,assign_row7,4,3.015625,readTest,writeFile)

print 'Success'
