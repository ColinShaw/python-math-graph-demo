from ..base.unop import UnOp

class Num(UnOp):

    def __init__(self, op1):
        UnOp.__init__(self, op1)

    def eval(self):
        return self.op1

