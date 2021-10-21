import csv 
import statistics

with open("HeightWeight.csv" , newline = '') as f:
     reader = csv.reader(f)
     file_data = list(reader)
file_data.pop(0)   
# print(file_data) 

newData = []
for i in range( len(file_data) ):
    num = file_data[i][2]
    newData.append(float(num))
print(newData)

n = len(newData)
sum = 0
for i in newData:
     #sum = sum + i
    sum += i

mean = sum/n 

print(f"THIS IS THE MEAN: {mean}")


print(f"statistics.mean(newData: {mean} )" )

print(statistics.median(newData))