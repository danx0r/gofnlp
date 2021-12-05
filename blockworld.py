import sys

bugg = 0
def parse(toks, i=0, end=(".",)):
    global bugg
    bugg += 1
    print ("   recursion level:", bugg, "i:", i, "toks:", toks, "end:", end)
    out = []
    ender = None
    while i < len(toks):
        tok = toks[i]
        if tok in end:
            ender = tok
            break
        if tok == "put":
            nu, i, ender = parse(toks, i + 1, ('in', 'on'))
            out += nu
            out.append(f"put-{ender}")
        else:
            out.append(tok)
        print ("==========>", tok, out)
        i += 1
    bugg -= 1
    print ("   returns:", out, i, ender)
    return out, i, ender


if __name__ == "__main__":
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
        print ("---------------------------------------")
        print (row)
        out = parse(row)
        print (out)
        break