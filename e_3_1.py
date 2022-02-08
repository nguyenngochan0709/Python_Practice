hours = float(input("Enter Hours: "))
rate_per_hours = float(input("Enter Rate per Hour: "))
if hours <= 40:
    gross_pay = hours * rate_per_hours
else:
    exceed_hours = hours - 40
    gross_pay = (40 * rate_per_hours) + (exceed_hours * (rate_per_hours * 1.5))
print(gross_pay)
