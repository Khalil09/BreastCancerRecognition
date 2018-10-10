import readfiles
import learnAlgorithms as learn

class Adapter(object):

    def __init__(self):
        log("Running")

    def run(self):
        log("Running")


    def log(self, msg):
        print('[Adapter] {}'.format(msg))
