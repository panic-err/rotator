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
    
    def doInput(self):
        print("Setting rotation skills...")
        self.keys = input("Which keys should we set? (qwerasdf)")
        self.biggest = 0
        for key in self.keys:
            self.cooldowns[key] = int(input("Skill "+key+" cooldown?: "))
            if self.cooldowns[key] > self.biggest:
                self.biggest = self.cooldowns[key]
        #print(self.queue[0])
        self.coolQueue = list(itertools.permutations(self.cooldowns))
        #print(self.coolQueue)
        self.fuzziness = int(input("Fuzziness? (leeway) :"))
    def findOut(self):
        out = list()
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
                    break
                elif tot < first:
                    print("Total less than first: "+ str(tot) + ":" +str(first))
                elif (tot == first and dontloop == False) or tot == first + self.fuzziness:
                    if tot <= first + self.fuzziness and tot >= first:
                        print("Total falls within the fuzz range")
                    out.append(i[:count+1])
                    #return i[:count+1], count
                count += 1
        return out
r = Rotation()

r.doInput()
#print(r.addCooldown(1, 2))
print(r.findOut())
#print(r.recurse())
