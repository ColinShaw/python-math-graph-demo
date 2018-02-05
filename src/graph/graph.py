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

