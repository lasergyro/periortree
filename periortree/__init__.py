import numpy as np
import cppyy
import os
cppyy.add_include_path(f"{os.environ['CONDA_PREFIX']}/include/periortree")

cppyy.include('periortree/rtree.hpp')
cppyy.include('periortree/point.hpp')
cppyy.include('periortree/query.hpp')
cppyy.include('periortree/boundary_conditions.hpp')
std=cppyy.gbl.std
perior=cppyy.gbl.perior

class PeriorTree:
    _p=perior.point['double',3]
    _r=perior.rectangle[_p]
    _b=perior.cubic_periodic_boundary[_p]
    _v=std.pair[_r,std.size_t]
    _t=perior.rtree[_v,perior.quadratic[6,2],_b]
    _q=perior.query.query_intersects_box[_p]
    def __init__(self,bbox):
        self._tree=self._t(self._b(self._p(bbox[0]),self._p(bbox[1])))
    def add(self,p,r,i):
        self._tree.insert(self._v(self._r(self._p(p),self._p(r)),i))
    def query(self,p,r):
        rq=self._r(self._p(p),self._p(r))
        q=self._q(rq)
        a = std.vector[self._v]()
        oi = std.back_inserter(a)
        self._tree.query(q,oi)
        return np.fromiter((b.second for b in a),dtype=int)