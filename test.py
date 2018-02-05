from src.graph.graph import Graph
from src.ops.add     import Add
from src.ops.mul     import Mul
from src.ops.num     import Num
from src.ops.neg     import Neg

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

g = Graph(math)
g.print_graph()
g.eval()

