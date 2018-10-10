import argparse
from adapter import Adapter

# DEFAULT_PLOT = 'none'
# DEFAULT_TRAIN = False
# DEFAULT_ALGORITHM = ''
# DEFAULT_CROSSVAL = 10
DEFAULT_PLOT = False


def getAdapter():
    parser = argparse.ArgumentParser(description='A supervised machine learning approach using SVM to diagnose patients with breast cancer.')

    # parser.add_argument('--algorithm', dest='algorithm', choices=[''], type=str, default=DEFAULT_ALGORITHM, help='Select Learning Algorithm')

    # parser.add_argument('-cv', dest='crossVal', type=int, default=DEFAULT_CROSSVAL, help='Select Cross Validation Value')

    # parser.add_argument('--train', dest='train', default=DEFAULT_TRAIN, type=bool, help='Enable or disable the training of the model')

    parser.add_argument('--plot', dest='confPlot', default=DEFAULT_PLOT ,type=bool, help='Change how confusion matrices are plot.')

    args = parser.parse_args()

    adapter = Adapter()

    return adapter
