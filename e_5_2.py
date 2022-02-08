largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    if largest == None:
        largest = fnum
        smallest = fnum
    elif fnum > largest:
        largest = fnum
    elif fnum < smallest:
        smallest = fnum
ilargest = int(largest)
ismallest = int(smallest)
print("Maximum is", ilargest)
print("Minimum is", ismallest)
