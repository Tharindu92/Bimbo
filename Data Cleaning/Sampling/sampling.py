# open required files
# CHANGE THE SOURCE ADDRESSES ACCORDING TO YOUR LOCATION

trainingData = open('G:/Academic/Data Mining/Bimbo/Training Set/train.csv', 'r')
week3 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek3.csv', 'a')
week4 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek4.csv', 'a')
week5 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek5.csv', 'a')
week6 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek6.csv', 'a')
week7 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek7.csv', 'a')
week8 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek8.csv', 'a')
week9 = open('G:/Academic/Data Mining/Bimbo/Training Set/trainWeek9.csv', 'a')

# insert column names at the top of the file

line = 'Semana,Agencia_ID,Canal_ID,Ruta_SAK,Cliente_ID,Producto_ID,Venta_uni_hoy,Venta_hoy,Dev_uni_proxima,Dev_proxima,Demanda_uni_equil\n'

week3.write(line)
week4.write(line)
week5.write(line)
week6.write(line)
week7.write(line)
week8.write(line)
week9.write(line)

for line in trainingData:
    if not line.startswith("S"):
        # options[int(line[0])]()
        if line[0] == '3':
            week3.write(line)
        elif line[0] == '4':
            week4.write(line)
        elif line[0] == '5':
            week5.write(line)
        elif line[0] == '6':
            week6.write(line)
        elif line[0] == '7':
            week7.write(line)
        elif line[0] == '8':
            week8.write(line)
        elif line[0] == '9':
            week9.write(line)

print 'Success'

