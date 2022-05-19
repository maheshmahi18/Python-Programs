import sys
program_name=sys.argv[0]
arguments=sys.argv[1:]
count=len(arguments)
print("Name of the program is:",program_name)
print("Number or command line arguments=",count)
print("Arguments are")
for x in arguments:
    print(x)
