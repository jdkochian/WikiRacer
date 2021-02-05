import wikipedia

class NodeData:
    dist = 0
    bkptr = wikipedia.page("wikipedia")

    def __init__(self, d, bk):
        self.dist = d
        self.bkptr = bk
