# import libraries
import os
import csv


# setup the file location 
filepath = "C:\\Users\\anany\\Desktop\\python_files"
csv_filepath = os.path.join(filepath,"budget_data.csv")

# open the file
with open(csv_filepath,'r',newline="") as pybank:
    # read the contents of the file
    csvreader = csv.reader(pybank,delimiter=",")
    # skip the header
    header = next(csvreader)
    
    # Create empty lists
    # to store months
    m_list = []
    # to store profit/loss
    pl_list = []
    # to store the change between months
    df_list = []

    # Create dictionaries
    # To store Mapping between profit/loss and Months
    # profit/loss is the Key and months is the value
    dict_pl_m = {}
    # to store mapping between change and profit/loss
    # Change is the Key and profit/loss is the value
    dict_df_pl = {}

    # for each row in the file
    for row in csvreader:
        # add the first column (months) to the month list
        m_list.append(row[0])
        # add the second column (profit/loss) to the profit_loss list
        pl_list.append(int(row[1]))
        # add the first row to the dictionary
        # profit/loss is the Key and months is the value
        dict_pl_m[row[1]]= row[0] 

    # for each row in the profit/loss list
    for itr in range(len(pl_list)-1):
        # calculate the change and add to the change list
        df_list.append(pl_list[itr+1]-pl_list[itr])
        # also add the change and profit/loss to the dictionary
        # Change is the Key and profit/loss is the value
        dict_df_pl[pl_list[itr+1]-pl_list[itr]] = pl_list[itr+1]

    # This will find the greatest increase from the change list
    df_inc = max(df_list)
    # this will find the greatest decrease from the change list
    df_dec = min(df_list)
    # this will get us the average change between months
    df_mean = round(sum(df_list)/len(df_list),2)

    # find the profit/loss record that has the greatest increase
    pl_inc = dict_df_pl[df_inc]
    # find the profit/loss record that has the greatest decrease
    pl_dec = dict_df_pl[df_dec]
    
    # using the profit/loss value from above search the profit/loss-month dictionary and find the month corresponding to that
    m_inc = dict_pl_m[str(pl_inc)]
    m_dec = dict_pl_m[str(pl_dec)]
    
   
    
    # print the output
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: "  + str(len(m_list)))
    print("Total: " +"$"+str(sum(pl_list)))
    print("Average Change: " + "$"+str(df_mean))
    print("Greatest Increase in Profits: " + m_inc + " ($" + str(df_inc)+")")
    print("Greatest Decrease in Profits: " + m_dec + " ($" + str(df_dec)+")")
    
    #export to text file 
    text_file = open("output_pybank.txt", "w")
    lines = ["Financial Analysis\n",   
             "-------------------\n",
             "Total Months:"  + str(len(m_list)) + "\n"
             "Total:"  + "$" +str(sum(pl_list)) + "\n"
             "Average Change:"  + "$"+str(df_mean)+"\n"
             "Greatest Increase in Profits: " + m_inc + " ($" + str(df_inc)+")\n"
             "Greatest Decrease in Profits: " + m_dec + " ($" + str(df_dec)+")"]
    text_file.writelines(lines)
    text_file.close()


        

