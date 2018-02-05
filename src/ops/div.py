from ..base.binop import BinOp

class Div(BinOp):

    def __init__(self, op1, op2):
        BinOp.__init__(self, op1, op2)

    def eval(self):
        return self.op1.eval() / self.op2.eval()

