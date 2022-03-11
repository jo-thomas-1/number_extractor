import sys

# get input data file
try:
	data_file = open(sys.argv[1], "r", encoding="utf-8")
except Exception as e:
	data_file = open("data.in", "r", encoding="utf-8")

content = data_file.read()

data_file.close()

# --------------------------------------------------------------------

contacts = []
count = 0
temp = ""

print("File length: ", len(content))

for character in content:
	count += 1
	print(count, " characters scanned", end="\r")

	if(character.isdigit() or character == '+' or character == ' '):
		temp += character
	elif(temp.strip() != ""):
		contacts.append(temp.strip())
		temp = ""

print("\n\n\b", len(contacts), " concats found")

# --------------------------------------------------------------------

count = 0

# set output data file
try:
	data_file = open(sys.argv[2], "w")
except Exception as e:
	data_file = open("data.out", "w")

for contact in contacts:
	if(len(contact) >= 10):
		count += 1
		print(count, " contacts saved", end="\r")
		data_file.write(contact)
		data_file.write("\n")

data_file.close()