import sys

fn = sys.argv[1]

f = open(fn)

for row in f.readlines():
    for sep in ".,?:;":
        row = row.replace(sep, " %s " % sep)
    row = row.strip().lower()
    if not row:
        continue
    row = row.split()
    for dis in ('the', 'a'):
        while dis in row:
            row.remove(dis)
    print (row)
