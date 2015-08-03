import sys, string, os

#Run in command line with python assembler.py file_name.asm
#Assembly file can be in the current working directory or a directory below the current working directory.
#The program will output a file_name.hack in the same directory as the assembly file

def dest(input):
	dest = input[0]
	if dest == "D":
		return "010"
	elif dest == "M":
		return "001"
	elif dest == "MD":
		return "011"
	elif dest == "A":
		return "100"
	elif dest == "AM":
		return "101"
	elif dest == "AD":
		return "110"
	elif dest == "AMD":
		return "111"
	else:
		print "Non legal destination"
		return "DEST_ERROR"

def comp(input):
	comp = input[0]
	if comp == "M":
		return "1110000"
	elif comp == "!M":
		return "1110001"
	elif comp == "-M":
		return "1110011"
	elif comp == "M+1":
		return "1110111"
	elif comp == "M-1":
		return "1110010"
	elif comp == "D+M":
		return "1000010"
	elif comp == "D-M":
		return "1010011"
	elif comp == "M-D":
		return "1000111"
	elif comp == "D&M":
		return "1000000"
	elif comp == "D|M":
		return "1010101"
	elif comp == "0":
		return "0101010"
	elif comp == "1":
		return "0111111"
	elif comp == "-1":
		return "0111010"
	elif comp == "D":
		return "0001100"
	elif comp == "A":
		return "0110000"
	elif comp == "!D":
		return "0001101"
	elif comp == "!A":
		return "0110001"
	elif comp == "-D":
		return "0001111"
	elif comp == "-A":
		return "0110011"
	elif comp == "D+1":
		return "0011111"
	elif comp == "A+1":
		return "0110111"
	elif comp == "D-1":
		return "0001110"
	elif comp == "A-1":
		return "0110010"
	elif comp == "D+A":
		return "0000010"
	elif comp == "D-A":
		return "0010011"
	elif comp == "A-D":
		return "0000111"
	elif comp == "D&A":
		return "0000000"
	elif comp == "D|A":
		return "0010101"
	else:
		print "Non legal computation"
		return "COMP_ERROR"

def jump(jump):
	print jump
	if jump == "JGT":
		return "001"
	elif jump =="JEQ":
		return "010"
	elif jump == "JGE":
		return "011"
	elif jump == "JLT":
		return "100"
	elif jump == "JNE":
		return "101"
	elif jump =="JLE":
		return "110"
	elif jump =="JMP":
		return "111"
	else:
		print "Non-legal jump code"
		return "JMP_ERROR"

def main():
	file_name = sys.argv[1]
	for path, dirs, files in os.walk('.'):
		if file_name in files:
			os.chdir(path)
			break
	
	with open(file_name) as f:
		content = f.readlines()
	f.close()
	file_name = file_name.split(".")
	newFileName = str(file_name[0]) + ".hack"
	#print newFileName
	#strips comments and white space from the strings
	for i in range(len(content)):
		content[i] = content[i].replace(' ', '')
		content[i] = content[i].replace('\t', '')
		content[i] = content[i].replace('\n', '')
		content[i] = content[i].replace('\r', '')
		content[i] = content[i].split("//", 1)[0]
	#remove empty lines
	content = [x for x in content if not x==""]
	#print content

	#Dictionary with predefined labels that can have new symbols added to it
	labels = {
			"R0":"0", "R1":"1", "R2":"2", "R3":"3", "R4":"4", "R5":"5", "R6":"6", "R7":"7", "R8":"8",
			"R9":"9", "R10":"10", "R11":"11", "R12":"12", "R13":"13", "R14":"14", "R15":"15", "SP":"0",
			"LCL":"1", "ARG":"2", "THIS":"3", "THAT":"4", "SCREEN":"16384", "KBD":"24576"
	}

	i=0
	
	#Pass 1 adds new labels of the form (XXXX) to the labels dict and removes them from the assembly
	while i < len(content):
		line = content[i]
		if '(' in line:
			index = content.index(line)
			line = line.replace(')', '')
			line = line.replace('(', '')
			labels[line] = str(index)
			content.pop(i)
			i-=1
		i += 1


	next_free_address = 16

	f = open(newFileName, 'w')
	
	#Pass 2 generates code and handles variable symbols
	for line in content:
		if "@" in line: #A-COMMAND
			line = line.replace("@", "")
			if not line[0].isdigit(): 
				if line not in labels:
					labels[line] = str(next_free_address)
					next_free_address += 1
			if line[0].isdigit():
				instruction = '{0:016b}'.format(int(line))
			elif labels.get(line) != None:
				instruction = '{0:016b}'.format(int(labels[line]))
		else: #C_COMMAND
			instruction = "111"
			line = line.split("=")
			if len(line) == 1:
				line = line[0].split(";")
				dest_binary = "000"
				comp_binary = comp(line[0])
				jump_binary = jump(line[1])
				instruction = instruction+comp_binary+dest_binary+jump_binary
			else:
				for i in range(2):
					line[i] = line[i].split(";")
				dest_binary = dest(line[0])
				comp_binary = comp(line[1])
				if len(line) == 2:
					jump_binary = "000"
				elif len(line) == 3:
					jump_binary = jump(line[2])
				instruction = instruction+comp_binary+dest_binary+jump_binary
		f.write(instruction+"\n")
	f.close()


main()

