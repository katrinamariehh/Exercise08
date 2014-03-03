from sys import argv

script, filename = argv

myfile = open(filename, "r+")

lines = []

for line in myfile:
    if ord(line[0]) == ord("O"):
        line = line.split(":")
        lines.append(line[1].strip())

for line in lines:
     myfile.write(line)
     myfile.write("\n")

myfile.close()