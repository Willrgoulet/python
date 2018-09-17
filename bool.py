def sleep_in (weekday, vacation):
    if  weekday == False or vacation == True:
	print True
    else:
	print False
print 'should be false'
sleep_in (True, False)
print 'next = true'
sleep_in (False, True)
print 'next = false'
sleep_in (True, False)
print ' next should be true'
sleep_in (True, True)

