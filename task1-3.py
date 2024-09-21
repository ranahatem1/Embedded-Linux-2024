# TASK 1

list_str=input("enter ur list") ## The input is taken as str
list_list=list(list_str) ## then it's converted to list to take its length
x=len(list_list)
y=0

for i in range(x):
    if int(list_list[i])==4: # don't forget to convert it to int for comparison
        y=y+1
    else: 
        y=y

print(y)

letters=input("\nput ur letter")
vowels=["aeiuoAEIUO"]

if letters in vowels:  ## sees whether the letter is in the given str or not
        print("True")
else:
        print("Flase")





## TASK 2

def circle_area(r): ## Arg: circle radius, returns the area
    area=3.14159*r**2
    print(area)
    return area

radius=float(input("put ur r here"))
circle_area(radius)

## Task 3

import calendar


