import math
import contextlib
import weakref
import numpy as np
from dezero import Function


class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y

    def backward(self, gy):
        x = self.inputs[0].data
        gx = gy*np.cos(x)
        return gx


def sin(x):
    return Sin()(x)


def my_sin(x, threshold=0.0001):
    y = 0
    for i in range(100000):
        c = (-1)**i/math.factorial(2*i+1)
        t = c*x**(2*i+1)
        y = y+t
        if abs(t.data) < threshold:
            break
        return y


def square(x):
    f = Square()
    return f(x)


def exp(x):
    f = Exp()
    return f(x)


class Square(Function):
    def forward(self, x):
        return x**2

    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2*x*gy
        return gx


class Exp(Function):
    def forward(self, x):
        return np.exp(x)

    def backward(self, gy):
        x = self.inputs.data
        gx = np.exp(x)*gy
        return gx


def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data-eps)
    x1 = Variable(x.data+eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data-y0.data)/(2*eps)


def square(x):
    f = Square()
    return f(x)


def exp(x):
    f = Exp()
    return f(x)


x = Variable(np.array(0.5))
a = square(x)
b = exp(a)
y = square(b)

y.backward()
print(x.grad)
