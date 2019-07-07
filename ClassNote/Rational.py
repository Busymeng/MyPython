# simple rationalNumber class
# wfp, 10/20/07
# wfp updated Py3, naming 4/2/13

def gcd(a,b):
    if not a>b:
        a,b=b,a
    while b!=0:
        rem = a%b
        a,b = b,rem
    return a

def lcm (a,b):
    return (a*b//gcd(a,b))

class Rational(object):
    def __init__(self,numer,denom=1):
        print('in construct')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        print('in str')
        return str(self.numer)+'/'+str(self.denom)

    def __repr__(self):
        print('in repr')
        return self.__str__()

    def __add__(self,f):
        print('in add')
        if type(f) == int:
            f = Rational(f)
        the_lcm = lcm(self.denom,f.denom)
        the_sum = (the_lcm//self.denom * self.numer)+(the_lcm//f.denom * f.numer)
        return Rational(the_sum,the_lcm)

    def __radd__(self,f):
        print('in radd')
        return self.__add__(f)

    def __iadd__(self,val):
        self = self.__add__(val)

    def __sub__(self,f):
        the_lcm  = lcm(self.denom,f.denom)
        the_diff = (the_lcm//self.denom * self.numer)-(the_lcm//f.denom * f.numer)
        return Rational(the_diff,the_lcm)

    def __eq__(self,f):
        f1 = self.reduce()
        f2 = f.reduce()
        return f1.numer == f2.numer and f1.denom == f2.denom

    def __float__(self):
        return float(self.numer)/self.denom

    def __coerce__(self,val):
        print('in coerce')

    def reduce(self):
        the_gcd = gcd(self.numer,self.denom)
        return Rational(self.numer//the_gcd,self.denom//the_gcd)

