#in this exapmle we are acting like we dont know whats in the list but we only know its decending and we want the sum of only the posotive integers
list3 = [5, 4, 4, 3, 3, 2, 1, -2, -4, -6, -7]
total = 0
i = 0
while list3[i] > 0:	#here we are making sure i is greater than 0 so we get the posotive integers
    total += list3[i]	# (total = total + i)
    i += 1	# (i = i + 1)
print (total)
#if the function didnt have any intergers less than 0 all you would do for the function to work is 
#while i < len(list3) and list3[i] > 0:

#now im going to add up all the postive intergers using a FOR loop
Total = 0
for i in list3:
    if i <= 0:
        break	#the break statement breaks the loop
    Total += i
print (Total)
# now doing a while statement with a break statement within it 
ToTal = 0
i = 0
while True:
    ToTal += list3[i]
    i += 1
    if list3[i] <= 0:
        break
print (ToTal)

#now doing an operation where I add all the negative intergers
list5 = [7,5, 4, 4, 3, 1, -2, -3, -5, -7]
TOTAL = 0
i = 0
for i in list5:
    if i <= 0:
        TOTAL += i
print (TOTAL)


