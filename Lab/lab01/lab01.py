def main() :
    names = list(map( str.strip, open("characters.txt","r").readlines()))
    counts = [0]*len(names)
    lines = open("shakespeare.txt","r").readlines()
    for line in lines :
        for i in range(len(names)) :
            counts[i] += line.count(names[i])
    for i in range(len(names)) :
        print("{:12s}\t: {:>3d}".format(names[i], counts[i]))

# calls main function
if __name__ == "__main__":
    main()
