hrs = input("Enter Hours:")
rate = input("Enter Rates:")

fhrs = float(hrs)
frate = float(rate)

if fhrs >= 40:
    new = (fhrs - 40) * (1.5 * frate)
    total = 40 * frate + new
print(total)	