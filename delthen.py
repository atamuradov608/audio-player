
def isCorrect(word: str) -> bool:
    if ".hlm" not in word and ".brhl" not in word:
        return False
    tmp1 = (word.find(".hlm"), 4)
    tmp2 =  (word.find(".brhl"), 5)
    ind = max(tmp1, tmp2, key=lambda x: x[0])
    if not word[:ind[0]].isalnum():
        return False
    if ind[0] + ind[1] == len(word):
        return True
    elif ind[0] + ind[1] + 1 == len(word) and word[-1] == ".":
        return True
    return False


with open("input.txt", 'r') as file:
    l = file.readlines()

for line in l:
    for i in line.split():
        if (isCorrect(i)):
            if i[-1] == ".":
                i = i[:-1]
            print(i)
