# # CS 224 Spring 2019 # Programming Assignment 3
 # # Your wonderful, pithy, erudite description of the assignment. -> Just read the read me
 # # Author: Julia
 # Date: March 13, 2019 #
from building import Building
import sys
# sys.argv - list of args

#
# b = Building(10,5, True)
# b.run(2,True)

def main() :
    # num floors
    nf = raw_input("Enter number of floors: ")
    while not nf.isdigit() or int(nf) <= 0 :
        nf = raw_input("Enter VALID NUMBER of floors: ")
    # num pass
    nf = int(nf)
    np = raw_input("Enter number of passengers: ")
    while not np.isdigit() or int(np) <= 0 :
        np = raw_input("Enter VALID NUMBER of passengers: ")
    np = int(np)
    # version
    ver = int(sys.argv[1]) if len(sys.argv) >=2 and sys.argv[1].isdigit() else 1
    # output
    pb = bool(sys.argv[2]) if len(sys.argv) >= 3 else True
    # debug
    debug = bool(sys.argv[3]) if len(sys.argv) >= 4 else False
    print("nf {}".format(nf))
    b = Building(nf, np, debug)
    b.run(ver, pb)

if __name__ == "__main__":
    main()
