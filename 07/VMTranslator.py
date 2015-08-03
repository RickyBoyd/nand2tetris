import string, system, os

def main():
	file_name = sys.argv[1]
	if file_name.endswith(".vm"):
		new_file_name = file_name.remove(".vm", "") + ".asm"
		print new_file_name
		for path, dirs, files in os.walk('.'):
		if file_name in files:
			os.chdir(path)
			with open(file_name) as f:
				content = f.readlines()
			f.close()
			#assembly = translate(content)
			break
	
