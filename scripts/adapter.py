import readfiles
import learnAlgorithms as learn
from plot import Plot as Plot

class Adapter(object):

    def __init__(self, kernel, turnPlot, interactions):
        self.log("Lendo Dados")
        rf = readfiles.ReadFiles()
        self.data = rf.getData()
        self.labels = rf.getLabels()
        self.la = learn.LearnAlgorithms(self.data, self.labels)
        self.kernel = kernel
        self.turnPlot = turnPlot
        self.interactions = interactions

    def run(self):
      acs_vector, log_values = self.la.runSVM(self.kernel, self.turnPlot, self.interactions)

      if(self.turnPlot):
        Plot.plot_c(acs_vector, log_values)
    
    def log(self, msg):
        print('[Adapter] {}'.format(msg))
