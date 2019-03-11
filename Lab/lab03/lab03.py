from random import random, randint

def uniform_crossover(parent1, parent2, inpb) :
    child1 = [x for x in parent1]
    for i in range(len(parent1)) :
        if random() < inpb :
            child1[i] = parent2[i]
    child2 = [x for x in parent2]
    for i in range(len(parent2)) :
        if random() < inpb :
            child2[i] = parent1[i]
    return child1, child2

def one_point_crossover(parent1, parent2) :
    k = randint(0, len(parent1))
    child1 = parent1[0:k] + parent2[k:len(parent2)]
    child2 = parent2[0:k] + parent1[k:len(parent1)]
    return child1, child2

def two_point_crossover(parent1, parent2) :
    k = randint(0, len(parent1))
    j = randint(0, len(parent1))
    print j , k
    child1 = []
    child2 = []
    if j > k :
        child1 = parent1[0:k] + parent2[k:j] + parent1[j:len(parent1)]
        child2 = parent2[0:k] + parent1[k:j] + parent2[j:len(parent1)]
    else :
        child1 = parent1[0:j] + parent2[j:k] + parent1[k:len(parent1)]
        child2 = parent2[0:j] + parent1[j:k] + parent2[k:len(parent1)]
    return child1, child2

par1 =[1,1,1,1,1,1,1,1,1,1,1]
par2 =[0,0,0,0,0,0,0,0,0,0,0]
print(uniform_crossover(par1, par2, .5))
print(one_point_crossover(par1, par2))
print(two_point_crossover(par1, par2))
