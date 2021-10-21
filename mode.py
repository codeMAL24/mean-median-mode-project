import csv 
from collections import Counter

with open("HeightWeight.csv" , newline = '') as f:
     reader = csv.reader(f)
     file_data = list(reader)
file_data.pop(0)   
# print(file_data) 

newData = []
for i in range( len(file_data) ):
    num = file_data[i][2]
    newData.append(float(num))
# print(newData)

data = Counter(newData)
modeDataRange = {
    "110-120" : 0,
    "120-130" : 0,
    "130-140" : 0,
    "140-150" : 0,
    "150-160" : 0
}
for height, occurence in data.items():
     if 110 < float(height) < 120:
          modeDataRange["110-120"] += occurence 

     elif 120 < float(height) < 130:
          modeDataRange["120-130"] += occurence   

     if 130 < float(height) < 140:
          modeDataRange["130-140"] += occurence  

     if 140 < float(height) < 150:
          modeDataRange["140-150"] += occurence  

     if 150 < float(height) < 160:
          modeDataRange["150-160"] += occurence               


modeRange, modeOccurence = 0,0
for range,occurence in modeDataRange.items():
    if occurence > modeOccurence:
        modeRange , modeOccurence = [int(range.split("-")[0] ),int(range.split("-")[1] )] ,occurence
# print(modeDataRange)
# print(modeRange)

mode = float(modeRange[0] + modeRange[1]/2)


# {} placeholder in this scenario
print("initializing....")

print(f" The mode of the data is: {mode} ")



    