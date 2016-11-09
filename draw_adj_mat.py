from collections import deque
from PIL import Image
import sys

class Graph(object):
    def __init__(self, adjmat):
        self.n = len(adjmat)
        self.adjmat = adjmat
        self.degree = [sum(row) for row in self.adjmat]

    def sort_by_degree(self):
        v_and_deg = zip(range(self.n), self.degree)
        v_and_deg.sort(key=lambda x: x[1], reverse=True)
        vv = [x[0] for x in v_and_deg]
        self.adjmat = [[self.adjmat[v][w] for v in vv] for w in vv]

    def show(self):
        img = Image.new('RGB', (self.n*3, self.n*3), "white")
        pixels = img.load()
        
        for i in range(self.n):
            for j in range(self.n):
                if self.adjmat[i][j]:
                    for k in range(3):
                        for l in range(3):
                            colour = (0,0,0)
                            if k==2 or l==2:
                                colour = (80,80,80)
                            if (k==2 and i%10==9) or (l==2 and j%10==9):
                                colour = (150,150,150)
                            pixels[i*3+k, j*3+l] = colour

        img.show()

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
    g.sort_by_degree()
    g.show()
