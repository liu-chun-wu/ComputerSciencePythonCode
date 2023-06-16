import pylab as pl

def f(x):
    return pl.maximum( abs(x*pl.sin(x)),abs(x*pl.cos(x)) )
def g(x):
    return pl.minimum( abs(x*pl.sin(x)),abs(x*pl.cos(x)) )
a,b,n=-2*pl.pi,2*pl.pi,10000
xs=pl.linspace(a,b,n)
ys1=f(xs)
ys2=g(xs)
pl.plot(xs,ys1)
pl.plot(xs,ys2)
pl.grid()
pl.xlabel("X")
pl.ylabel("Y")
pl.title("f(x)=max(abs(x sin(x)),abs(x cos(x))),g(x)=min(abs(x sin(x)),abs(x cos(x)))")
pl.show()