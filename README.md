Unit 3 | Assignment - Py Me Up, Charlie


Background

Well... you've made it!

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete 2 of 4 Python Challenges. Which ones you choose are completely your choice. In fact, feel encouraged to complete them all if you can muster the time.

Each of these challenges encompasses a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!


Before You Begin


Create a new GitHub repo called python-challenge. Then, clone it to your computer.
Inside your local git repository, create a directory for 2 of the 4 Python Challenges. Use folder names corresponding to the 2 challenges that you have chosen to complete: PyBank, PyPoll, PyBoss, or PyParagraph.
Inside of each folder that you just created, add a new file called main.py. This will be the main script to run for each analysis.
Push the above changes to GitHub.



Option 1: PyBank



In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total amount of revenue gained over the entire period
The average change in revenue between months over the entire period
The greatest increase in revenue (date and amount) over the entire period
The greatest decrease in revenue (date and amount) over the entire period


As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


Option 2: PyPoll



In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
