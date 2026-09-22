# Write a program to convert kilometers to miles. 

kilometers = float(input("Enter distance in kilometers: "))

# conversion factor : 1 kilometer = 0.6213 miles 

conversion = 0.621371 

miles = kilometers * conversion 

print(f"{kilometers} kilometers is equal to {miles} miles")