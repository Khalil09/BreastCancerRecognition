from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np



class LearnAlgorithms(object):

    def __init__(self, data, labels):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(data, labels,
                                                                                test_size=0.30)

    def runSVM(self, kernel, turnPlot, interactions):
      acs_vector = []
      
      if(not turnPlot):
        log_values = [1]
      else:
        log_values = np.logspace(-5, 15, interactions, base=2)

      for c in log_values:
        self.log("Interação com C = {}".format(c))
        svm = SVC(kernel=kernel, gamma='auto', C=c)
        svm.fit(self.x_train, self.y_train)
        pred = svm.predict(self.x_test)
        acs = accuracy_score(self.y_test, pred)

        acs_vector.append(acs)
      
      self.log("SVM Accuracy Score: {}".format(acs))

      return acs_vector, log_values


    def log(self, msg):
        print('[Learn] {}'.format(msg))