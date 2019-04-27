import sys

def evaluateRankings(c, r1, r2) :
    c1 = sorted(r1,reverse=True)
    c2 = sorted(r2,reverse=True)
    for i in range(c) :
        if r1.index(c1[i]) != r2.index(c2[i]) :
            return i + 1
    return 0

def main() :
    rank1 = []
    rank2 = []
    count = 0
    i = 1
    for line in sys.stdin:
        if not count :
            count = int(line)
        elif not rank1 :
            rank1 = map(int, line.split(" "))
        else :
            rank2 = map(int, line.split(" "))
            e = evaluateRankings(count ,rank1, rank2)
            print("Case {} : {}".format(i, e if e else "agree"))
            i+=1
            count = 0
            rank1 = []
            rank2 = []

if __name__ == "__main__" :
    main()
