from mountains import Mountain

def main() :
    lines = open("mountains.txt","r").readlines()
    swiss_mountains = []
    for l in lines :
        l = l.split()
        if len(l) < 5 :
            break
        swiss_mountains.append(Mountain(l[0], int(l[1]), int(l[2]), tuple(l[3].split(":")), tuple(l[4].split(":"))))

    print(Mountain.num_mountains)

    x = 4 - +2
    print x
    # for m in swiss_mountains :
    #     m.mprint()
    #     del m
    #     print

if __name__ == "__main__" :
    main()
