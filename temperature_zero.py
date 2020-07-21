"""
Dans cet exercice, vous devez analyser un relevé de températures 
pour trouver quelle température se rapproche le plus de zéro.
"""
test = True
while test:
    n = int(input("N = "))  # the number of temperatures to analyse
    if n>=0 and n<10000:
        test = False

r1 = [] #positif list
r2 = [] #negatif list
v = input().split() #la valeur des n temperatures separé par des espaces 
if n  >= len(v):
    for i in v:
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if (t >=0):
            r1.append(t)
        else:
            r2.append(t)
    if r1 and r2: 
        if  min(r1) <= -max(r2):
            print(min(r1))
        else:
            print(max(r2))
    elif r1:
        print(min(r1))
    elif r2:
        print(max(r2))
    elif not r1 and not r2:
        print(0)
