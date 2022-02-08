para = open('mbox-short.txt')
i = 0
for line in para:
    if line.startswith('From '):
        split_line = line.split()
        email_address = split_line[1]
        i = i + 1
        print(email_address)
print('There were', i, 'lines in the file with From as the first word')
