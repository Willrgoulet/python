list = [1, 3, 4, 1, 3]
set1 = set()
for x in list:
    set1.add(x)
print set1
total = 0 
for x in set1:
    total += x # total = total + x 
print total

print sum(set1) # this is alot quicker way of adding up all of the integers 
