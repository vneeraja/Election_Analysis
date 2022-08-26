# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# import datetime class from the datetime module with Alias dt
import datetime as dt
# import csv module to pull data from external csv files
import csv
# import os module to pull a file indirectly from an unknown path 
import os

# Assisgn a variable for the file to load and the path
#file_to_load = "Resources/election_results.csv"

# Assign a variable to load a file from unknown path
file_os_load =  os.path.join("Resources","election_results.csv")

# Assign a filename variable to save the file to the path
file_os_write = os.path.join("Analysis","election_analysis.txt")

# open the election results file and the read the data
with open(file_os_load) as election_data:   
    
    # Read and do the data analysis
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # print each row in the csv
    for row in file_reader:
            print(row)

# open the election results to write
with open(file_os_write,"w") as txt_file:

    # write to file
    # write the title
    txt_file.write("Counties in the Election\n")
    # underline the title
    txt_file.write("-------------------------\n")
    # write the three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
    
    # close the file
    txt_file.close()


