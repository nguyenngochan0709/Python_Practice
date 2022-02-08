source = input("Enter a file name: ")
para = open(source, "r")
for line in para:
    xline = line.rstrip()
    upline = xline.upper()
    print(upline)
