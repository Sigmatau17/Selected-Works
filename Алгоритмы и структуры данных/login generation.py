
def split(word):
    splitted = []
    for i in range(len(word)):
        splitted.append(word[i])
    return splitted

line = str(input())
words = list(map(str, line.split()))
name = split(words[0])
surname = split(words[1])

login = name[0]
for i in range(len(name) - 1):
    if ord(name[i + 1]) < ord(surname[0]):
        login = login + name[i + 1]
    else:
        break
login = login + surname[0]
print(login)