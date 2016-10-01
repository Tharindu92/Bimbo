import csv

readFile4 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek8_9_2.csv'

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer2_9.csv'

readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer3_9.csv'


medianFile2 = open(readFile4,'r')
test = open(readTest,'r')

answerFile = open(writeFile,'w')
answerFile.write('Canal_ID,Ruta_SAK,Producto_ID,Cliente_ID,Agencia_ID,id,Demanda_uni_equil\n')

testReader = csv.reader(test, delimiter=',', quotechar='\n')
count = 0
count2 = 1
prevRow = []
rowMedian5 = []
print 'read test file'

for row in testReader:
    answer = -1
    if not row[0] == 'Canal_ID':
        if(count == 0):
            prevRow = row
            rowMedian5 = ['1', '900', '29']
        if row[6] != '-1':
            rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
            answerFile.write(rowString)
            count = count + 1
            continue
        '''
        if row[0] == prevRow[0] and \
           row[1] == prevRow[1] and \
           row[2] == prevRow[2] and \
           count > 0:
            if(count == 1096):
                print row
                print prevRow
            answer = prevRow[6]
            rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
            answerFile.write(rowString)
            count = count + 1
            continue
        #medianFile5.seek(0) '''
        if not rowMedian5 == []:

            if row[0] == rowMedian5[0] and \
               row[1] == rowMedian5[1]:
                answer = rowMedian5[2]
                rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                    row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
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

        medianReader4 = csv.reader(medianFile2 ,delimiter=',', quotechar='\n')
        for rowMedian5 in medianReader4:
            if not rowMedian5[0] == 'Canal_ID':
                if row[0] == rowMedian5[0] and \
                   row[1] == rowMedian5[1]:
                    answer = rowMedian5[2]
                    break
                elif row[0] == rowMedian5[0] and \
                   int(row[1]) < int(rowMedian5[1]):
                    break
                elif int(row[0]) < int(rowMedian5[0]):
                    break
                else:
                    count2 = count2 + 1
        rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]) + ',' + str(row[5]) + ',' +   str(answer)+ '\n'
        answerFile.write(rowString)
        count = count + 1
        prevRow = row
        if(count == 10):
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
        if(count % 1000000 == 0):
            print str(count)

print 'Success'
