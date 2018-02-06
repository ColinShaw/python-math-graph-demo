from ..ops.scalar import Neg, Num
from resolve      import obj


def reduce_neg(graph):
    if graph.op_type == 'UnOp':
        if graph.op == 'Neg': 
            if graph.op1.op == 'Num':
                return obj(graph.op1, -graph.op1.op1)
            else:
                return Neg(obj(graph, reduce_neg(graph.op1)))
        if graph.op == 'Num':
            return Num(graph.op1)
    if graph.op_type == 'BinOp':
        return obj(graph, reduce_neg(graph.op1), reduce_neg(graph.op2))
       
def reduce_add(graph):
    if graph.op_type == 'UnOp':
        return obj(graph, reduce_add(graph.op1))
    if graph.op_type == 'BinOp':
        if graph.op == 'Add':
            if graph.op1.op == 'Num' and graph.op2.op == 'Num':
                return Num(graph.op1.op1 + graph.op2.op1)
            if graph.op1.op == 'Num':
                return obj(graph, Num(graph.op1.op), reduce_add(graph.op2))
            if graph.op2.op == 'Num':
                return obj(graph, reduce_add(graph.op1), Num(graph.op2.op)) 
            else:
                return obj(graph, reduce_add(graph.op1), reduce_add(graph.op2))
        else:
            return obj(graph, reduce_add(graph.op1), reduce_add(graph.op2))


