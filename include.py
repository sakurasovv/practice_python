wordlist = ["cool", "lock", "cook"]
result = []

for i in wordlist[0]:
    acc = 1
    for j in range(1, len(wordlist)):
        if wordlist[j - 1].count(i) > 0 and wordlist[j].count(i) > 0 :
            acc += 1

    if acc == len(wordlist) :
        result.append(i)
        for z in range(len(wordlist)):
            wordlist[z] = wordlist[z].replace(i, "")

print(result)