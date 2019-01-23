import codecs

with open("../data.txt", "r") as file:
    qfile = codecs.open("data/q.txt", "w", encoding="ascii", errors="ignore")
    afile = codecs.open("data/a.txt", "w", encoding="ascii", errors="ignore")

    buf = []
    abuf = []
    found_questions = False
    for line in file:
        if not found_questions:
            if len(line) > 1:
                buf.append(line)
            else:
                found_questions = True
        else:
            if len(line) > 1:
                abuf.append(line)
            else:
                found_questions = False
                answer = " ".join(abuf).replace("\n", "") + "\n"
                for line in buf:
                    qfile.write(line)
                    afile.write(answer)
                buf.clear()
                abuf.clear()
    qfile.close()
    afile.close()
