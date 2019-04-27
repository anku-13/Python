def shortest_path(rc, grid) :
    t = [0] * rc[1]
    gp = [t for _ in range(rc[0])]
    print(gp)
    return 0

def main() :
    tests = int(raw_input(""))
    for i in range(tests) :
        rc = map(int, raw_input("".split()))
        grid = []
        for j in range(rc[0]) :
            grid.append(map(int, raw_input("".split())))
        print(shortest_path(rc, grid))

if __name__ == "__main__" :
    main()
