import reduce_base

class Graph(object):

    def __init__(self, graph):
        self.__graph = graph

    def eval(self):
        print('Eval: {}'.format(self.__graph.eval()))

    def __print_indented(self, indent, text):
        print('  ' * indent + text)

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

    def reduce(self):
        graph = None
        while self.__graph != graph:
            self.__graph = reduce_base.reduce_neg(self.__graph)
            self.__graph = reduce_base.reduce_add(self.__graph)

    def reduce_neg(self):
        self.__graph = reduce_base.reduce_neg(self.__graph)

    def reduce_add(self):
        self.__graph = reduce_base.reduce_add(self.__graph)

