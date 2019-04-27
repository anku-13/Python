from os import listdir
import colorama

def grep(f, w):
    # your code goes here
    w = w.lower()
    lines = open("datafiles/"+f,"r").readlines()
    for i, line in enumerate(lines) :
        if w in line.lower() :
            index = line.lower().index(w)
            print("{}:    {}:    {}".format(f,i,line[0:index]+"\033[1;31;40m"+line[index:index+len(w)]+"\033[1;0;40m"+line[index+len(w):]))

def main():
    # call grep from here
    colorama.init()
    files = listdir("datafiles")
    word = "Victor"
    for file in files :
        grep(file, word)
    colorama.deinit()

if __name__ == '__main__':
    main()
