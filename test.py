from src.ops.scalar import Num, Neg, Add, Mul
from src.graph.base import Graph


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
g.pprint()
g.eval()


math = Add(
    Neg(Num(2.0)),
    Num(-3.0)
)
g = Graph(math)
g.pprint()
g.reduce_neg()
g.pprint()

