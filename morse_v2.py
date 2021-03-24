lettre = {"a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.", "h": "....", "i": "..", "j": ".---", "k": "_._", "l": "._..", "m": "__",
          "n": "_.", "o": "___", "p": ".__.", "q": "__._", "r": "._.", "s": "...", "t": "_", "u": ".._", "v": "..._", "w": ".__", "x": "_.._", "y": "_.__", "z": "__.."}

morse = {'._': 'a', '_...': 'b', '_._.': 'c', '_..': 'd', '.': 'e', '.._.': 'f', '__.': 'g', '....': 'h', '..': 'i', '.___': 'j', '_._': 'k', '._..': 'l', '__': 'm',
         '_.': 'n', '___': 'o', '.__.': 'p', '__._': 'q', '._.': 'r', '...': 's', '_': 't', '.._': 'u', '..._': 'v', '.__': 'w', '_.._': 'x', '_.__': 'y', '__..': 'z'}
l = [];
qbis = 0

while qbis != 3:
    k = int(input(" veux tu traduire des lettre(0) ou du morse(1) ?"))
    if k == 0:
       q = str(input("quelle lettre veux-tu traduire ?"))
       for t in range(len(q)):
           l.append(q[t])
       for x in l:
           if x in lettre.keys():
               print(lettre[x])
       del l[:]
    elif k == 1:
        q = str(input("que veux tu décoder ?"))
        if q in morse.keys():
            print(morse[q])
        else :
            print("ceci n'est pas un caractère morse ")
    else :
        print("choisi 1(lettre) ou 0(morse)")
    qbis = int(input("encore un(e) lettre/mot ? oui(2) non(3)"))
        