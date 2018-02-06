from base import UnOp, BinOp


class Num(UnOp):

    def __init__(self, op1):
        UnOp.__init__(self, op1)

    def eval(self):
        return self.op1


class Add(BinOp):

    def __init__(self, op1, op2):
        BinOp.__init__(self, op1, op2)

    def eval(self):
        return self.op1.eval() + self.op2.eval()


class Sub(BinOp):

    def __init__(self, op1, op2):
        BinOp.__init__(self, op1, op2)

    def eval(self):
        return self.op1.eval() - self.op2.eval()


class Mul(BinOp):

    def __init__(self, op1, op2):
        BinOp.__init__(self, op1, op2)

    def eval(self):
        return self.op1.eval() * self.op2.eval()


class Div(BinOp):

    def __init__(self, op1, op2):
        BinOp.__init__(self, op1, op2)

    def eval(self):
        return self.op1.eval() / self.op2.eval()


class Neg(UnOp):

    def __init__(self, op1):
        UnOp.__init__(self, op1)

    def eval(self):
        return Mul(Num(-1.0), self.op1).eval()

