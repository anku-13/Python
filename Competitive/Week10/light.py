import sys
lights = [[0]*1000 for _ in range(1000)]

def toggle(x1, y1, x2, y2):
    global lights
    for i in range(x1, x2+1) :
        for j in range(y1, y2+1):
            lights[i][j] = int(not lights[i][j])

def on(x1, y1, x2, y2) :
    global lights
    for i in range(x1, x2+1) :
        for j in range(y1, y2+1):
            lights[i][j] = 1

def off(x1, y1, x2, y2) :
    global lights
    for i in range(x1, x2+1) :
        for j in range(y1, y2+1):
            lights[i][j] = 0

def main():
    global lights
    for line in sys.stdin:
        # print line
        line = line.split()
        if line[0] == "turn" :
            c = line[2].split(",") + line[4].split(",")
            c = map(int, c)
            if line[1]  == "on" :
                on(c[0], c[1], c[2], c[3])
            else :
                off(c[0], c[1], c[2], c[3])
        else :
            c = line[1].split(",") + line[3].split(",")
            c = map(int, c)
            toggle(c[0], c[1], c[2], c[3])
    s = 0
    for l in lights :
        s += sum(l)
    print("There are {} lights on now.".format(s))

if __name__ == "__main__" :
    main()
