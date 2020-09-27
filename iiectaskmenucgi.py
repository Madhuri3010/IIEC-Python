#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess

print()
print("Press 1 to open notepad")
print("Press 2 to open calculator")
print("Press 3 to open mspaint")
print()

print("Enter your choice of program: ", end='')
p = input()

if int(p) == 1:
	subprocess.getoutput("notepad")
elif int(p) == 2:
	subprocess.getoutput("calc")
elif int(p) == 3:
	subprocess.getoutput("mspaint")	
else:
	print("Choice is not supported")


