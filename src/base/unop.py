class UnOp(object):

    def __init__(self, op1):
        self.op = self.__class__.__name__
        self.op_type = self.__class__.__bases__[0].__name__
        self.op1 = op1

