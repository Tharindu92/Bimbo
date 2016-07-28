# open required files
week3 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek3.csv', 'r')
week4 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek4.csv', 'r')
week5 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek5.csv', 'r')
week6 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek6.csv', 'r')
week7 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek7.csv', 'r')
week8 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek8.csv', 'r')
week9 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek9.csv', 'r')

cleanedWeek3 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek3.csv', 'a')
cleanedWeek4 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek4.csv', 'a')
cleanedWeek5 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek5.csv', 'a')
cleanedWeek6 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek6.csv', 'a')
cleanedWeek7 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek7.csv', 'a')
cleanedWeek8 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek8.csv', 'a')
cleanedWeek9 = open('G:/Academic/Data Mining/Bimbo/Training Set/cleanedTrainWeek9.csv', 'a')

# insert column names at the top of the file

line = 'Semana,Agencia_ID,Canal_ID,Ruta_SAK,Cliente_ID,Producto_ID,Venta_uni_hoy,Venta_hoy,Dev_uni_proxima,Dev_proxima,Demanda_uni_equil\n'

cleanedWeek3.write(line)
cleanedWeek4.write(line)
cleanedWeek5.write(line)
cleanedWeek6.write(line)
cleanedWeek7.write(line)
cleanedWeek8.write(line)
cleanedWeek9.write(line)

for line in week3:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek3.write(line)

for line in week4:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek4.write(line)

for line in week5:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek5.write(line)

for line in week6:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek6.write(line)

for line in week7:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek7.write(line)

for line in week8:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek8.write(line)

for line in week9:
     if not line.startswith("S"):
        data = line.split(',')
        if ((int(data[6]) - int(data[8]) == int(data[10]))):
            cleanedWeek9.write(line)

print 'Success'

