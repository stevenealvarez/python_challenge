
import csv

#as mentioned in class using a dicitonary for this challenge

csvpath=os.path.join('/Users/stevene/Desktop/python_challenge/PyPoll/election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    #Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #total number of votes cast use len to keep count of all the votes
    total_votes = (len(votes))
    print(total_votes)

    #list of candidates who received votes
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            voted_khan = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            voted_correy = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            voted_li = len(li)
        else:
            otooley.append(candidates)
            voted_otooley = len(otooley)

    print(voted_khan)
    print(voted_correy)
    print(voted_li)
    print(voted_otooley)

    #Percentage of votes for each candidate won
    khan_perc = round(((voted_khan / total_votes) * 100), 2)
    correy_perc = round(((voted_correy / total_votes) * 100), 2)
    li_perc = round(((voted_li / total_votes) * 100), 2)
    otooley_perc = round(((voted_otooley / total_votes) * 100), 2)
    print(khan_perc)
    print(correy_perc)
    print(li_perc)
    print(otooley_perc)


    #winner of election based on popular vote

    if khan_percent > max(correy_perc, li_perc, otooley_perc):
        winner = "Khan"
    elif correy_percent > max(khan_perc, li_perc, otooley_perc):
        winner = "Correy"  
    elif li_percent > max(correy_perc, khan_perc, otooley_perc):
        winner = "Li"
    else:
        winner = "O'Tooley"
        #Print Statements


print(f"Election Results") 
print(f"-----------------------------------") 
print(f"Total Votes: {total_votes}" 
print(f"-----------------------------------")
print(f"Khan: {khan_perc}% ({voted_khan})") 
print(f"Correy: {correy_perc}% ({voted_correy})") 
print(f"Li: {li_perc}% ({voted_li)") 
print(f"O'Tooley: {otooley_perc}% ({voted_otooley})") 
print(f"-----------------------------------") 
print(f"Winner: {winner}") 
print(f"-----------------------------------")


