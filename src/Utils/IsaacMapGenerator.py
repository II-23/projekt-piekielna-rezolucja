from random import randint, random, choice
from math import floor

OFFSETS = [[0,1],[1,0],[0,-1],[-1,0]]

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def clamp(x, l, r):
    return max(l, min(r, x))

class MapGenerator():
    start = (0, 0)
    end = (0, 0)
    mapDict = set()
    mapArr = None
    mapList = []

    @classmethod
    def getneigh(cls, pos):
        ret = 0
        for off in OFFSETS:
            npos = add(pos, off)
            ret += ((npos[0], npos[1]) in cls.mapDict)
        return ret

    @classmethod
    def generate(cls, complexity):
        complexity = clamp(complexity, 1, 8)
        while True:
            cls.mapDict = set()
            cls.mapDict.add((0, 0))
            cls.start = (0, 0)

            attempts = 2 + randint(clamp((complexity-2)//3, 0, 2), clamp((complexity+2)//3, 0, 2))
            for _ in range(attempts):
                pos = (0, 0)
                segments = 2 + complexity//3 + floor((2 + complexity//5) * random())
                lstdir = -1
                for __ in range(segments):
                    length = randint(2, 5)//2
                    dir = randint(0, 3)
                    while dir == lstdir: dir = randint(0, 3)
                    lstdir = dir
                    for ___ in range(length):
                        pos = add(pos, OFFSETS[dir])
                        cls.mapDict.add((pos[0], pos[1]))

            possibleEnds = []

            for pos in cls.mapDict:
                if cls.getneigh(pos) == 1 and pos != cls.start:
                    possibleEnds.append(pos)

            if len(possibleEnds) == 0:
                continue

            if len(cls.mapDict) < 4:
                continue

            if not (5 + round(complexity*1.5) <= len(cls.mapDict) <= 5 + round(complexity*2.5)):
                continue

            cls.end = choice(possibleEnds)

            miny, minx, maxy, maxx = 100, 100, -100, -100

            for pos in cls.mapDict:
                miny = min(miny, pos[0])
                maxy = max(maxy, pos[0])
                minx = min(minx, pos[1])
                maxx = max(maxx, pos[1])

            cls.start = (-miny, -minx)
            cls.end = add(cls.end, (-miny, -minx))
            cls.mapArr = [[0 for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]

            if len(cls.mapArr)*2 < len(cls.mapArr[0]): continue
            if len(cls.mapArr[0])*2 < len(cls.mapArr): continue

            break
        
        cls.mapList = []

        for pos in cls.mapDict:
            cls.mapArr[pos[0]-miny][pos[1]-minx] = 1
            cls.mapList.append((pos[0]-miny, pos[1]-minx))

        return cls.mapArr
    
def demo():
    for i in range(0, 30):
        print(1 + i//3)
        MapGenerator.generate(1 + i//3)
        for arr in MapGenerator.mapArr:
            for v in arr:
                print(v, end='')
            print()
        print()

if __name__ == "__main__":
    demo()