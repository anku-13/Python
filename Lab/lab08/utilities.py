
# parameter d is the dictionary of characters
def print_menu(d):
    keys = sorted(list(d.keys()))
    # print(chr(27) + "[2J")
    print('Potentially evil Westerosianites:')
    for k in keys:
        print('{}: {}'.format(k, str(d[k])))


def read_characters(filename):
    try:
        fn = open(filename, 'r')
    except IOError as error:
        print('IO Error.  Check your filename.')
        return []

    characters = fn.read().splitlines()
    fn.close()

    return characters
