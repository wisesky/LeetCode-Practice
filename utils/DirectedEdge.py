#------------------------------------------------------------------------------
# Immutable weighted directed edge
#------------------------------------------------------------------------------

class DirectedEdge:
    def __init__(self, v, w, weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def weight(self):
        return self.weight

    def fr(self):
        return self.v

    def to(self):
        return self.w

    def __str__(self):
        return f"{self.v} -> {self.w} weight: {self.weight}"


if __name__=='__main__':
    diedge = DirectedEdge(0, 1, 3)
    print(diedge)