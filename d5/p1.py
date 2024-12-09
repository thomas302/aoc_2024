import re
with open("input") as f:
    data = f.read()

rules = re.findall(r'(\d{2})\|(\d{2})',data)
data = re.findall(r"(\d{2},.*)\n", data)

def checkRule(rule, string):
    if rule[0] in string and rule[1] in string:
        if string.index(rule[0]) < string.index(rule[1]):
            return True
        return False
    return True

def checkEntry(entry, rules):
    passes = False
    for rule in rules:
        passes = checkRule(rule, entry)
        if not passes:
            break
    return passes

c = 0
for entry in data:
    if (checkEntry(entry, rules)):
        l = entry.split(',')
        c += int(l[len(l)//2])       
c