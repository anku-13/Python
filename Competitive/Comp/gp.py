
def gp(l):
    l.sort()
    # print(l)
    sums = [0] * len(l)
    for i,e in enumerate(l) :
        sums[i] = (len(l) - i ) * e
    # print(sums)
    return max(sums)

def main():
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        listy = []
        for j in range(n):
            p = map(int, raw_input().split())
            for k in range(p[0]):
                listy.append(p[1])
        print("Case {}: {}".format(i+1, gp(listy)))

if __name__ == "__main__":
    main()
