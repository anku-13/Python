from random import randint
from random import shuffle
from sys import exit

class Master():
    def __init__(self, d=False):
        self.debug = d                               ## SET TRUE TO REVEAL TARGET
        self.colors = ['B', 'W', 'R', 'G', 'P', 'O']
        self.ccts = [0] * len(self.colors)
        self.board = [[[self.colors[c] for c in [randint(0, 5) for _ in range(0, 4)]]], [['T', 'A', 'R', 'G']]]
        for i in range(0, len(self.board[0][0])):
            self.ccts[self.colors.index(self.board[0][0][i])] += 1

    def get_board(self):
        return self.board

    def get_guess(self):
        print('Potential guesses: {}'.format(' '.join(self.colors)))
        guess = [0] * 4
        for i in range(0, 4):
    		# While guess is invalid, get new guess
    		while guess[i] not in self.colors:
    			guess[i] = raw_input('Please enter a valid guess number {}: '.format(i + 1)).upper()
    			# User types q or Q to quit
    			if guess[i] == 'Q':
    				exit('Thanks for playing!')
    	return guess

    # Evaluates the user's guess
    def evaluate_guess(self, guess, target):
    	gcts = [0] * len(self.colors)
    	pegs = ['-'] * len(guess)
    	# Get black pegs first because of white peg problem
    	for i in range(0, len(guess)):
    		if guess[i] == target[i]:
    			pegs[i] = 'b'
    			gcts[self.colors.index(guess[i])] += 1
    	# Get white pegs depending on black pegs and identified color count
    	for i in range(0, len(target)):
    		if pegs[i] != 'b' and gcts[self.colors.index(guess[i])] != self.ccts[self.colors.index(guess[i])]:
    			for j in range(len(target)):
    				if guess[i] == target[j]:
    					pegs[i] = 'w'
    					break
    	shuffle(pegs)
    	return pegs

    def __str__(self):
        s = ""
    	n = 1
    	if self.debug:   # Index to target for printing
    		s+='DEBUG MODE. FIRST ROW IS TARGET PATTERN.\n'
    		n = 0
    	s+='---------------------\n'
    	for i in range(n, len(self.board[0])):
    		s+='| {} | {} |'.format(' '.join(self.board[0][i]), ' '.join(self.board[1][i]))+"\n"
    	s+='---------------------\n'
        return s

def main():
    m = Master()   # Create game
    print("Welcome to Mastermind! Try to guess the pattern of colors!")
    print("The pegs to the right of your guess convey its quality, and are displayed in a random order.")
    guess = m.get_guess()         # Get first guess
    board = m.get_board()
    print(0)
    count = 1                   # Initialize count
    while guess != board[0][0]:
    	board[0].append(guess)  # Append guess and evaluated guess
    	board[1].append(m.evaluate_guess(guess, board[0][0]))
    	print(m)      # Print

    	guess = m.get_guess()     # Next guess and increment count
    	count += 1
    print("You guessed the correct pattern in {} guesses! : {}".format(count, ' '.join(board[0][0])))

if __name__ == '__main__':
	main()
