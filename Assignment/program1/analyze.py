#
# CS 224 Spring 2019
# Programming Assignment 1
#
# This program performs simple analysis of a data element across a
# large number of data files representing runs of a traveling salesman
# algorithm.
#
# Author: Julia Froegel
# Date: February 18, 2019 #

# Expects the following file structure
#   > datafiles
#       > <folder_name>
#           > <file_name>.runbest
#   > analyze.py

from os import listdir
from numpy import amin, average

# main funtion
def main() :
    path = 'datafiles'
    runs = listdir(path)
    fvalList = []
    for run in runs :
        # May need to change this so that it works on mac?
        f = open(path+"\\"+run+"\\"+run+".runbest", "r")
        lines = f.readlines()
        for line in lines :
            fvalList.append(findF(line))
    print("Number of Runs : {}".format(len(fvalList)))
    # print("Minimum        : {}".format(amin(fvalList)))
    # print("Mean           : {}".format(average(fvalList)))
    stats = findStats(fvalList)
    print("Minimum        : {}\nMean           : {}".format(stats[0], stats[1]))

# in <- list of numbers
# out <- list in the form [<min in input list> , <avg from input list>]
def findStats(list) :
    stats = [list[0], 0]
    for num in list :
        if (num < stats[0]) :
            stats[0] = num
        stats[1] += num
    stats[1] /= len(list)
    return stats

# in  <- string - line frome file
# out <- float  - returns the number that comes after the letter F or -1 if that is not found
def findF(line) :
    line = line.split(" ")
    for i in range(len(line)) :
        # can we assume that there will be an valid F ?
        if(line[i] == 'F') :
            return float(line[i+1])
    return -1

# calls main function
if __name__ == "__main__":
    main()
