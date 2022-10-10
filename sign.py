from elipt import ECurve
import random


class DSignature:
    # p - int, модуль эллиптической кривой
    # a, b - int, коэффициенты эллиптической кривой
    # q - int, порядок точки P
    # p_x, p_y - int, координаты точки Р
    def __init__(self, p, a, b, q, G_x, G_y):
        self.G = ECurve(G_x, G_y, a, b, p)
        self.q = q
        self.a = a
        self.b = b
        self.p = p

    def find_q(G,a,b,p):
        r=ECurve(1,1,a,b,p)
        i=0
        while r!=float('inf'):
            i+=1;
            r=i*G
        return i

    def points_generate(LHS,RHS,a,b,p):
        points=[]
        count=0
        for i in range(0,p):
            for j in range(0,p):
                if(LHS[1][i]==RHS[1][j]):
                    count+=1
                    points.append(ECurve(LHS[0][i],RHS[0][j],a,b,p))
        return count,points

    def polynomial(LHS,RHS,a,b,p):
        for i in range(0,p):
            LHS[0].append(i)
            RHS[0].append(i)
            LHS[1].append((i*i*i + a*i + b)%p)
            RHS[1].append((i*i)%p)
        return LHS,RHS

    def sign(self, message, private_key, k=0):
        h=message
        r=0
        s=0
        while (r==0)or(s==0):
            if k==0:
                k=random.randint(1,self.q-1)
            P=k*self.G
            r=P.x%self.q
            s=(k*h+r*private_key)%self.q
            return r,s

    def verify(self, message, sign, public_key):
        h=message
        if not((0<sign[0])and(sign[1]<self.q)):
            print ("не выполняются условия 0<r, s<q");
        u1=(sign[1]*pow(h,self.q-1-1))%self.q
        u2=((-sign[0])*pow(h,self.q-1-1))%self.q                                                                             
        u1G=u1*self.G
        u2Ya=u2*public_key
        P=u1G+u2Ya
        if P==float('inf'):
            return False
        else:
            if P[0]%self.q==sign[0]:
                return True
            else:
                return False

    def gen_keys(self):
        d = random.randint(1, self.q - 1)
        q_point = d * self.G
        return d, q_point