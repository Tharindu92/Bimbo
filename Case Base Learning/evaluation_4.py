import csv

readFile4 = 'G:/Academic/Data Mining/Bimbo/Training Set/medianDemandWeek8_9_4.csv'

writeFile = 'G:/Academic/Data Mining/Bimbo/Training Set/answer4_9.csv'

readTest = 'G:/Academic/Data Mining/Bimbo/Training Set/answer5_9.csv'

medianFile4 = open(readFile4,'r')
test = open(readTest,'r')

answerFile = open(writeFile,'w')
answerFile.write('Canal_ID,Ruta_SAK,Producto_ID,Cliente_ID,Agencia_ID,id,Demanda_uni_equil\n')

testReader = csv.reader(test, delimiter=',', quotechar='\n')
count = 0
count2 = 1
prevRow = []
rowMedian5 = ['1','900','72','1327212','19']
print 'read test file'

for row in testReader:
    answer = -1
    if not row[0] == 'Canal_ID':
        if count == 30:
            print row
            print rowMedian5
        if(count == 0):
            prevRow = row
        if row[6] != '-1':
            rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + '\n'
            answerFile.write(rowString)
            count = count + 1
            continue
        '''if row[0] == prevRow[0] and \
           row[1] == prevRow[1] and \
           row[2] == prevRow[2] and \
           row[3] == prevRow[3] and \
           count > 0:
            answer = row[6]
            rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
            answerFile.write(rowString)
            count = count + 1
            continue
        #medianFile5.seek(0) '''
        if not rowMedian5 == []:

            if row[0] == rowMedian5[0] and \
               row[1] == rowMedian5[1] and \
               row[2] == rowMedian5[2] and \
               row[3] == rowMedian5[3]:
                answer = rowMedian5[4]
                rowString = str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(
                    row[4]) + ',' + str(row[5]) + ',' + str(answer) + '\n'
                answerFile.write(rowString)
                count = count + 1
                continue
            elif row[0] == rowMedian5[0] and \
               row[1] == rowMedian5[1] and \
               row[2] == rowMedian5[2] and \
               int(row[3] )< int(rowMedian5[3]):
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

        medianReader4 = csv.reader(medianFile4 ,delimiter=',', quotechar='\n')
        for rowMedian5 in medianReader4:
            if not rowMedian5[0] == 'Canal_ID':
                if count == 30:
                    print row
                    print rowMedian5
                if row[0] == rowMedian5[0] and \
                   row[1] == rowMedian5[1] and \
                   row[2] == rowMedian5[2] and \
                   row[3] == rowMedian5[3]:
                    answer = rowMedian5[4]
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
