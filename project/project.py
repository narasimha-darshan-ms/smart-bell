import csv
import pprint
with open('ODB.txt') as csvfile:
    readCSV = csv.reader(csvfile , delimiter=',')
    line = next(readCSV)
    #for row in readCSV:
        #your_list = list(row)
        #print(your_list)
    #print(line)
    if line:
        output = {
        'GPS_Time' : line[0],
        'Device_Time' : line[1],
        'Longitude' : line[2],
        'Latitude' : line[3],
        'GPS_Speed' : line[4],
        'Horizontal_Dilution_of_Precision' : line[5],
        'Altitude' : line[6],
        'Bearing' : line[7],
        'Gx' : line[8],
        'Gy' : line[9],
        'Gz' : line[10],
        'G_calibrated' : line[11],
        'Engine_Coolant_Temp' : line[12],
        'Engine_RPM' : line[13],
        'Intake_Air_Temp' : line[14],
        'Engine_Load' : line[15],
        'Mass_Air_Flow_Rate' : line[16],
        'Throttle_Pos': line[17]
        }
        pprint.pprint(output)
csvfile.close()

with open('ODB.txt', 'rb') as readFile:
    dataRead = readFile.readlines()
readFile.close()

with open('ODB.txt', 'wb') as writeFile:
    writeFile.writelines(dataRead[1:])
writeFile.close()

