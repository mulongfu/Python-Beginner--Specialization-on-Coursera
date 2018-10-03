largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        now = int(num)    
    except:
        print("Invalid input")
        continue
    if largest is None :
        largest = now
    if smallest is None :
        smallest = now
    if now > largest :
        largest = now
    if now < smallest :
        smallest = now

print("Maximum is", largest)
print("Minimum is", smallest)