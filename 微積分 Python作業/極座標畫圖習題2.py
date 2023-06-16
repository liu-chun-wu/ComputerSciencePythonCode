import pylab
from numpy import *
angs=linspace(0,pi*10,2000)
rs=sin(2.3*angs)**2+cos(2.3*angs)**4
pylab.polar(angs,rs,lw=3,color='g')
pylab.title("graph of sin(2.3x)^2+cos(2.3x)^4 for x in [0,10pi]",color='r')
pylab.show()
