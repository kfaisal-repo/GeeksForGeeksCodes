t = int(input())
mainlist = []
outputlist = []

for i in range(0, t):
    maindixtionary = {}
    interdiction = {}

    nofelements = input()
    elements1 = input()
    noOfLNR = int(input())
    lnrlimts = input()

    maindixtionary["nofelements"] = nofelements

    elements = [int(l) for l in elements1.split()]

    maindixtionary["elements"] = elements
    maindixtionary["noOfLNR"] = noOfLNR

    tempsplit = lnrlimts.split()
    
    o = 0
    while o < noOfLNR:
        interdiction[o] = tempsplit[2*o] + " " + tempsplit[(2*o) + 1]
        o += 1
    
    maindixtionary["lnrlimts"] = interdiction
    mainlist.append(maindixtionary)

for j in mainlist:
    for k in j["lnrlimts"].values():
        sum_ele=0
        m = int((k.split())[0])
        while m <= int((k.split())[1]):
            sum_ele += j["elements"][m-1]
            m = m + 1
        outputlist.append(sum_ele)
    
    print(*outputlist, sep=" ")
