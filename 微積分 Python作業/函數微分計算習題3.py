import pylab as pl
def h(x):
    return (1.2732)*pl.sin(2*x)+(0.4244)*pl.sin(6*x)+(0.25465)*pl.sin(10*x)+(0.18189)*pl.sin(14*x)+(0.14147)*pl.sin(18*x)
def dh(x,delta_x):
    return (h(x+delta_x)-h(x))/delta_x
a,b,n=-1*pl.pi,pl.pi,10000
delta_x=(b-a)/(n-1)
xs=pl.linspace(a,b,n)
ys1=h(xs)
ys2=dh(xs,delta_x)
pl.plot(xs,ys1,label="h(x)")
pl.plot(xs,ys2,label="h'(x)")
pl.grid()
pl.xlabel("X")
pl.ylabel("Y")
pl.title("sawtooth function approximation and derivative")
pl.legend(loc=4)
pl.show()