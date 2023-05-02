##kdtree
d = 2
class Edge:
    def __init__(self,x=0,y=0,level=0):
        self.pos = [x,y]
        self.level = level
        self.left = None
        self.right = None


    def search(self,key,level):
        assert isinstance(key, Edge)
        if(self is None): return None
        if(self.pos[0]==key.pos[0] and self.pos[1] == key.pos[1]): return self
        if(self.pos[level]>key.pos[level]):
            return self.left.search(key,(level+1)%d)
        else:
            return self.right.search(key,(level+1)%d)

