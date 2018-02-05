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

    def eval(self):
        print('Result: {}'.format(self.__graph.eval()))

    def __pprint(self, graph, level):
        if graph.op != 'Num':
            print('  ' * level + graph.op)
        if graph.op_type == 'UnOp':
            if graph.op == 'Num':
                print('  ' * level + str(graph.op1))
            else:
                self.__pprint(graph.op1, level+1)
        if graph.op_type == 'BinOp':
            self.__pprint(graph.op1, level+1)
            self.__pprint(graph.op2, level+1)

    def pprint(self):
        self.__pprint(self.__graph, 0)

    def __obj(self, obj, *args):
        return type(obj)(*args)

    def __reduce_neg(self, graph):
        if graph.op_type == 'UnOp':
            if graph.op == 'Neg': 
                if graph.op1.op == 'Num':
                    return self.__obj(graph.op1, -graph.op1.op1)
                else:
                    return Neg(self.__obj(graph, self.__reduce_neg(graph.op1)))
            if graph.op == 'Num':
                return Num(graph.op1)
        if graph.op_type == 'BinOp':
            return self.__obj(graph, self.__reduce_neg(graph.op1), self.__reduce_neg(graph.op2))
       
    def reduce_neg(self):
        self.__graph = self.__reduce_neg(self.__graph)

    def __reduce_add(self, graph):
        if graph.op_type == 'UnOp':
            return self.__obj(graph, self.__reduce_add(graph.op1))
        if graph.op_type == 'BinOp':
            if graph.op == 'Add':
                if graph.op1.op == 'Num' and graph.op2.op == 'Num':
                    return Num(graph.op1.op1 + graph.op2.op1)
                if graph.op1.op == 'Num':
                    return self.__obj(graph, Num(graph.op1.op), self.__reduce_add(graph.op2))
                if graph.op2.op == 'Num':
                    return self.__obj(graph, self.__reduce_add(graph.op1), Num(graph.op2.op)) 
                else:
                    return self.__obj(graph, self.__reduce_add(graph.op1), self.__reduce_add(graph.op2))
            else:
                return self.__obj(graph, self.__reduce_add(graph.op1), self.__reduce_add(graph.op2))

    def reduce_add(self):
        self.__graph = self.__reduce_add(self.__graph)

 
        
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
#g.pprint()
#g.eval()



# Test of reducing addition
math = Add(
    Neg(Num(5.0)),
    Add(
        Num(2.0),
        Num(-4.0)
    )
)

g = Graph(math)
g.pprint()
g.reduce_neg()
g.pprint()
g.reduce_add()
g.pprint()



