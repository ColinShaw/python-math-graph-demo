class UnOp(object):
    def __init__(self, op1):
        self.op = self.__class__.__name__
        self.op_type = self.__class__.__bases__[0].__name__
        self.op1 = op1

class BinOp(object):
    def __init__(self, op1, op2):
        self.op = self.__class__.__name__
        self.op_type = self.__class__.__bases__[0].__name__
        self.op1 = op1
        self.op2 = op2



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







class Graph(object):

    def __init__(self, graph):
        self.__graph = graph

    def __print_indented(self, indent, text):
        print('  ' * indent + text)

    def eval(self):
        print('Result: {}'.format(self.__graph.eval()))

    def print_graph(self, graph=None, level=0):
        if graph == None:
            graph = self.__graph
        if graph.op != 'Num':
            self.__print_indented(level, graph.op)
        if graph.op_type == 'UnOp':
            if graph.op == 'Num':
                self.__print_indented(level, str(graph.op1))
            else:
                self.print_graph(graph.op1, level+1)
        if graph.op_type == 'BinOp':
            self.print_graph(graph.op1, level+1)
            self.print_graph(graph.op2, level+1)

    def reduce_neg(self, graph=None):
        if graph == None:
            graph = self.__graph
        if graph.op_type == 'UnOp':
            if graph.op == 'Neg': 
                if graph.op1.op == 'Num':
                    print('1')
                    print -1.0 * graph.op1.op1
                    return Num(-1.0 * graph.op1.op1) 
                else:
                    print('2a')
                    return Neg(self.reduce_neg(graph.op1))
            if graph.op == 'Num':
                print('2b')
                return Num(graph.op1)
        if graph.op_type == 'BinOp':
            if graph.op == 'Add':
                print('3')
                return Add(self.reduce_neg(graph.op1), self.reduce_neg(graph.op2))
            if graph.op == 'Sub':
                print('4')
                return Sub(self.reduce_neg(graph.op1), self.reduce_neg(graph.op2))
            if graph.op == 'Mul':
                print('5')
                return Mul(self.reduce_neg(graph.op1), self.reduce_neg(graph.op2))
            if graph.op == 'Div':
                print('6')
                return Div(self.reduce_neg(graph.op1), self.reduce_neg(graph.op2))
        

        
'''
    def reduce_adds(self, graph=None):
        if graph == None:
            graph = self.__graph
        p = self.__class_name(graph)
        c1 = self.__class_name(graph.op1)
        c2 = self.__class_name(graph.op2)
        if p == 'Add' and c1 == 'Num' and c2 == 'Num':
            return Num(graph.op1.op1 + graph.op2.op1)
        if p != 'Num':
            return self.reduce_add(
        else:
            return graph
'''



# Random case for printing
math = Add(
    Mul(
        Neg(Num(5.0)),
        Num(2.0)
    ),
    Add(
        Mul(
            Num(-2.0),
            Neg(Num(2.0))
        ),
        Num(3.0)
    )
)

#g = Graph(math)
#g.print_graph()
#g.eval()



# Test of reducing addition
math = Add(
    Neg(Num(5.0)),
    Num(2.0)
)

g = Graph(math)
g.print_graph()
g.reduce_neg()
g.print_graph()

