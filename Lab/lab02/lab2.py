from random import randint

def main() :
    from os import listdir
    runs = [run for run in listdir('datafiles')]
    list1 = [x for x in runs if x+".rand" in listdir('datafiles/'+x)]
    print(list1)
    print(len(list1))
    list2 = [x for x in runs if not int(x.split(".")[1])%2]
    print(list2)
    print(len(list2))
    list3 = [pair for pair in [(x,y) for x in runs for y in runs] if not (int(pair[0].split(".")[1])+int(pair[1].split(".")[1]))%100]
    print(list3)
    print(len(list3))
    
    sevens = [ int(s) for s in [str(randint(1, 100)) for _ in range(20)] if "7" in s]
    print(sevens)



if __name__ == "__main__" :
    main()
