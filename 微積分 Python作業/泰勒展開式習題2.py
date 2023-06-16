import pylab,numpy
def factorial(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
def taylor_poly(n,x):
    s=0
    for k in range(1,n+1):
        s+=((-1)**pylab.floor((k*2-2)/2) * x**(k*2-2)) / factorial(k*2-2)
        s+=((-1)**pylab.floor((k*2-1)/2) * x**(k*2-1)) / factorial(k*2-1)
    return s
a=0
b=numpy.pi*3
m=100
xs=numpy.linspace(a,b,m)
n=10
for i in range(1,n+1):
    ys=taylor_poly(i,xs)
    pylab.plot(xs,ys,label="P"+str(i*2-1))

pylab.plot(xs,numpy.cos(xs)+numpy.sin(xs),label="sin(x)+cos(x)")
pylab.title("Taylor polynomials with different orders for sin(x)+cos(x)")
pylab.legend(loc='upper right')
pylab.grid()
pylab.xlabel("X")
pylab.ylabel("Y")
pylab.ylim(-2,2)
pylab.show()