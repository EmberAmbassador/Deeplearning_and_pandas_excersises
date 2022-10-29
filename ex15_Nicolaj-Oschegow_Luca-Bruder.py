# Oschegow Nicolaj, Bruder Luca

#a)

# The assert keyword is useful for debugging. It enables the user
# to check whether a given condition is true or false. In the latter
# case an assertion error is raised.
# Additionally a message can be printed.

# The given example is a simple function to calculate the average age
# of a given number of participants.
def calcAvg(age):
    assert len(age) != 0, "List of participants should not be empty."
    return sum(age)/len(age)
participants = []
#print("The average age of all participants is ", calcAvg(participants))


#b)

import random
import logging
### NOTE: If you do NOT use Jupyter Lab, you can replace the following two lines...
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
# ... by the following line:
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def main():
    guess = ''
    while guess not in ('right', 'left'):
        print('Guess in which hand is a present! Enter right or left:')
        guess = input()
        logging.debug(guess)
    hands = [('left'), ('right')]
    hand = random.randint(0, 1) # 0 is left, 1 is right
    logging.debug(hand)
    logging.debug(hands[hand])
    if hands[hand] == guess:
        print('You got it, here is the present!')
    else:
        print('Wrong! Guess again!')
        guess = ''
        while guess not in ('right', 'left'):
            print('Guess in which hand is a present! Enter right or left:')
            guess = input()
            logging.debug(guess)
        if hands[hand] == guess:
            print('You got it, here is the present!')
        else:
            print('Nope! You do not seem to be very good at this game.')


logging.debug('Start of program')
if __name__ == '__main__':
    main()
logging.debug('End of program')
