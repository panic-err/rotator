
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
    
    
    def doInput(self):
        print("Setting rotation skills...")
        keys = input("Which keys should we set? (qwerasdf)")
        for key in keys:
            self.cooldowns[key] = input("Skill "+key+" cooldown?: ")
        self.fuzziness = input("Fuzziness? (leeway) :")
        
    def calculateRotation(self):
        print("Placeholder")
r = Rotation()

r.doInput()
