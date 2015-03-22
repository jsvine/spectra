class Scale(object):
    kwargs = ("from_num", "to_num", "map_func")
    def __init__(self, colors, domain=None, mapping=None):
        self.colors = colors
        n = len(colors)
        self._domain = domain or [ float(x) / (n - 1) for x in range(n) ]
        self._mapping = mapping or (lambda x: x)
#        self.from_num = from_num
#        self.to_num = to_num
#        self.map_func = map_func
        
    def __call__(self, num):
        if num < self._domain[0] or num > self._domain[-1]:
            msg = "Number ({0}) not in domain ({1} -> {2})."
            raise ValueError(msg.format(num, self._domain[0], self._domain[-1]))
        f = self._mapping
        segments = zip(self._domain[:-1], self._domain[1:])
        for i, seg in enumerate(segments):
            x0, x1 = seg
            if num >= x0 and num <= x1:
                num_range = f(x1) - f(x0)
                prop = float(f(num) - f(x0)) / num_range
                return self.colors[i].blend(self.colors[i+1], prop)
    
    def domain(self, domain):
        return self.__class__(self.colors, domain, self._mapping)
    
    def mapping(self, mapping):
        return self.__class__(self.colors, self._domain, mapping)
    
    def colorspace(self, space):
        new_colors = [ c.to(space) for c in self.colors ]
        return self.__class__(new_colors, self._domain, self._mapping)

    def range(self, count):
        if count <= 1:
            raise ValueError("Range size must be greater than 1.")
        dom = self._domain
        distance = dom[-1] - dom[0]
        props = [ self(dom[0] + distance * float(x)/(count-1))
            for x in xrange(count) ]
        return props
