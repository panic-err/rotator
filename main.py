
class Rotation(object):
    #qwer asdf
    cooldowns = {
        'q' : 0,
        'w' : 0,
        'e' : 0,
        'r' : 0,
        'a' : 0,
        's' : 0,
        'd' : 0,
        'f' : 0
        }
    
    skills = {
        'q' : '',
        'w' : '',
        'e' : '',
        'r' : '',
        'a' : '',
        's' : '',
        'd' : '',
        'f' : ''
        }

    added = {
        'q' : False,
        'w' : False,
        'e' : False,
        'r' : False,
        'a' : False,
        's' : False,
        'd' : False,
        'f' : False
        }
    queue = list()
    
    def doInput(self):
        print("Setting rotation skills...")
        self.keys = input("Which keys should we set? (qwerasdf)")
        biggest = 0
        for key in self.keys:
            self.cooldowns[key] = input("Skill "+key+" cooldown?: ")
            self.queue.append(self.cooldowns[key])
            if self.cooldowns[key] > biggest:
                biggest = self.cooldowns[key]
        #print(self.queue[0])
        self.fuzziness = input("Fuzziness? (leeway) :")
        
    def addCooldown(self, one, two):
        three = one + two
        return three
    def calculateRotation(self):
        print("Placeholder")
        count = 0
        for key in self.keys:
            self.addCooldown(self.queue[count], self.queue[count]) 
r = Rotation()

r.doInput()
print(r.addCooldown(1, 2))
