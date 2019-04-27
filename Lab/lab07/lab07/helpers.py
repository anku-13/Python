import Animals
# from Animals import Birds, Fish, Mammals, SquirmyThings

def print_members(mammals):
    print('list:')
    for m in mammals.members:
        print('  {}'.format(m))

def sort_members(mammals):
    mammals.members.sort()

# def main():
#     mammals = Animals.Mammals.Mammals.Mammals()
#     fishy = Animals.
#     sort_members(mammals)
#     print_members(mammals)
#
# if __name__ == "__main__" :
#     main()
