import itertools


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
    queue = list(itertools.permutations(['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']))
    #print(queue)
    total = 0
    compare = 0
    
    def doInput(self):
        print("Setting rotation skills...")
        self.keys = input("Which keys should we set? (qwerasdf)")
        self.biggest = 0
        for key in self.keys:
            self.cooldowns[key] = int(input("Skill "+key+" cooldown?: "))
            self.queue.append(self.cooldowns[key])
            if self.cooldowns[key] > self.biggest:
                self.biggest = self.cooldowns[key]
        #print(self.queue[0])
        self.coolQueue = list(itertools.permutations(self.cooldowns))
        #print(self.coolQueue)
        self.fuzziness = int(input("Fuzziness? (leeway) :"))
    def findOut(self):
        for i in self.coolQueue:
            tot = 0
            count = 0
            first = 0
            for x in i:
                dontloop = False
                if first == 0:
                    first = self.cooldowns[x]
                    dontloop = True
                if dontloop == False:
                    tot = self.cooldowns[x] + tot
                if tot > first and tot > first + self.fuzziness:
                    return False
                elif tot < first:
                    print("Total less than first: "+ str(tot) + ":" +str(first))
                elif tot == first and dontloop == False:
                    return i[:count+1], count
                count += 1
    def recurse(self):
        
        for key in self.keys:
            if self.added[key] == False:
                self.added[key] = True
                self.total = self.total + self.cooldowns[key]
                self.skills[key] = key
                print(key)
                #self.queue.append(self.skills[i])
                if self.biggest < self.total:
                     return "biggest reached"
                else:
                     self.recurse()
        #otherthing = thing + recurse(thing)
        
        #return recurse(otherthing)
    def addCooldown(self, one, two):
        three = one + two
        return three
    def calculateRotation(self):
        print("Placeholder")
        #for key in self.keys:
        #    self.addCooldown(self.queue[], self.queue[count]) 
r = Rotation()

r.doInput()
#print(r.addCooldown(1, 2))
print(r.findOut())
#print(r.recurse())
