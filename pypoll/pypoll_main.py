# import libraries
import os
import csv

#create variables for calculations
vote_count = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

#repeat code once for each data file
for file_count in range(2):
	file_name = "election_data_" + str(file_count+1) + ".csv"
	
	#create path
	csvpath = os.path.join(file_name)

	#open file and create file handl
	with open(csvpath, newline = "") as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ",")
		next(csvreader, None)

		# finding total vote count; finding individual vote counts
		for row in csvreader:
			vote_count += 1
			if row[2] in candidates.keys():
				candidates[row[2]] += 1
			else:
				candidates[row[2]] = 1

	# percentages for each candidate
	for key, value in candidates.items():
		candidates_percent[key] = round((value/vote_count) * 100, 2)

	# finding the winner
	for key in candidates.keys():
		if candidates[key] > winner_count:
			winner = key
			winner_count = candidates[key]
			
	# printing to the terminal
	print(f"Election Result for {file_name}:")
	print("-------------------------------------")
	print("Total Votes: " + str(vote_count))
	print("-------------------------------------")
	for key, value in candidates.items():
		print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
	print("-------------------------------------")
	print("Winner: " + winner)
	print("-------------------------------------")
