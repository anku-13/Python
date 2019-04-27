def make_dict(n) :
    d = {}
    for i in range(n) :
        line = raw_input().split()
        d[line[0]] = int(line[1])
    return d

def eval_job(lines,d) :
    # print lines
    x = 0
    for line in lines:
        for word in line.split():
            if word in d:
                x += d[word]
    return x

def main() :
    x = map(int , raw_input().split())
    d = make_dict(x[0])
    # print(d)
    lines = []
    for i in range(x[1]) :
        line = raw_input()
        while line != "." :
            lines.append(line)
            line = raw_input()
        print(eval_job(lines, d))
        lines = []


if __name__ == "__main__" :
    main()
