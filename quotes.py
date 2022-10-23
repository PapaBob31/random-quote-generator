import sys, random

help_text = ("This program prints out a random quote everytime it is run.\n" +
			"You can add a quote with the '-add' parameter\n" +
			"e.g quotes -add \"The sun in the Sky doesn't stop me from flying.\"\n" +
			"Added quotes must be inside double quotes or an error will be raised.")


def get_valid_line(quotes_list):
	"""Gets a non-empty line of text from the quotes_list parameter"""
	if quotes_list:
		quote = random.choice(quotes_list).rstrip("\n").rstrip()
		if quote:
			print(quote)
			return
		try:
			get_valid_line(quotes_list)
		except RecursionError:
			sys.exit("Error: Couldn't get a valid quote!")
	else:
		sys.exit("No quote was found. Please add a quote through the -add parameter")

def add_new_quote(new_quote):
	try:
		with open('quotes.txt', 'r+') as quotes_file:
			all_quotes = quotes_file.read()
			quotes_file.seek(0, 2)
			if all_quotes[-1] != "\n": # Checks if there's no new line at the end of the file.
				quotes_file.write("\n" + new_quote)
			else:
				quotes_file.write(new_quote)
	except FileNotFoundError:
		with open('quotes.txt', 'w') as quotes_file:
			quotes_file.write(sys.argv[2])
	finally:
		print("New quote was added succesfully.")


if len(sys.argv) == 1: # The command to get a random quote
	try:
		with open('quotes.txt', 'r') as quotes_file:
			get_valid_line(quotes_file.readlines())
	except FileNotFoundError:
		print("No quote was found. Please add a quote through the -add parameter")

elif len(sys.argv) == 2: # The command can only be to get help about the program or invalid
	if sys.argv[1] == "/?":
		print(help_text)
	else:
		print("invalid parameter! Use the '/?' parameter for more info on the built in parameters.")

elif len(sys.argv) == 3: # The command can only be to add a quote or invalid
	if sys.argv[1] == "-add":
		new_quote = sys.argv[2].strip()
	if new_quote:
		add_new_quote(new_quote)
	else:
		print("Invalid input! Quote must contain non white space characters.")

else:
	print("invalid parameters! Use the '/?' parameter for more info on the built in parameters.")