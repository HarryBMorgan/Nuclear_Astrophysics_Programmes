#Binding energy calculator.
import numpy as np


def B(A, Z):	#Binding energy function.
    N = A - Z
    v = a_v * float(A)
    s = a_s * A**(2.0/3.0)
    c = a_c * Z**2.0 / A**(1.0/3.0)
    a = a_a * (N - Z)**2.0 / A
    return v - a - c - a + delta


ans = input("Input paramaters? y/n")

if ans == "y":
    a_v = float(input("Input a_v:"))
    a_s = float(input("Input a_s:"))
    a_c = float(input("Input a_c:"))
    a_a = float(input("Input a_a:"))
    delta = float(input("Input delta:"))
else:
    print("Using preset parameters")
    a_v = 15.56; a_s = 17.23; a_c = 0.7; a_a = 23.28
    delta = float(input("Input delta:"))
    print("""a_v = {}
a_s = {}
a_c = {}
a_a = {}
delta = {}""" .format(a_v, a_s, a_c, a_a, delta))


A = float(input("Enter A:"))
Zlo = float(input("Enter minimum Z:"))
Zup = float(input("Enter maximum Z:"))
Z = np.arange(Zlo, Zup, 1)


file = open("binding_energies.txt", 'w')
for i in Z:
    file.write(str(B(A, i)) + "\n")
file.close()