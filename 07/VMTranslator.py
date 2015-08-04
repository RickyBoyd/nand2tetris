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
	#push whatever is in D
	push_asm = "@SP\nM=M+1\nA=M\nM=D\n"

def constant(i):
	number = str(i)
	constant_asm = "@"+number+"\nD=A\n"

def add_routine():
	add_asm = "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D\n"
	return

def newFileName(file_name):
	return file_name.replace(".vm", "") + ".asm"

def initialise():
	initialise_asm = "@SP\nM=256"

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
				print parse(content)
				#print content
				#TO BE IMPLEMENTED
				#assembly = translate(content)
				#f = open(new_file_name, "w")
				#for line in assembly:
				#	f.write(line)
				#f.close()
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