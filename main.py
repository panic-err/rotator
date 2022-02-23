
class Rotation(object):
    cooldowns = {
        'one' : '0',
        'two' : '0',
        'three' : '0',
        'four' : '0',
        'five' : '0',
        'six' : '0',
        'seven' : '0',
        'eight' : '0'
        }
    
    skills = {
        'one' : '',
        'two' : '',
        'three' : '',
        'four' : '',
        'five' : '',
        'six' : '',
        'seven' : '',
        'eight' : ''
        }
    
    
    def doInput(self):
        print("Setting rotation skills...")
        for key in self.cooldowns:
            self.cooldowns[key] = input("Skill "+key+" cooldown?: ")
        self.fuzziness = input("Fuzziness? (leeway) :")
        
    def calculateRotation(self):
        
r = Rotation()

r.doInput()
