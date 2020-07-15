import random
from game import Person, bcolors


magic=[{"name":"Fire","cost":10,"dmg":100,"type":"black"},
       {"name":"Thunder","cost":12,"dmg":120,"type":"black"},
       {"name":"Blizzard","cost":10,"dmg":100,"type":"black"},
       {"name":"Meteor","cost":20,"dmg":200,"type":"black"},
       {"name":"Quake","cost":14,"dmg":140,"type":"black"},
       {"name":"Cure","cost":12,"dmg":120,"type":"white"},
       {"name":"Cura","cost":18,"dmg":200,"type":"white"}]

items=[{"name":"Potion","type":"potion","description":"Heals 50 hp","prop":50,"quantity":15},
       {"name":"Hi-Potion","type":"potion","description":"Heals 100 hp","prop":100,"quantity":5},
       {"name":"Super Potion","type":"potion","description":"Heals 500 hp","prop":500,"quantity":5},
       {"name":"Elixer","type":"elixer","description":"Fully restores HP/MP of one party member","prop":9999,"quantity":5},
       {"name":"MegaElixer","type":"elixer","description":"Fully restores party's HP/MP","prop":9999,"quantity":2},
       {"name":"Grenade","type":"attack","description":"Deals 500 damage","prop":500,"quantity":5}]

player=Person(500,65,60,34,magic,items)
enemy=Person(1200,65,45,25,magic,items)

running=True
while running:
    print("===================================================")
    player.choose_action()
    choice=input("Choose action: ")
    index=int(choice)-1
    #action process
    if index==0:
        dmg=player.hit_damage()
        enemy.take_damage(dmg)
        print("You hit for",dmg,"points!")

        enemy_dmg=enemy.hit_damage()
        player.take_damage(enemy_dmg)
        print("Enemy hit for",enemy_dmg,"points!")
        print("\nEnemy's hp: ", bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()), bcolors.ENDC)
        print("\nYour hp: ", bcolors.OKGREEEN, str(player.get_hp()) + "/" + str(player.get_maxhp()), bcolors.ENDC)
        print("Your mp: ",bcolors.OKBLUE,str(player.get_mp())+ "/" + str(player.get_maxmp()),bcolors.ENDC)
        print("===================================================")
    #magic process
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose magic: "))-1
        #method 1 starts here
        cost=magic[magic_choice]["cost"]
        current_mp=player.get_mp()
        if cost>current_mp:
            print(bcolors.FAIL,"You don't have enough mp!",bcolors.ENDC)
            continue

        dmgl = magic[magic_choice]["dmg"] - 5
        dmgh = magic[magic_choice]["dmg"] + 5

        if magic[magic_choice]["type"]=="black":
            magic_dmg=random.randrange(dmgl,dmgh)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[magic_choice]["name"], "hit for", magic_dmg,"points!")
        elif magic[magic_choice]["type"]=="white":
            heal=random.randrange(dmgl,dmgh)
            player.heal_player(heal)
            player.reduce_mp(cost)
            print(magic[magic_choice]["name"], "heals for",heal,"hp!")

        #method 2nd for magics
        """   
        player.choose_magic()
        magic_choice=int(input("Choose magic: "))-1
        cost=player.get_spell_cost(magic_choice)
        current_mp=player.get_mp()
        if cost>current_mp:
            print(bcolors.FAIL,"You don't have enough mp!",bcolors.ENDC)
            continue
   
        if magic_choice==0:
            magic_dmg=random.randrange(95,105)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[0]["name"],"hit for",bcolors.OKGREEEN,magic_dmg,bcolors.ENDC,"points!")
        elif magic_choice==1:
            magic_dmg=random.randrange(115,125)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[1]["name"], "hit for",magic_dmg,"points!")
        elif magic_choice==2:
            magic_dmg=random.randrange(95,105)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[2]["name"], "hit for",magic_dmg,"points!")
        elif magic_choice==3:
            magic_dmg=random.randrange(195,205)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[3]["name"], "hit for",magic_dmg,"points!")
        elif magic_choice==4:
            magic_dmg=random.randrange(135,145)
            enemy.take_damage(magic_dmg)
            player.reduce_mp(cost)
            print(magic[4]["name"], "hit for",magic_dmg,"points!")
        elif magic_choice==5:
            heal=random.randrange(115,125)
            player.heal_player(heal)
            player.reduce_mp(cost)
            print(magic[5]["name"], "heals for", bcolors.OKGREEEN,heal, bcolors.ENDC,"hp!")
        elif magic_choice == 6:
            heal = random.randrange(195, 205)
            player.heal_player(heal)
            player.reduce_mp(cost)
            print(magic[6]["name"], "heals for", bcolors.OKGREEEN, heal, bcolors.ENDC, "hp!")

        """

        enemy_dmg=enemy.hit_damage()
        player.take_damage(enemy_dmg)
        print("Enemy hit for",enemy_dmg,"points!")


        print("\nEnemy's hp: ", bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()), bcolors.ENDC)
        print("\nYour hp: ",bcolors.OKGREEEN,str(player.get_hp())+"/"+str(player.get_maxhp()),bcolors.ENDC)
        print("Your mp: ", bcolors.OKBLUE,str(player.get_mp())+"/"+str(player.get_maxmp()),bcolors.ENDC,)
        print("===================================================")
    #items process
    elif index==2:
        player.choose_item()
        item_choice=int(input("Choose item: "))-1
        if items[item_choice]["quantity"]==0:
            print(bcolors.FAIL,"None left...!!",bcolors.ENDC)
            continue
        if items[item_choice]["type"]=="potion":
            item_heal=items[item_choice]["prop"]
            player.heal_player(item_heal)
            items[item_choice]["quantity"]-=1
            print(bcolors.OKGREEEN,items[item_choice]["name"], "heals for", item_heal, "HP!", bcolors.ENDC)
        elif items[item_choice]["type"]=="elixer":
            player.hp=player.maxhp
            player.mp=player.maxmp
            items[item_choice]["quantity"] -= 1
            print(bcolors.OKGREEEN, items[item_choice]["name"], "fully restores HP/MP",bcolors.ENDC)
        elif items[item_choice]["type"]=="attack":
            propl=items[item_choice]["prop"]-5
            proph = items[item_choice]["prop"] + 5
            item_dmg= random.randrange(propl,proph)
            enemy.take_damage(item_dmg)
            items[item_choice]["quantity"] -= 1
            print(bcolors.OKGREEEN,items[item_choice]["name"],"attacks for",item_dmg,"HP!",bcolors.ENDC)
        enemy_dmg=enemy.hit_damage()
        player.take_damage(enemy_dmg)
        print("Enemy hit for",enemy_dmg,"points!")

        print("\nEnemy's hp: ", bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()), bcolors.ENDC)
        print("\nYour hp: ", bcolors.OKGREEEN, str(player.get_hp()) + "/" + str(player.get_maxhp()), bcolors.ENDC)
        print("Your mp: ", bcolors.OKBLUE, str(player.get_mp()) + "/" + str(player.get_maxmp()), bcolors.ENDC, )
        print("===================================================")

    #final result
    if enemy.get_hp()==0:
        print(bcolors.BOLD+bcolors.OKGREEEN,"You win!",bcolors.ENDC)
        running= False
    elif player.get_hp()==0:
        print(bcolors.BOLD+bcolors.FAIL,"Your enemy has defeated you!",bcolors.ENDC)
        running=False

