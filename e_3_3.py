score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Error, please enter a number between 0.0 and 1.0")
    quit()
if (fscore < 0.0) or (fscore >= 1.0):
    print("Error, please enter a score between 0.0 and 1.0")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
else:
    print("F")
