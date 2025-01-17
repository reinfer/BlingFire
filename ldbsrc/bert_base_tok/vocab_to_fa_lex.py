
def token2regexp(token):
    is_internal = len(line) >= 2 and line[0] == '#' and line[1] == '#'
    tok = line if not is_internal else line[2:]
    anchor = "" if is_internal else "^ "

    reg = []
    chars = list(tok)
    for c in chars:
        if c == '\\':
            reg.append("[\\x5C]")
        elif c == ']':
            reg.append("[\\]]")
        elif c == '[':
            reg.append("[\\[]")
        elif c == '^':
            reg.append("[\\^]")
        elif c == '-':
            reg.append("[\\-]")
        else:
            reg.append("[" + c + "]")

    reg = "".join(reg)

    return anchor, reg


with open("vocab.txt", "r", encoding='utf-8') as i:
    with open("vocab.falex", "w", encoding='utf-8') as f:
        with open("tagset.txt", "w", encoding='utf-8') as t:
            for (id, line) in enumerate(i):

                if id < 100:
                    continue

                line = line.strip()
                anchor, reg = token2regexp(line)

                if reg is "":
                    continue

                print(" < " + anchor + reg + " > --> WORD_ID_" + str(id), file=f)
                print("WORD_ID_" + str(id) + " " + str(id), file=t)
