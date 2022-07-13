import sys

STACK = []
TOKENS = []
INDEX = 0

TABLE = []
BASKET = ["block1_red", "block2_blue"]

def process_token():
    global INDEX
    token = TOKENS[INDEX]
    INDEX += 1
    funcname = f"_{token}"
    if funcname in globals():
        print ("CALL", funcname)
        return globals()[funcname]()
    else:
        print ("PRIM    :", token)
        return token

def tokenize_sentence(s):
    for sep in ".,?:;":
        s = s.replace(sep, " %s " % sep)
    s = s.strip().lower()
    s = s.split()
    return s


def parse_sentence(s):
    global INDEX
    t = tokenize_sentence(s)
    INDEX = 0
    TOKENS.clear()

    for tok in t:
        TOKENS.append(tok)
    print(TOKENS)
    while INDEX < len(TOKENS):
        process_token()


def _put():
    subj = process_token()
    prep = process_token()
    obj = process_token()
    print ("PUT:", subj, prep, obj)
    if subj == 'block':
        if obj == 'table':
            TABLE.append(BASKET.pop())
        elif obj == 'basket':
            BASKET.append(TABLE.pop())


def _and():
    return process_token()


def _a():
    return process_token()


def _the():
    return process_token()


if __name__ == "__main__":
    print("BASKET:", BASKET)
    print("TABLE:", TABLE)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    parse_sentence("Put a block on the table and put a block on the table Bob.")
    print("BASKET:", BASKET)
    print("TABLE:", TABLE)
