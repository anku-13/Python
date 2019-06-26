# CS 224 - Intro To Python - Assignment 3 3

# Author #
Julia Froegel

# Description #
Randomly places Passengers and elevator in a building with N floors and takes them to their floors.
     * The simple algorithm starts by having the elevator go all the way up and then all the way down and repeating until all the passengers arrive at their destination floors.
     * The second one algorithm that I implemented follows the same general strategy as the simple one but the checks if it needs to go all the way up or all the way down. If it does not have to go all the way to the top floor then it will turn around. The performance of this strategy should on average be better because it can sometimes skip floors that it does not need to visit

# Usage #
Run program from the command line with the following form. 
The last 3 arguments are optional
`python otis.py <verson_num> <show_output> <debug_info>`
     * <version_num> - Specifics with version to run(optional). Options are 1 or 2. The default is 1. 1 is the simple alg and 2 is the second one.
     * <show_output> - Optional Boolean that controls whether the building state is printed to the console.
     * <debug_info> - Optional Boolean that controls if extra info is printed about the building for error checking.
