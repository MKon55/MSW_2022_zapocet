#pass

def forward_derivate(f, x0, h):
    return (f(x0+h) - f(x0))/h

def backward_derivate(f, x0, h):
    return (f(x0) - f(x0-h))/h

def central_derivate(f, x0, h):
    return (f(x0+h) - f(x0-h))/(2*h)

def forward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0))/h_adaptive

def backward_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0) - f(x0-h_adaptive))/h_adaptive

def central_derivate_adaptive(f, x0, h_adaptive):
    return (f(x0+h_adaptive) - f(x0-h_adaptive))/(2*h_adaptive)

f = lambda x: x**2 + 2
x0 = 2
h = 0.1
h_adaptive = float(input("Zadejte adaptive krok: "))

print(forward_derivate(f, x0, h))
print(backward_derivate(f, x0, h))
print(central_derivate(f, x0, h))

print(forward_derivate_adaptive(f, x0, h_adaptive))
print(backward_derivate_adaptive(f, x0, h_adaptive))
print(central_derivate_adaptive(f, x0, h_adaptive))