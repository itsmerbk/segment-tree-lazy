class LazySegTree:
    def __init__(self, arr):
        self.n = len(arr); self.tree = [0]*(4*self.n); self.lazy = [0]*(4*self.n)
        self._build(arr, 1, 0, self.n-1)
    def _build(self, a, v, tl, tr):
        if tl == tr: self.tree[v] = a[tl]; return
        tm = (tl + tr)//2
        self._build(a, v*2, tl, tm); self._build(a, v*2+1, tm+1, tr)
        self.tree[v] = self.tree[v*2] + self.tree[v*2+1]
    def _push(self, v, tl, tr):
        if self.lazy[v]:
            tm = (tl + tr)//2
            for child, seg in [(v*2, tm-tl+1), (v*2+1, tr-tm)]:
                self.tree[child] += self.lazy[v]*seg; self.lazy[child] += self.lazy[v]
            self.lazy[v] = 0
    def add(self, l, r, val, v=1, tl=0, tr=None):
        if tr is None: tr = self.n - 1
        if l > r: return
        if l == tl and r == tr: self.tree[v] += val*(tr-tl+1); self.lazy[v] += val; return
        self._push(v, tl, tr); tm = (tl + tr)//2
        self.add(l, min(r, tm), val, v*2, tl, tm); self.add(max(l, tm+1), r, val, v*2+1, tm+1, tr)
        self.tree[v] = self.tree[v*2] + self.tree[v*2+1]
    def query(self, l, r, v=1, tl=0, tr=None):
        if tr is None: tr = self.n - 1
        if l > r: return 0
        if l == tl and r == tr: return self.tree[v]
        self._push(v, tl, tr); tm = (tl + tr)//2
        return self.query(l, min(r, tm), v*2, tl, tm) + self.query(max(l, tm+1), r, v*2+1, tm+1, tr)

if __name__ == "__main__":
    st = LazySegTree([1, 2, 3, 4, 5]); st.add(1, 3, 10)
    assert st.query(0, 4) == 45 and st.query(1, 2) == 25
    print("[PASS] 005_segment_tree_lazy")
