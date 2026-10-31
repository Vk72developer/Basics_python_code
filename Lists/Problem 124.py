# Second Largest Element

num = [10, 20, 60, 30, 60, 65]
largest = None 
second = None 
for n in num:
    if largest is None or n > largest:
        second = largest 
        largest = n 

    elif n != largest and (second is None or n > second):
        second = n 

print("Second largest:", second)