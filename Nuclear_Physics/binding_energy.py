#Binding energy calculator.
import numpy as np


#Define the function for easy use throughout the programme.
def binding_energy(A, Z):	#Binding energy function.
    N = A - Z
    v = a_v * A
    s = a_s * A**(2.0/3.0)
    c = a_c * Z**2.0 / A**(1.0/3.0)
    a = a_a * (N - Z)**2.0 / A
    return v - s - c - a + delta

if __name__ == "__main__":
    #Asking the user to decide how to proceed for the variable definitions.
    ans = input("Input paramaters? y/n")

    if ans == "y":  #Allow user to set all parameters.
        a_v = float(input("Input a_v:"))
        a_s = float(input("Input a_s:"))
        a_c = float(input("Input a_c:"))
        a_a = float(input("Input a_a:"))
        delta = float(input("Input delta:"))
    else:   #Set parameters automatically.
        print("Using preset parameters")
        a_v = 15.56; a_s = 17.23; a_c = 0.7; a_a = 23.28
        delta = float(input("Input delta:"))
        print("""a_v = {}
a_s = {}
a_c = {}
a_a = {}
delta = {}""" .format(a_v, a_s, a_c, a_a, delta))


    #Take the values of each nuclear variable from user.
    A = float(input("Enter A:"))
    #There is a range setting for Z so a range of binding energies can be
    #calculated. (This is useful to me in my studies.) For a single binding energy
    #calculation, enter Zlo=n, Zup=n+1.
    Zlo = float(input("Enter minimum Z:"))
    Zup = float(input("Enter maximum Z:"))
    Z = np.arange(Zlo, Zup, 1)


    #ERROR CHECK: Check for Zup<Zlo.
    if Zup <= Zlo:
        print("Zup <= Zlo. Program failed to execute correctly. Exiting")
        exit(1)


    file = open("binding_energies.txt", 'w')
    for i in Z:
        print("Binding energy for Z = {} is B = {} MeV" .format(i, '%.5f' \
            %binding_energy(A, i)))
        file.write(str(binding_energy(A, i)) + "\n")
    file.close()