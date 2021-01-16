#Nuclear Radii
#This programme estimates the radii of a nucleus based on the atomic number.


#Making the calculation into a funtion in case I need to expand the programme.
def R(A):
    return A**(1/3)


#Get the value for A.
A = float(input("Input the A value of the nuclei:"))

print("The radii =", '%.3f' %R(A), "fm")