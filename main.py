import sys

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
input_data_length = len(input_data)

print("Data length: ", input_data_length)

for i in range(len(input_data)):
	print("scannig data -", int(((i + 1)/input_data_length) * 100), '%',  end="\r")

	if(input_data[i].isdigit() or input_data[i] == '+' or input_data[i] == ' '):
		temp += input_data[i]
	elif(temp.strip() != ""):
		data.append(temp.strip())
		temp = ""

print("\n\n", len(data), "values found")

# --------------------------------------------------------------------

# clean data
output_data = []
count = 0

for i in range(len(data)):
	if(len(data[i]) >= 10 and data[i][0] == '+' and data[i] not in output_data):
		output_data.append(data[i])
		count += 1
		print(count, "contacts retrieved", end="\r")

# --------------------------------------------------------------------

# set output data file
try:
	data_file = open(sys.argv[2], "w")
except Exception as e:
	data_file = open("data.out", "w")

for i in range(len(output_data)):
	print("saving contacts...", end="\r")
	data_file.write(output_data[i])
	data_file.write("\n")

data_file.close()