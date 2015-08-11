import string, sys, os

def parse(content):
	for i in range(len(content)):
		content[i] = content[i].replace('\t', '')
		content[i] = content[i].replace('\n', '')
		content[i] = content[i].replace('\r', '')
		content[i] = content[i].split("//", 1)[0]

	#remove empty lines
	content = [x for x in content if not x==""]
	for i in range(len(content)):
		content[i] = content[i].split(" ")
	return content

def pop(args):
	#pop whatever is at the top of the stack to D
	pop_asm = "@SP\nM=M-1\nA=M\nD=M\n"

def push(args):
	push_asm = ""
	if args[0] == "constant":
		push_asm = push_asm + constant(args[1])

	#push whatever is in D
	push_asm = push_asm + "@SP\nM=M+1\nA=M-1\nM=D\n"
	return push_asm

def constant(i):
	number = str(i)
	constant_asm = "@"+number+"\nD=A\n"
	return constant_asm

def add_routine():
	return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M+D\n"

def sub_routine():
	return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n"

def neg_routine():
	return "@SP\nA=M-1\nM=-M\n"

def not_routine():
	return "@SP\nA=M-1\nM=!M\n"

def and_routine():
	return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M&D\n"

def or_routine():
	return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M|D\n"

### IDEA
### Make it so that the eq lt and gt routines are written only once and can be reused
###
def eq_routine(call_number):
	number = str(call_number)
	return "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@EQUALS"+number+"\nD;JEQ\n@SP\nA=M-1\nM=0\n@END"+number+"\n0;JMP\n(EQUALS"+number+")\n@SP\nA=M-1\nM=-1\n(END"+number+")\n"

def lt_routine(call_number):
	number = str(call_number)
	assembly = "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@LT"+number+"\nD;JLT\n@SP\nA=M-1\nM=0\n@END"+number+"\n0;JMP\n(LT"+number+")\n@SP\nA=M-1\nM=-1\n(END"+number+")\n"
	return assembly
def gt_routine(call_number):
	number = str(call_number)
	assembly = "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GT"+number+"\nD;JGT\n@SP\nA=M-1\nM=0\n@END"+number+"\n0;JMP\n(GT"+number+")\n@SP\nA=M-1\nM=-1\n(END"+number+")\n"
	return assembly

def stack_arithemtic(operation, call_number):
	if operation == "add":
		return add_routine()
	elif operation == "sub":
		return sub_routine()
	elif operation == "neg":
		return neg_routine()
	elif operation == "not":
		return not_routine()
	elif operation == "and":
		return and_routine()
	elif operation == "or":
		return or_routine()
	elif operation == "eq":
		return eq_routine(call_number)
	elif operation == "lt":
		return lt_routine(call_number)
	elif operation == "gt":
		return gt_routine(call_number)
	else:
		print '"'+line[0]+'"' + " is not a known operation."

def initialise():
	initialise_asm = "@SP\nM=256"

def generateAssembly(parsed_vm_code):
	assembly = ""
	call_number = "0" #needed so that each label for every comparison operation is unique
	for line in parsed_vm_code:
		if len(line) == 3 and line[0] == "push":
			assembly = assembly + push(line[1:3])
		if len(line) == 1:
			assembly = assembly + stack_arithemtic(line[0], call_number)
			call_number = str(int(call_number)+1)
	return assembly

def translate(content):
	return generateAssembly(parse(content))

def newFileName(file_name):
	return file_name.replace(".vm", "") + ".asm"

def main():
	file_name = sys.argv[1]
	add_routine()
	if file_name.endswith(".vm"): #Dealing with a single .vm file
		new_file_name = newFileName(file_name)
		for path, dirs, files in os.walk('.'):
			if file_name in files:
				os.chdir(path)
				with open(file_name) as f:
					content = f.readlines()
				f.close()
				print translate(content)
				assembly = translate(content)
				f = open(new_file_name, "w")
				for line in assembly:
					f.write(line)
				f.close()
				break
	elif not '.' in file_name: #Dealing with a directory
		for path, dirs, files in os.walk("./"+file_name):
			for f in files:
				if f.endswith(".vm"):
					os.chdir(path)
					content = []
					with open(f) as file_content:
						content = file_content.readlines()

					file_content.close
					#print content
					#assembly = translate(content)
					new_file_name = newFileName(f)
					#f = open(new_file_name, "a")
					#for line in assembly:
					#	f.write(line)
					#f.close()


main()