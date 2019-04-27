def findPre(t) :
    pre = t[0]
    end = ""
    for i in range(1, len(t)) :
        row = t[i]
        pre += row[0:len(row)/2]
        end += row[len(row)/2:len(row)]
    print(pre+row)

def main():
     x = raw_input()
     while x != "$" :
        tree = []
        while x != "*" and x != "$" :
             tree.insert(0, x)
             x = raw_input()
        findPre(tree)
        tree = []
        if x != "$" :
            x = raw_input()

if __name__ == "__main__" :
    main()
