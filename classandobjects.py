
class soda:
    def introduce_self(self):
	print ('my name is ' + self.name )
s1 = soda()
s1.name = 'coke'
s1.color = 'red'
s1.calories = 140

s1.introduce_self()
s2 = soda()
s2.name = 'sprite'
s2.color = 'green'
s2.calories = 100

s1.introduce_self()
s2.introduce_self()

class person:
    def __init__(self, n, p, i):
	self.name = n
	self.personality = p
	self.is_sitting = i
	print (n, p, i)
    def sit_down(self):
	self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
p1 = person('alice', 'aggressive', False)
p2 = person('Becky', 'talkative', True)

p1.soda_owned = s2
p2.soda_owned = s1

p1.soda_owned.introduce_self()
im writing this so i can have words in this file 
