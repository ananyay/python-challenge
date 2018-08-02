#importing libraries
import os 
import csv 
# filepath
filepath = "C:\\Users\\anany\\Desktop\\python_files"
csv_filepath = os.path.join(filepath,"election_data.csv")
with open(csv_filepath,newline="",encoding='utf-8') as pypoll:
    csvreader = csv.reader(pypoll,delimiter=",")
    header = next(csvreader)
    t_votes = []
    d = {}

    for row in csvreader:
        t_votes.append(row[0])
        k = row[2]
        v = row[0]
        if k in d:
            d[k] = d[k]+1
        else:
            d[k] = 1
print ("Total Votes:" + str(len(t_votes))) 
print (d)

for key in d:
    print(key,':',(d[key]/len(t_votes)),(d[key]))
        