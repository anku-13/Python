def pair(l1,l2):
    print l1
    print l2
    sum1 = 0
    for i in range(len(l1)) :
        sum1 += l1[i] - l2[i] if l1[i] > l2[i] else l2[i] > l1[i]
    sum2 = 0
    for i in range(len(l1)):
        sum2 += l1[i] - l2[(i+1) % len(l1)]
    print sum1
    print sum2


def main() :
    n = int(raw_input())
    while n :
        l1 = []
        l2 = []
        for i in range(n):
            l1.append(int(raw_input()))
        for i in range(n):
            l2.append(int(raw_input()))
        pair(l1, l2)
        n = int(raw_input())

if __name__ == "__main__" :
    main()
