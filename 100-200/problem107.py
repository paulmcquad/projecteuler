#problem107.py
#http://inanemathgeek.wordpress.com/2012/10/15/euler-107-back-to-python/
from operator import itemgetter

class DisjointSet (dict):
    def add(self, item):
        self[item] = item
    
    def find(self, item):
        parent = self[item]
        while self[parent] != parent:
            parent = self[parent]
        self[item] = parent
        return parent
    
    def union(self, item1, item2):
        self[item2] = self[item1]

def kruskal (nodes, edges):
    forest = DisjointSet ()
    mst = []
    for n in nodes:
        forest.add (n)
    sz = len(nodes)-1
    for e in sorted (edges, key = itemgetter(2)):
        n1, n2, _ = e
        t1 = forest.find (n1)
        t2 = forest.find (n2)
        if t1 != t2:
            mst.append (e)
            sz -= 1
            if sz == 0:
                return mst
            forest.union (t1, t2)

def convert2Edges (m):
    e = []
    for i in range (1, len(m)):
        for j in range (0,i):
            if m[i][j] != 0:
                e.append ([str(i), str(j), m[i][j]])
    return e

def generateNodes (m):
    n = []
    for i in range(0, len(m)):
        n.append(str(i))
    return n

def calcWeight(e):
    w = 0
    for i in e:
        w += i[2]
    return w

def generateMatrix ():
    m = []
    f = open ("data/pb107network.txt", "r")
    for line in f.read().split ('\n'):
        m.append (line.split (","))
    f.close()
    num = len(m)
    for i in range (0, num-1):
        for j in range (0, num-1):
            if m[i][j] == '-' or m[i][j] == '-\r':
                m[i][j] = '0'
            m[i][j] = int (m[i][j])
    m.pop()
    return m
    
if __name__=="__main__":
    m = generateMatrix()
    e = convert2Edges (m)
    n = generateNodes (m)
    e1 = kruskal (n,e)
    w1 = calcWeight (e)
    w2 = calcWeight (e1)
    print ("Original weight: " + str (w1))
    print ("New weight: " + str (w2))
    print ("Difference: "+ str (w1-w2))
