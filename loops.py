c = (range(1, 40))
for i in c:
     if i % 3 == 0:	#multiple of three
         print (i)


print ' doing another operation'

for i in c:
    if i % 2 == 0:	#multiple of 2
        print (i)
a = [67, 5436, 545, 43543, 345, 67, 6564, 44, 644, 3454, 666743434564566]
print 'adding to the list'
a.append(90234920)
print (a)
print 'deleting '
a.pop()
print (a)
print 'switching a1 with a a6'
c = a[1]
a[1] = a[6]
a[6] = c
print (a)
print 'adding the remainder of a6 and a7'
a.append( a[6] % a[7])
print (a)

print (5436 / 44)	#this equals 123
print (44 * 123)	
print (44 * 123 - 5436)

