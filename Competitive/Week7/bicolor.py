
def main() :

    n = int(raw_input(""))
    t = int(raw_input(""))
    hash = [[i, 0, []] for i in range(n)]
    for i in range(t) :
        e = map(int, raw_input("").split())
        hash[e[0]][2].append(e[1])
        hash[e[1]][2].append(e[0])

    c = 0

    for i in hash :
        

if __name__ == "__main__" :
    main()
