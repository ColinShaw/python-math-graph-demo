from ..base.unop import UnOp
from mul         import Mul
from num         import Num

class Neg(UnOp):

    def __init__(self, op1):
        UnOp.__init__(self, op1)

    def eval(self):
        return Mul(Num(-1.0), self.op1).eval()

