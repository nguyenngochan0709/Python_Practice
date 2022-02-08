def computepay(fh, fr):
    if fh > 40:
        gp = 40 * fr + ((fh - 40) * (1.5 * fr))
    else:
        gp = fh * fr
    return gp

h = input("Enter Hours: ")
r = input("Enter Rate per Hour: ")
try:
    fh = float(h)
    fr = float(r)
except:
    print("Error, please input a number")
    quit()
gross_pay = computepay(fh, fr)
print("Pay", gross_pay)
