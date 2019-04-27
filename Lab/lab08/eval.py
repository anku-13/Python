from character import Character
import utilities as u

def make_dict(lines) :
    # print(lines)
    d = {}
    for i in range(0, len(lines), 3) :
        d[lines[i+2]] = Character(lines[i],lines[i+1])
        # print(d[lines[i+2]])
    return d

def main() :
    print("here")
    d = make_dict(u.read_characters("characters.txt"))
    u.print_menu(d)
    ch = raw_input()
    while ch != "quit":
        if ch in d :
            d[ch].increment_evil()
        u.print_menu(d)
        ch = raw_input()
    # print d
    max = 0
    chr = "no evil"
    for k in d.keys():
        if d[k].get_evil() > max :
            max = d[k].get_evil()
            chr = d[k]
    print("Most evil is {} with {}".format(chr.get_name(),max))

if __name__ == "__main__" :
    main()
