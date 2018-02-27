# import OS libraries
import os

# declaring & initializing variables
letter_count = 0

#repeat code once for each data file
for file_count in range(2):
		file_name = "paragraph_" + str(file_count+1) + ".txt"

		# opening file
		with open(file_name, 'r') as txtfile:
			# reading file
			paragraph = txtfile.read()

			# finding word count
			word_count = paragraph.count(" ") + 1 # +1 to account for the last word

			# finding sentence count
			sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

			# finding average letter count
			for character in paragraph:
				if character.isalpha():
					letter_count += 1 # counting how many characters are letters
			avg_letter_count = letter_count/word_count # finding average letter count

			# finding average sentence length
			avg_sentence = word_count/sentence_count

		# printing results to terminal
		print(f"Paragraph Analysis for {file_name}:")
		print("----------------------------------")
		print("Approximate Word Count:", word_count)
		print("Approximate Sentence Count:", sentence_count)
		print("Average Letter Count:", avg_letter_count)
		print("Average Sentence Length:", avg_sentence)