fname = input('Enter a file name: ')
para = open(fname)
i = 0
tot = 0
for line in para:
    if line.startswith('X-DSPAM-Confidence:'):
        i = i + 1
        colloc = line.find(':')
        extr = line[colloc+1:]
        num = extr.strip()
        fnum = float(num)
        tot = tot + fnum
aver = tot/i
print('Average spam confidence:', aver)
