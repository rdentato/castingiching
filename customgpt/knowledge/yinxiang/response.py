hexagrams = [
"QIAN2, CREATING.",
"KUN1, ACCEPTING.",
"ZHUN1 (or TUN2), RALLYING.",
"MENG2, INEXPERIENCE.",
"XU1, ANTICIPATION.",
"SONG4, CONTENTION.",
"SHI1, THE MILITIA.",
"BI3, BELONGING.",
"XIAO3 CHU4, RAISING SMALL BEASTS.",
"LU3, RESPECTFUL CONDUCT.",
"TAI4, INTERPLAY.",
"PI3, SEPARATING.",
"TONG2 REN2, FELLOWSHIP w/ OTHERS.",
"DA4 YOU3, BIG DOMAIN.",
"QIAN1, AUTHENTICITY.",
"YU4, READINESS.",
"SUI2, FOLLOWING.",
"GU3, DETOXIFYING.",
"LIN2, TAKING CHARGE.",
"GUAN1, PERSPECTIVE.",
"SHI4 HE2, BITING THROUGH.",
"BI4, ADORNMENT.",
"BO1, DECOMPOSING.",
"FU4, RETURNING.",
"WU2 WANG4, WITHOUT PRETENSE.",
"DA4 CHU4, RAISING GREAT BEASTS.",
"YI2, HUNGRY MOUTH.",
"DA4 GUO4, GREATNESS IN EXCESS.",
"KAN3, EXPOSURE.",
"LI2, ARISING.",
"XIAN2, RECIPROCITY.",
"HENG2, CONTINUITY.",
"DUN4, DISTANCING.",
"DA4 ZHUANG4, BIG AND STRONG.",
"JIN4, EXPANSION.",
"MING2 YI2, BRIGHTNESS OBSCURED.",
"JIA1 REN2, FAMILY MEMBERS.",
"KUI2, ESTRANGEMENT.",
"JIAN3, IMPASSE.",
"JIE3, RELEASE.",
"SUN3, DECREASING.",
"YI4, INCREASING.",
"GUAI4, DECISIVENESS.",
"GOU4, DISSIPATION.",
"CUI4, COLLECTEDNESS.",
"SHENG1, ADVANCEMENT.",
"KUN4, EXHAUSTION.",
"JING3, THE WELL.",
"GE2, SEASONAL CHANGE.",
"DING3, THE CAULDRON.",
"ZHEN4, AROUSAL.",
"GEN4, STILLNESS.",
"JIAN4, GRADUAL PROGRESS.",
"GUI1 MEI4, LITTLE SISTER’S MARRIAGE.",
"FENG1, ABUNDANCE.",
"LU3, THE WANDERER.",
"XUN4 (or SUN4), ADAPTATION.",
"DUI4, SATISFACTION.",
"HUAN4, SCATTERING.",
"JIE2, BOUNDARIES.",
"ZHONG1 FU2, THE TRUTH WITHIN.",
"XIAO3 GUO4, SMALLNESS IN EXCESS.",
"JI4 JI4, ALREADY COMPLETE.",
"WEI4 JI4, NOT YET COMPLETE."
]

import sys
import re
import random

hexs = [  2,24, 7,19,15,36,46,11,16,51,40,54,62,55,32,34,
          8, 3,29,60,39,63,48, 5,45,17,47,58,31,49,28,43,
         23,27, 4,41,52,22,18,26,35,21,64,38,56,30,50,14,
         20,42,59,61,53,37,57, 9,12,25, 6,10,33,13,44, 1 ]

mv = []
qst = sys.argv[1]
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
        if random.randint(0,255) < 64 : # Three coins probabilities
            mv.append(k+1)
            lns ^= (1<<k)
    secondary_hexagram = hexs[ lns ]

print(f"Question: {qst}")
print(f"Primary hexagram: {primary_hexagram} {hexagrams[primary_hexagram-1]}")
print(f"Primary hexagram Image {primary_hexagram}: ")
if primary_hexagram == 1 and secondary_hexagram == 2 :
    print("Changing Lines 1.all: ")
elif primary_hexagram == 2 and secondary_hexagram == 1 :
    print("Changing Lines 2.all: ")
else :
    for k in mv :
        print(f"Changing Line {primary_hexagram}.{k}: ")
print(f"Secondary hexagram: {secondary_hexagram} {hexagrams[secondary_hexagram-1]}")
