class BinOp(object):

    def __init__(self, op1, op2):
        self.op = self.__class__.__name__
        self.op_type = self.__class__.__bases__[0].__name__
        self.op1 = op1
        self.op2 = op2

