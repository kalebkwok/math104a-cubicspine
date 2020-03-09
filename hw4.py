import numpy as numpy
import scipy
import naturalSpline
import math


def make_spine(xs,as,bs,cs,ds):
    result = np.zeros(len(xs))
    for i in range(len(xs))
        result[i] = as[i]*(xs[i]-xs[-1])+bs[i]*(xs[i]-xs[-1])+cs[i]*np.power((xs[i]-xs[-1]),2)+ds[i]*(np.power((xs[i]-xs[-1]),3))

    return result



def get_coeffs(fs,zs):
    a = fs
    b = zs

    for i in range(len(fs)):
        c[i]=3*(fs[i+1]-fs[i])-2*zs[i]-zs[i+1]
    for r in range(len(fs)):
        d[r]=2*(y[r]-y[r+1])+zs[i]+zs[i+1]

    return(a,b,c,d)




def get_tridiag(xs,fs):
#caluculate for a b c d coefficient\
    h = np.zeros(len(xs)-1)
    for i in range(1,len(xs))
        h[i-1]=xs[i]-xs[i-1]
    # we solve for a b c d based on code in our text book.
    a = h[1:-2]
    b = np.zeros(len(h)-1)
    for i in range(len(b)):
        b[i]=2*(h[i]+h[i+1])
    c = h[1:-2]
    d = np.zeros(len(d))
    for i in range(len(d)):
        d[i]=np.negative(6)/h[i]*(fs[i+1]-fs[i])+6/h[i+1]*(fs[i+2]-fs[i+1])

    return (a,b,c,d)


def tridiag(as,bs,cs,ds):
    m = np.zeros(len(as))
    l = np.zeros(len(as))
    m[1]=as[1]
    for j in range(len(m)):
        l[j] = c[j]/m[j]
        m[j+1]=as[j+1]-l[j]*b[j]
    
    y = np.zeros(len(ds))
    for k in range(2,len(y)):
        y[k]=ds[k]-l[k-1]*y[k-1]
    
    r = range(len(ds))
    x[r] = y[r]/m[r]

    for p in range(len(m),1)
        x[p] = (y[p]-bs[p]*x[p+1])/m[p]
    
    return x
         


def return_spine(xs,fs):
    (mas,mbs,mcs,mds)= get_tridiag(xs,fs)
    zs= tridiag(mas,mbs,mcs,mds)
    (as,bs,cs,ds)=get_coeffs(xs,fs,zs)
    return make_spine(zs,as,bs,cs,ds)

