import sys
from lib.parser_ import parse
from lib.runner import run

fin = sys.argv[1]

with open(fin) as f:
    source = f.read()

run(parse(source))
