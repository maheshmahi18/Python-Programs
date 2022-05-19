import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
s=0
count=len(arguments)
for i in arguments:
    s=s+int(i)
avg=s/count
print("Name of the program is:",program_name)
print("Number or command line arguments=",count)
print("Average value of arguments are",avg)

