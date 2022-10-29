# Oschegow Nicolaj, Bruder Luca

L = ['Lucas Sankt ', 'Phillipp Klug ', 'Alf Redo ', 'Klaudia Kaiser ', 'Ute Beich ', 'Vanessa Trommler ', 'Lien Hsia ', 'Alf Redo ', 'Alf Redo ', 'Ute Beich ']

# a)

# Sorting the list as suggested in the hint is not necessary
L.sort()

aList = []
for name in L:
    if name in aList:
        continue
    else:
        aList.append(name)
print(aList)

# b)

bSet = set(L)
print(list(bSet))
