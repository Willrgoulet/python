a = [ 55, 23, 8, 9, 125]	#the list starts placements from 0 from left to right
print (a)
print ('adding 777')
a.append(777)
print (a)
a.append('this is adding this')
print (a)
print ('deleting last string that was appeneded')
a.pop()
print (a)
print ('this should print 8')
print a[2]			# .append adds things while .pop deletes
a[0] = 100
print ('just replaced 55 with 100')
print (a)
term = a[1]		# to switch things within the list you must create a new variable 
a[1] = a[3]
a[3] = term
print ('just switched 23 and 9')
print (a)
print ('if this worked your a straight g ;{')
