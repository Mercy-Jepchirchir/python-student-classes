#using while, if and continue statement  print all te numbers that are divisible by 5 between 100 and 200
x= 100
y=200
while x<y:
    x+=1
    if x%5 !=0:
        continue
    print(x)
