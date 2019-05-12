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
        "GPS_Time" : line[0],
        "Device_Time" : line[1],
        "Longitude" : float(line[2]),
        "Latitude" : float(line[3]),
        "GPS_Speed" : float(line[4]),
        "Horizontal_Dilution_of_Precision" : float(line[5]),
        "Altitude" : int(line[6]),
        "Bearing" : float(line[7]),
        "Gx" : float(line[8]),
        "Gy" : float(line[9]),
        "Gz" : float(line[10]),
        "G_calibrated" : float(line[11]),
        "Engine_Coolant_Temp" : int(line[12]),
        "Engine_RPM" : float(line[13]),
        "Intake_Air_Temp" : int(line[14]),
        "Engine_Load" : float(line[15]),
        "Mass_Air_Flow_Rate" : float(line[16]),
        "Throttle_Pos": float(line[17])
        }
        pprint.pprint(output)
csvfile.close()

with open('ODB.txt', 'rb') as readFile:
    dataRead = readFile.readlines()
readFile.close()

with open('ODB.txt', 'wb') as writeFile:
    writeFile.writelines(dataRead[1:])
writeFile.close()

