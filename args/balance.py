from args.base import BaseArg


class UseBalancingArg(BaseArg):

    __default = True

    def __init__(self):
        pass

    @staticmethod
    def read_argument(args):
        return args.balance_samples[0]

    @staticmethod
    def add_argument(parser):
        parser.add_argument('--balance-samples',
                            dest='balance_samples',
                            type=lambda x: (str(x).lower() == 'true'),
                            nargs=1,
                            help='Balanced input of the Train set"')
