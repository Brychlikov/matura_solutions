import sys

for fname in sys.argv[1:]:
    with open(fname, 'rb') as old, open("new_" + fname, 'w') as new:
        new.write(old.read().decode('utf-8', 'ignore'))
