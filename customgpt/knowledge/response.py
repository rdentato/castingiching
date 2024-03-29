import sys
import re
import random

dir = "/mnt/data"

qst = sys.argv[1]

if qst[0] == '}' :
    dir = "."
    qst = qst[1:]

if qst == "@" :
    with open('iching.txt', 'r') as file:
        primary_hexagram = 1
        line = file.readline()
        while line:
            pos = file.tell()
            line = file.readline()
            mtc = re.match(f"^Hexagram: {primary_hexagram}",line)
            if mtc :
                primary_hexagram += 1
                print(f"{pos:05}")
        file.close()
        exit()

hexs = [  2,24, 7,19,15,36,46,11,16,51,40,54,62,55,32,34,
          8, 3,29,60,39,63,48, 5,45,17,47,58,31,49,28,43,
         23,27, 4,41,52,22,18,26,35,21,64,38,56,30,50,14,
         20,42,59,61,53,37,57, 9,12,25, 6,10,33,13,44, 1 ]

mv = []

ptrn = '\s*(\d+)\.?(\d)?\.?(\d)?\.?(\d)?\.?(\d)?\.?(\d)?\.?(\d)?\.?\s*(.+)'
mtc = re.match(ptrn,qst)

if mtc :
    primary_hexagram = ((int(mtc.group(1)) - 1) % 64) +1
    lns = 0
    while hexs[lns] != primary_hexagram :
        lns += 1
    k = 2
    while (k<8 and mtc.group(k) != None) :
        mv.append(int(mtc.group(k)))
        lns ^= (1<<(int(mtc.group(k))-1))
        k += 1
    secondary_hexagram = hexs[ lns ]
    qst = mtc.group(8)
    
else :
    lns = random.randint(0, 255) % 64
    primary_hexagram = hexs[ lns ]
    for k in range(6) :
        r = random.randint(0,255)
        l = 1 << k
        if ((lns & l) != 0 and r < 48) or (r < 16)  : # 16 marbles probabilities
            # print(f"r:{r} l:{lns & l}")
            mv.append(k+1)
            lns ^= l
    secondary_hexagram = hexs[ lns ]

if (primary_hexagram == 1 and secondary_hexagram == 2) or (primary_hexagram == 2 and secondary_hexagram == 1) :
    mv = [ "all" ]

print(f"Question: \"{qst}\"")
with open(f"{dir}/iching.txt", 'r') as file:
    file.seek((primary_hexagram-1) * 6)
    line = file.readline()
    file.seek(int(line))
    for k in range(3) :
        line = file.readline() 
        print ("Primary",line,end="")

    for k in range(6) :
        line = file.readline()
        if k+1 in mv :
            print("Changing",line,end="")

    line = file.readline()
    if "all" in mv :
        print("Changing", line,end="")

    file.seek((secondary_hexagram-1) * 6)
    line = file.readline()
    file.seek(int(line))
    for k in range(2) :
        line = file.readline() 
        print ("Secondary",line,end="")

    print("")

 
file.close()
