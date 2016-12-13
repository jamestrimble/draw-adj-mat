import matplotlib.pyplot as plt
import networkx as nx
import sys

class Graph(object):
    def __init__(self, adjmat):
        self.n = len(adjmat)
        self.adjmat = adjmat
        self.degree = [sum(row) for row in self.adjmat]

    def show(self):
        G = nx.Graph()
        for i in range(self.n):
            G.add_node(i)
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.adjmat[i][j]:
                    G.add_edge(i, j)
        nx.draw_networkx(G, pos=nx.circular_layout(G))
        plt.show()

def read_instance(lines):
    lines = [line.strip().split() for line in lines]
    p_line = [line for line in lines if line[0]=="p"][0]
    e_lines = [line for line in lines if line[0]=="e"]
    n = int(p_line[2])
    print "Number of vertices:", n
    print "Number of edges:", len(e_lines)
    adjmat = [[False] * n for _ in range(n)]
    for e in e_lines:
        v, w = int(e[1])-1, int(e[2])-1
        if v==w:
            print "Loop detected", v
        if adjmat[v][w]:
            print "Duplicate edge", v, w
        adjmat[v][w] = adjmat[w][v] = True
    print "Finished reading instance."
    return Graph(adjmat)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = read_instance([line for line in f.readlines()])
    g.show()
