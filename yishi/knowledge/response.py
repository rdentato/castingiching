hexagrams = [
"Qian (The Creative)",
"K'un (The Receptive)",
"Chun (Difficulty at the Beginning)",
"Meng (Youthful Folly)",
"Hsu (Waiting [Nourishment])",
"Sung (Conflict)",
"Shih (The Army)",
"Pi (Holding Together)",
"Hsiao Ch'u (The Taming Power of the Small)",
"Lü (Treading [Conduct])",
"T'ai (Peace)",
"P'i (Standstill [Stagnation])",
"T'ung Jen (Fellowship with Men)",
"Ta Yu (Possession in Great Measure)",
"Qian (Modesty)",
"Yu (Enthusiasm)",
"Sui (Following)",
"Ku (Work on What Has Been Spoiled [Decay])",
"Lin (Approach)",
"Kuan (Contemplation [View])",
"Shih Ho (Biting Through)",
"Pi (Grace)",
"Po (Splitting Apart)",
"Fu (Return [The Turning Point])",
"Wu Wang (Innocence [The Unexpected])",
"Ta Ch'u (The Taming Power of the Great)",
"Yi (Nourishment)",
"Ta Kuo (Preponderance of the Great)",
"K'an (The Abysmal [Water])",
"Li (The Clinging, Fire)",
"Hsien (Influence [Wooing])",
"Heng (Duration)",
"Dun (Retreat)",
"Ta Chuang (The Power of the Great)",
"Chin (Progress)",
"Ming I (Darkening of the Light)",
"Chia Jen (The Family",
"K'uei (Opposition)",
"Chien (Obstruction)",
"Hsieh (Deliverance)",
"Sun (Decrease)",
"I (Increase)",
"Kuai (Break-through [Resoluteness])",
"Kou (Coming to Meet)",
"Ts'ui (Gathering Together [Massing])",
"Sheng (Pushing Upward)",
"K'un (Oppression [Exhaustion])",
"Ching (The Well)",
"Ko (Revolution [Molting])",
"Ting (The Caldron)",
"Chen (The Arousing [Shock, Thunder])",
"Ken (Keeping Still, Mountain)",
"Jian (Development [Gradual Progress])",
"Kuei Mei (The Marrying Maiden)",
"Feng (Abundance [Fullness])",
"Lu (The Wanderer)",
"Sun (The Gentle [The Penetrating, Wind])",
"Tui (The Joyous, Lake)",
"Huan (Dispersion [Dissolution])",
"Chieh (Limitation)",
"Chung Fu (Inner Truth)",
"Hsiao Kuo (Preponderance of the Small)",
"Chi Chi (After Completion)",
"Wei Chi (Before Completion)"
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
if primary_hexagram == 1 and secondary_hexagram == 2 :
    print("Changing Lines 1.all: ")
elif primary_hexagram == 2 and secondary_hexagram == 1 :
    print("Changing Lines 2.all: ")
else :
    for k in mv :
        print(f"Changing Line {primary_hexagram}.{k}: ")
print(f"Secondary hexagram: {secondary_hexagram} {hexagrams[secondary_hexagram-1]}")
