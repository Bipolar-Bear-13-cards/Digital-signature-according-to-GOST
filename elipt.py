class ECurve:
    def __init__(self, x=0, y=0, a=0, b=0, p=0, is_polynomial_basis=False):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.p = p
        self.pol_basis = is_polynomial_basis

    def __rmul__(self, other):
        if other==1:
            return self
        else:
            if self.y==0:
                return float('inf')
            k=((3*self.x*self.x+self.a)*pow(2*self.y,self.p-1-1))%self.p
            x3=(k*k-2*self.x)%self.p
            r = ECurve(x3,(k*(self.x-x3)-self.y)%self.p,self.a,self.b,self.p)
            for i in range (3,other+1):
                if self.x==r.x:
                    return float('inf')
                k=((r.y-self.y)*pow(r.x-self.x,self.p-1-1))%self.p
                x3=(k*k-self.x-r.x)%self.p
                r = ECurve(x3,(k*(self.x-x3)-self.y)%self.p,self.a,self.b,self.p)
            return r
    
    def __add__(self, other):
        if (self==float('inf'))or(other==float('inf')):
            return float('inf')
        k=((other.y-self.y)*pow(other.x-self.x,self.p-1-1))%self.p
        x3=(k*k-self.x-other.x)%self.p
        other = (x3,(k*(self.x-x3)-self.y)%self.p)
        return(other)


