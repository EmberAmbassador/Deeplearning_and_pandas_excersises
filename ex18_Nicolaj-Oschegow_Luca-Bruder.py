# Oschegow Nicolaj, Bruder Luca

# a) Keys are unique while values are not. This means each key
# can only occur once but values can occur multiple times. Since
# each person is supposed to only get one gift it would make
# alot more sense to use persons as keys.

# b)

gift_dict = {'Playmobil ': 'Alf ', 'Slingshot ': 'Bart ', 'Guitar ':
'Lisa ', 'Earrings ': 'Nina ', ' Playstation ': 'Maya ', 'Books ':
'Lisa ', 'TV ': 'Alf ', 'Money ': 'Alf ', 'Joghurt ': 'Nobody '}

persons = dict()
multipleGifts = dict()


for val in gift_dict.values():
    if val not in persons:
        persons.update({val : 1})
    else:
        persons.update({val : persons.get(val) + 1})

for keyPerson in persons:
    presents = persons.get(keyPerson)
    if presents > 1:
        print(keyPerson + "is recieving " + str(presents) + " presents.")

        # c)

        print("These are the gifts " + keyPerson + "is recieving:")
        print("-------------")

        for keyGift in gift_dict:
            if gift_dict.get(keyGift) == keyPerson:
                print(keyGift)
        print("")




        
        

