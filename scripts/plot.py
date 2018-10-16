import matplotlib.pyplot as plt

class Plot(object):

  @staticmethod
  def plot_c(acs_vector, log_values):

    acs_vector_error = [1-x for x in acs_vector]

    print(acs_vector_error)
    print(log_values)

    plt.xscale('log', basex=2)
    plt.xlabel('Valores de C')
    plt.ylabel('Erros de Teste')
    plt.plot(log_values, acs_vector_error, 'go--')

    plt.show()