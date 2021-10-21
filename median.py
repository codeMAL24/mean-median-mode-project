import csv 
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

n = len(newData)
newData.sort()
#modulo - it finds the remainder
if n % 2 == 0:
    # floor division is shown by //
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1 + m2/2)     
else:
    median = newData[n//2]
print(f"median: {median}")    