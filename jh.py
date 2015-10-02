#! /bin/python

from pprint import pprint

class GitTraining(object):

    def __init__(self, message, pp=True):
        """
        Constructor
        `inputs`:
            `message`: `string` : returns the message output
            `pp`: `boolean` : define whether to pprint output
        """
        self.message = message
        self.pp = pp

    def print_message(self):
        if self.pp:
            pprint(self.message)

if __name__ == '__main__':
    gt = GitTraining("I'm in git training", pp=True)
    gt.print_message()
