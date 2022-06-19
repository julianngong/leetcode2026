class UnionFind:
    def __init__(self, size): #UnionFind is just a list with each element being the value of the root node
        self.roots = []
        for i in range(size):
            self.roots.append(i)
    
    def findroot(self,x): #return the xth element of the root node list
        return(self.roots[x])
    
    def union(self,x,y):
        if (self.roots.count(x) <= self.roots.count(y)): #if the size of one group is less than the other, then add the root of the smaller one as the child of the bigger one
            self.roots = [self.roots[y] if elem==self.roots[x] else elem for elem in self.roots] # this list comprehension means replace all elements in self.roots which are equal to self.roots[x] with self.roots[y]
        else:
            self.roots = [self.roots[x] if elem==self.roots[y] else elem for elem in self.roots]
    
    def connected(self,x,y): #return yes if the two elements are connected at all
        return(self.roots[x]==self.roots[y])
    
    def getroots(self): #return the roots
        return(self.roots)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = UnionFind(len(isConnected[0])) #make new disjoint union find
        for i in range(len(isConnected[0])):
            for j in range(i+1,len(isConnected[0])):
                if(isConnected[i][j] == 1):
                    provinces.union(i,j) #connect up all the elements which should be conneted.
        roots = provinces.getroots()
        return(len(set(roots))) #set makes a list containing only each unique element.
                    
