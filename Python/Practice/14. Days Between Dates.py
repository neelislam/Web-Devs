from datetime import date
# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days


from datetime import date

# Input dates in dd/mm/yyyy format
fDate = input("Enter first date (dd/mm/yyyy): ").split('/')
sDate = input("Enter second date (dd/mm/yyyy): ").split('/')

# Convert string parts into integers for year, month, day
fDate = date(int(fDate[2]), int(fDate[1]), int(fDate[0]))
sDate = date(int(sDate[2]), int(sDate[1]), int(sDate[0]))

# Calculate difference
res = fDate - sDate
print(f"Estimated time is {res.days} days")
# Another way
res = abs((fDate - sDate).days)
print(f"Estimated time is {res} days")
# --- IGNORE ---