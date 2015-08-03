import string, sys, os

def newFileName(file_name):
	return file_name.replace(".vm", "") + ".asm"

def main():
	file_name = sys.argv[1]
	if file_name.endswith(".vm"): #Dealing with a single .vm file
		new_file_name = newFileName(file_name)
		for path, dirs, files in os.walk('.'):
			if file_name in files:
				os.chdir(path)
				with open(file_name) as f:
					content = f.readlines()
				f.close()
				print content
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
					print content
					#assembly = translate(content)
					new_file_name = newFileName(f)
					#f = open(new_file_name, "a")
					#for line in assembly:
					#	f.write(line)
					#f.close()


main()