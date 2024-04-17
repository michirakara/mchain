import re
import sys
import parser_

fin = sys.argv[1]
fout = "out.cpp"
if len(sys.argv) >= 3:
    fout = sys.argv[2]

with open(fin) as f:
    source = f.read()
source = re.sub(r"[\n\t]", "", re.sub(r"(?m)\/\/.*?$", "", source))

lines = source.split(";")

if lines[-1] == "":
    lines.pop()


for line in lines:
    parser_.parse_line(line)
