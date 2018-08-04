#importing libraries
import os 
import csv 
import pathlib

# setup the file location
filepath = pathlib.Path(__file__).parent

csv_filepath = os.path.join(filepath,"resources","election_data.csv")
# opening the file 
with open(csv_filepath,newline="",encoding='utf-8') as pypoll:
    # read the contents of the file 
    csvreader = csv.reader(pypoll,delimiter=",")
    # skip the header 
    header = next(csvreader)
    # create an empty lists to store voter id's
    total_votes = []
    # create a dictionary with key as candidates , values as voter id 
    dict_cand_vot = {}
    # for every row in the file 
    for row in csvreader:
        total_votes.append(row[0])
        key = row[2]
        value = row[0]
        if key in dict_cand_vot:
            dict_cand_vot[key] = dict_cand_vot[key]+1
        else:
            dict_cand_vot[key] = 1

# print the output
print("Election Results")
print("------------------------------")

print ("Total Votes: " + str(len(total_votes))) 
print("-------------------------------")
# for each key in the dictionary
for k in dict_cand_vot:
    votes_pct = round((dict_cand_vot[k]/len(total_votes)*100.0),3)
    cand_votes = str(dict_cand_vot[k])
    #print(k + ": " + str(votes_pct) + "00% (" + str(cand_votes) + ")")
    print(f'{k} : {votes_pct:.3f}% ({cand_votes})')
print("-------------------------------")    
print("winner is : "+ max(dict_cand_vot,key=dict_cand_vot.get))
print("-------------------------------")

# writing into txt file 
output_path = os.path.join(filepath,"output_pypoll.txt")
text_file = open(output_path,"w")
# for writing multiple lines to txt file 
lines = ["Election Results\n"
         "------------------------------\n",
         "Total Votes: " + str(len(total_votes)) + "\n",
         "-------------------------------\n"]
text_file.writelines(lines)
# for each key in the dictionary
for k in dict_cand_vot:
    votes_pct = round((dict_cand_vot[k]/len(total_votes)*100.0),3)
    cand_votes = dict_cand_vot[k]
    lines = [ f'{k} : {votes_pct:.3f}% ({cand_votes})\n']
    text_file.writelines(lines)
#
lines = ["-------------------------------\n",
        "winner is : "+ max(dict_cand_vot,key=dict_cand_vot.get)+ "\n",
        "---------------------------------\n"]
text_file.writelines(lines)
text_file.close()
       

