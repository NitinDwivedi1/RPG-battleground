import random

class bcolors:
    HEADER= '\033[95m'
    OKBLUE= '\033[94m'
    OKGREEEN= '\033[92m'
    WARNING= '\033[93m'
    FAIL= '\033[91m'
    ENDC='\033[0m'
    BOLD = '\033[01m'
    UNDERLINE = '\033[04m'

class Person:
    def __init__(self,hp,mp,atk,dfn,magic,items):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkh=atk+10
        self.atkl=atk-10
        self.dfn=dfn
        self.magic=magic
        self.items=items
        self.action=["Attack","Magic","Items"]

    def get_maxhp(self):
        return self.maxhp
    def get_hp(self):
        return self.hp
    def get_maxmp(self):
        return self.maxmp
    def get_mp(self):
        return self.mp
    def reduce_mp(self,cost):
        self.mp-=cost
    def hit_damage(self):
        dmg=random.randrange(self.atkl,self.atkh)
        return dmg
    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<=0:
            self.hp=0
    def choose_action(self):
        print(bcolors.OKBLUE+"Actions-"+bcolors.ENDC)
        i=1
        for item in self.action:
            print(str(i)+". "+item)
            i+=1
    def choose_magic(self):
        print(bcolors.OKBLUE+"Magics-"+bcolors.ENDC)
        i=1
        for item in self.magic:
            print(str(i)+". "+item["name"]+"    "+str(item["dmg"])+"hp approx."+"    $"+str(item["cost"]))
            i+=1
    def get_spell_cost(self,magic_choice):
        return self.magic[magic_choice]["cost"]
    def heal_player(self,heal):
        self.hp+=heal
        if self.hp>self.maxhp:
            self.hp=self.maxhp
    def choose_item(self):
        print(bcolors.OKBLUE+"Items-"+bcolors.ENDC)
        i=1
        for item in self.items:
            print(str(i)+"."+item["name"]+": "+item["description"]+" (x"+str(item["quantity"])+")")
            i+=1



