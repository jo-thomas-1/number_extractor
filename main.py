import sys

data_file = open(sys.argv[1], "r", encoding="utf-8")
content = data_file.read()
data_file.close()

contacts = []
count = 0
temp = ""

print("File length: ", len(content))

for character in content:
	count += 1
	print(count, " characters scanned", end="\r")

	if(character.isdigit() or character == '+' or character == ' '):
		temp += character
	elif(temp.strip() != "" and len(temp.strip()) >= 5):
		contacts.append(temp.strip())
		temp = ""

print("\n\n", "Concats found: ", len(contacts))

count = 0

data_file = open("data.out", "w")
for contact in contacts:
	count += 1
	print("contact saved: ", count, end="\r")
	data_file.write(contact)
	data_file.write("\n")
data_file.close()