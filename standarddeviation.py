import csv
import math
with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

#finding mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

#squaring and getting the values
square_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    square_list.append(a)

#getting sum
sum = 0
for i in square_list:
    sum = sum+i

#diving sum by total number of values
result = sum/(len(data)-1)

#getting deviation by taking the square root
standard_deviation = math.sqrt(result)
print(standard_deviation)
