from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score



class LearnAlgorithms(object):

    def __init__(self):
        log("Learning")

    def log(self, msg):
        print('[Learn] {}'.format(msg))
