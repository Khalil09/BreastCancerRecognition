import argparse
from adapter import Adapter

# DEFAULT_PLOT = 'none'
# DEFAULT_TRAIN = False
DEFAULT_KERNEL = 'linear'
# DEFAULT_CROSSVAL = 10
DEFAULT_PLOT = False
DEFAULT_INTER = 20


def getAdapter():
    parser = argparse.ArgumentParser(description='A supervised machine learning approach using SVM to diagnose patients with breast cancer.')

    parser.add_argument('--kernel', dest='kernel', choices=['linear', 'rbf'], type=str, default=DEFAULT_KERNEL, help='Select Kernel of SVM')

    # parser.add_argument('-cv', dest='crossVal', type=int, default=DEFAULT_CROSSVAL, help='Select Cross Validation Value')

    # parser.add_argument('--train', dest='train', default=DEFAULT_TRAIN, type=bool, help='Enable or disable the training of the model')

    parser.add_argument('--plot', dest='turnPlot', default=DEFAULT_PLOT ,type=bool, help='Turn on the plot (Test erros x C panalty parameter)')
    parser.add_argument('-i', dest='interactions', default=DEFAULT_INTER ,type=int, help='Set numbers of interactions for plot')

    args = parser.parse_args()

    adapter = Adapter(args.kernel,
    				  args.turnPlot,
    				  args.interactions)

    return adapter
