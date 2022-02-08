para = open('romeo.txt')
lst = list()
for line in para:
    line_spiltted = line.split()
    for word in line_spiltted:
        if (word in lst) == False:
            lst.append(word)
lst.sort()
print(lst)
