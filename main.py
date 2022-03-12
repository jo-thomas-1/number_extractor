import sys
import csv

# get input data file
try:
	data_file = open(sys.argv[1], "r", encoding="utf-8")
except Exception as e:
	data_file = open("data.in", "r", encoding="utf-8")

input_data = data_file.read()

data_file.close()

# --------------------------------------------------------------------


data = []
temp = ""
data_length = len(input_data)

print("Data length: ", data_length)

for i in range(len(input_data)):
	print("Scannig data -", int(((i + 1)/data_length) * 100), '% (' + str(i + 1) + ' out of ' + str(data_length) + ')',  end="\r")

	if(input_data[i].isdigit() or input_data[i] == '+' or input_data[i] == ' '):
		temp += input_data[i]
	elif(temp.strip() != ""):
		temp = temp.strip()
		if(len(temp) >= 10 and temp[0] == '+' and temp not in data):
			data.append(temp)
		temp = ""

print("\n\n", len(data), "contacts retrieved")

# --------------------------------------------------------------------

# set output data file

if(input("Do you wish to create a CSV file [Y/N]: ").lower() == 'y'):
	data_file = open("data.csv", "w")

	data_length = len(data)

	for i in range(len(data)):
		print("saving contacts to CSV file -", int(((i + 1)/data_length) * 100), '% (' + str(i + 1) + ' out of ' + str(data[i]) + ')',  end="\r")
		data_file.write(data[i])
		data_file.write("\n")

	data_file.close()

else:
	try:
		data_file = open(sys.argv[2], "w")
	except Exception as e:
		data_file = open("data.out", "w")

	data_length = len(data)

	for i in range(len(data)):
		print("saving contacts -", int(((i + 1)/data_length) * 100), '% (' + str(i + 1) + ' out of ' + str(data[i]) + ')',  end="\r")
		data_file.write(data[i])
		data_file.write("\n")

	data_file.close()