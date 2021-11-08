#This program will check for a DNA match:
import sys
import csv

if len(sys.argv) != 3:
    print("Please enter correctly the command line argument: program/data/sequence")

#Reading persons DNA:
csv_list = []
with open(sys.argv[1], "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        csv_list.append(i)
#Reading sequence of DNA:
sequence_list = ""
with open(sys.argv[2], "r") as txt_file:
    list_reader = txt_file.read()
    for i in list_reader:
        sequence_list += i

#Converting STRS into a list:
strs_list = []
for i in csv_list[1].keys():
    strs_list.append(i)


def_counter = []

#Cheking for STRS in the sequence:
for i in range(len(strs_list)-1):
    count = 0
    counter = []
    strs_lenght = len(strs_list[i+1])
    for j in range(len(sequence_list)):
        if strs_list[i+1] == sequence_list[j:j+strs_lenght]:
            count = 1
            counter.append(count)
            while sequence_list[j:j+strs_lenght] == sequence_list[j+strs_lenght:j+strs_lenght*2]:
                count += 1
                j += strs_lenght
                counter.append(count)
    if count == 0:
        def_counter.append(count)
    else:
        counter.sort()
        def_counter.append(counter[-1])
         
       
#Putting the STRS persons into a list:
data_list = []
for i in range(len(csv_list)):
    variable_list = []
    for j in range(len(strs_list)-1):
        variable_list.append(csv_list[i][strs_list[j+1]])
    data_list.append(variable_list)

final = [str(x) for x in def_counter]

#Comparing STRS of sequence and STRS of persons:
for i in range(len(csv_list)):
    if data_list[i] == final:
        print(csv_list[i]["name"])
        sys.exit(0)

print("No match")





