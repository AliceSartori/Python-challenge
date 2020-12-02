#Dependeces
import os
import csv


## Open and read csv
path = os.path.join('.', 'Resources', 'election_data.csv')
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(reader)
    print(csv_header)

    #Set the conter for total votes as 0
    total_votes_count = 0
    maxvalue = 0
    #Create an empty dictionary that will pull the name of the candidate as key and have the total
    #for each candidate as value
    # candidates={name:count_vote}
    candidates = {}
    #loop through all rows
    for row in reader:
        #get the total number of votes
        name_candidate = row[2]
        total_votes_count += 1
        #if the name of the candidate is already present as key, it adds up to itself every time it gets through the for loop
        #otherwise create the occurrence
        if(name_candidate in candidates.keys()):
            candidates[name_candidate] += 1
        else:
            candidates[name_candidate] = 1


    #creating a .txt file
    fp_write = open('PyPoll_Analysis.txt', 'w')
    print('text')
    fp_write.write('text\n')
    print('Election Results')
    fp_write.write(f'Election Results\n')
    print(f'------------------------------')
    fp_write.write('------------------------------\n')
    print(f"Total Votes: {total_votes_count}")
    fp_write.write(f"Total Votes: {total_votes_count}\n")
    print(f'------------------------------')
    fp_write.write('------------------------------\n')

#create a foor loop that gets the percentage of single candidate
    for name_candidate in candidates:
        #print(candidates[name_candidate]) #values and tot votes per candidate
        #print(name_candidate) # keys
        percentage_votes = (candidates[name_candidate]/total_votes_count) * 100
        print(f'{name_candidate}: {percentage_votes:.3f}% ({candidates[name_candidate]})')
        fp_write.write(f'{name_candidate}: {percentage_votes:.3f}% ({candidates[name_candidate]})\n')
    #create an if-statement to pull the name of the candidate who got the greatest amount
    #of votes
        if candidates[name_candidate] > maxvalue:
            maxvalue = candidates[name_candidate]
            tmp_winner = name_candidate

    print("------------------------------")
    fp_write.write('------------------------------\n')
    print(f'Winner: {tmp_winner}')
    fp_write.write(f'Winner: {tmp_winner}\n')
    print("------------------------------")
    fp_write.write('------------------------------\n')

#output file
# fp_write = open('PyPoll_Analysis.txt', 'w')
#     print('text')
#     fp_write.write('text\n')
#     print('Election Results')
#     fp_write.write(f'Election Results\n')
#     print(f'------------------------------')
#     fp_write.write('------------------------------\n')
#     print(f"Total Votes: {total_votes_count}")
#     fp_write.write(f"Total Votes: {total_votes_count}")
#     print()
