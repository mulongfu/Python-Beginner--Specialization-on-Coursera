hrs = input("Enter Hours:")
rate = input("Enter Rates:")

fhrs = float(hrs)
frate = float(rate)
def computepay(h,r):
    if h >= 40.0:
        new = (h - 40) * (1.5 * r)
        total = 40.0 * r + new
        return total

p = computepay(fhrs, frate)
print(p)