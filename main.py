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
        count = 0
        inp = list()
        print("Setting rotation skills...")
        self.keys = input("Which keys should we set? (qwerasdf)")
        self.biggest = 0
        for key in self.keys:
            self.cooldowns[key] = int(input("Skill "+key+" cooldown?: "))
            if self.cooldowns[key] > self.biggest:
                self.biggest = self.cooldowns[key]
            count += 1
        for h in self.cooldowns:
            if self.cooldowns[h] > 0:
                inp.append(h)
        self.coolQueue = list(itertools.permutations(inp))
        self.fuzziness = int(input("Fuzziness? (leeway) :"))
    def comp(self, first, second):
        for v in first:
            if v in second:
                return True
        return False
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
                if (tot == first and dontloop == False) or (tot <= first + self.fuzziness and tot >= first)and dontloop == False:

                    out.append(i[:count+1])
                    break
                count += 1
        out = list(dict.fromkeys(out))
        return out
r = Rotation()

r.doInput()
print(r.findOut())
