from . import PeriorTree
import numpy as np
def test():
    N=int(1e4)
    ps = np.random.rand(N,3)
    rs= np.random.rand(N,3)*.05
    bbox=np.stack([np.zeros(3),np.ones(3)])
    t=PeriorTree(bbox)
    for i in range(N):
        p = ps[i]
        r = rs[i]
        t.add(p,r,i)
    pm=(bbox[0]+bbox[1])/2
    rm=np.ones(3)*.25
    a=t.query(pm,rm)
    #TODO: check correctedness
if __name__=='__main__':
    test()