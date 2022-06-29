import wikipedia

class NodeData:
    """
    A node corresponding to an article on wikipedia and associated data 

    `dist`: How many articles away this article is from the source
    `bkptr`: Backpointer, the closest link to the source article 
    """
    dist = 0
    bkptr = wikipedia.page("wikipedia")

    def __init__(self, d, bk):
        self.dist = d
        self.bkptr = bk
