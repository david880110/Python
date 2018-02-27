#import OS and CSV libraries
import os
import csv
from datetime import datetime

#repeat code once for each data file
for file_count in range(2):
	file_name = "employee_data" + str(file_count+1) + ".csv"
	
	#create path
	csvpath = os.path.join(file_name)

	# Lists to store data: 
	EmpID = []
	FirstName = []
	LastName = []
	DOB = []
	SSN = []
	State = []

	# Copying us_states abbv data
	us_state_abbrev = {
		'Alabama': 'AL',
		'Alaska': 'AK',
		'Arizona': 'AZ',
		'Arkansas': 'AR',
		'California': 'CA',
		'Colorado': 'CO',
		'Connecticut': 'CT',
		'Delaware': 'DE',
		'Florida': 'FL',
		'Georgia': 'GA',
		'Hawaii': 'HI',
		'Idaho': 'ID',
		'Illinois': 'IL',
		'Indiana': 'IN',
		'Iowa': 'IA',
		'Kansas': 'KS',
		'Kentucky': 'KY',
		'Louisiana': 'LA',
		'Maine': 'ME',
		'Maryland': 'MD',
		'Massachusetts': 'MA',
		'Michigan': 'MI',
		'Minnesota': 'MN',
		'Mississippi': 'MS',
		'Missouri': 'MO',
		'Montana': 'MT',
		'Nebraska': 'NE',
		'Nevada': 'NV',
		'New Hampshire': 'NH',
		'New Jersey': 'NJ',
		'New Mexico': 'NM',
		'New York': 'NY',
		'North Carolina': 'NC',
		'North Dakota': 'ND',
		'Ohio': 'OH',
		'Oklahoma': 'OK',
		'Oregon': 'OR',
		'Pennsylvania': 'PA',
		'Rhode Island': 'RI',
		'South Carolina': 'SC',
		'South Dakota': 'SD',
		'Tennessee': 'TN',
		'Texas': 'TX',
		'Utah': 'UT',
		'Vermont': 'VT',
		'Virginia': 'VA',
		'Washington': 'WA',
		'West Virginia': 'WV',
		'Wisconsin': 'WI',
		'Wyoming': 'WY',
	}

	#open file and create file handl
	with open(csvpath, newline="") as csvfile:
		csvreader= csv.reader(csvfile, delimiter=",")    

		#skip header row
		next(csvfile)

		for row in csvreader:
			
			# Adding EmpID
			EmpID.append(row[0])
			

			# Splitting full name into first and last
			fullName = row[1].split(" ")
			FirstName.append(fullName[0])
			LastName.append(fullName[1])

			# Converting DOB from YYYY-MM-DD to MM/DD/YYYY
			csvDOB = datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")
			DOB.append(csvDOB)

			# Convert SSN by grabbing the last 4 adding prefix ***-**-
			csvSSN = row[3]
			csvSSN = csvSSN[-4:]
			SSN.append("***-**-" + csvSSN)

			# Convert from full state name to abbv via state dictionary  
			csvState = row[4]
			State.append(us_state_abbrev[csvState])
	   

	# Zip lists together
	cleaned_csv = zip(EmpID, FirstName, LastName, DOB, SSN, State)
	print(cleaned_csv)

	# Set variable for output file
	output_file = os.path.join("pybossOutput.csv")

	#  Open the output file
	with open(output_file, "w", newline="") as datafile:
		writer = csv.writer(datafile)

		# Write the header row
		writer.writerow(["EmpID", "FirstName", "LastName", "DOB", "SSN", "State"])

		# Write in zipped rows
		writer.writerows(cleaned_csv)