import os
import csv
pypoll = os.path.join(".","Resources","election_data.csv")
with open (pypoll, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    data = list(csvreader)
    row_count = len(data)


    candidatelist = list()
    sum = list()
    for x in range (0,row_count):
        candidate = data[x][2]
        sum.append(candidate)
        if candidate not in candidatelist:
            candidatelist.append(candidate)
           
    candicount = len(candidatelist)
    votes = list()
    percentage = list()
    for y in range (0,candicount):
        name = candidatelist[y]
        votes.append(sum.count(name))
        vprct = votes[y]/row_count
        percentage.append(vprct)
winner = votes.index(max(votes))

os.mkdir("Analysis")
result = os.path.join ("Analysis","result_PyPoll.txt")
with open (result, "w") as f:
    f.write("Election Results \n")
    f.write("------------------------------------\n")
    f.write("Total Votes: " + str(row_count) + "\n")
    f.write("------------------------------------\n")
    
print("Election Results")
print("----------------------------")
print(f"Total Votes: {row_count:,}")
print("----------------------------")

for z in range (0,candicount):
  print(f"{candidatelist[z]}: {percentage[z]:.3%} ({votes[z]:,})")


  f.write("Winner" + str(candidatelist(winner))+"\n" )
  f.write("------------------------------------\n")
print("----------------------------")
print(f"Winner: {candidatelist[winner]}")
print("----------------------------")