text = "X-DSPAM-Confidence:    0.8475"
colloc = text.find(":")
fintext = text[colloc+1:]
extrnum = fintext.lstrip()
fextrnum = float(extrnum)
print(fextrnum)
