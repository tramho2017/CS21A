from random import randrange


class Card:
    '''create card class'''

    def __init__(self, rank, suit):

        # must assign because use with getRank()
        self.rank = rank

        # for card J,Q,K mark as ten value.
        if self.rank > 10:
            self.value = 10
        else:
            # other card leave it equal to self.rank
            self.value = self.rank

        # define suit full name
        if suit == 1:self.suit = 'Diamonds'
        elif suit == 2:self.suit = 'Clubs'
        elif suit == 3:self.suit = 'Hearts'
        elif suit == 4:self.suit = 'Spades'

        # define real value
        if self.rank == 1:self.nName = 'Ace'
        elif self.rank == 2:self.nName = 'Two'
        elif self.rank == 3:self.nName = 'Three'
        elif self.rank == 4:self.nName = 'Four'
        elif self.rank == 5:self.nName = 'Five'
        elif self.rank == 6:self.nName = 'Six'
        elif self.rank == 7:self.nName = 'Seven'
        elif self.rank == 8:self.nName = 'Eight'
        elif self.rank == 9:self.nName = 'Nine'
        elif self.rank == 10:self.nName = 'Ten'
        elif self.rank == 11:self.nName = 'Jack'
        elif self.rank == 12:self.nName = 'Queen'
        elif self.rank == 13:self.nName = 'King'

    def __str__(self):
        return self.nName + ' of ' + self.suit

    def BJvalue(self):
        '''define self.value and return it'''
        return self.value

    def getRank(self):
        '''return rank of this card'''
        return self.rank

    def getSuit(self):
        '''return suit of this card'''
        return self.suit


def main():
    '''Main algorithm'''

    printIntro()
    n, test = getInput()

    if test != 'error':
        for i in range(n):
            card = drawCard()
            printCardInfo(i, card)


def printIntro():
    '''Prin program name.'''
    print('Drawing card program.\n')


def getInput():
    '''Ask user input and verify it'''

    # create blank value for return process
    n = test = 0

    # first firewall try to catch user input problem
    try:
        n = eval(input('How many card do you need? '))
        print()

    except ValueError:
        print('\nError! Only integer number acceptable.')
        test = 'error'

    except NameError:
        print('\nError! Only integer number acceptable.')
        test = 'error'

    except:
        print('Unknow error!')
        test = 'error'

    # second firewall in case he enter minus number
    if test != 'error':
        n, test = verifyInput(n, test)

    return n, test


def verifyInput(n, test):
    '''Verify user input that he's not enter something to break program'''

    if n <= 0:
        test = 'error'
        print('\nError!. You must provide positive integer number.')

    return n, test


def drawCard():
    '''Draw cards many as user want.'''

    # generate value of each card
    rank, suit = genCardValue()
    # create object card
    x = Card(rank, suit)

    return x


def genCardValue():
    '''randomly generate rank between 1-13 and suit between 1-4'''

    r = randrange(1, 14)
    s = randrange(1, 5)

    return r, s


def printCardInfo(i, card):
    '''Print card detail.'''
    print('Card', i + 1, 'is ', card, 'which has value of', card.BJvalue())


if __name__ == '__main__': main()
