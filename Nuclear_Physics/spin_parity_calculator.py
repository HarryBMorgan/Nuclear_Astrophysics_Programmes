#This programme prints the ground state energy level structure of a nucleus.
#The structure is based on the Wood-Saxon well with spin-orbit splitting.
#------------------------------------------------------------------------------
#Import libraries that help the programme run.
from numpy import loadtxt   #Used to get data from txt file.
from fractions import Fraction  #Used for displaying output nicely.


#___Functions of the programme___


#___Main___
if __name__ == "__main__":
    #Create dictionary of l numbers.
    l = {0:"s", 1:"p", 2:"d", 3:"f", 4:"g", 5:"h", 6:"i", 7:"j"}
    for i in l:
        print("{}-level, l = {}" .format(l[i], i))

    #
    j = loadtxt("wood_saxon_so_energy_levels.txt")[:, 2]
    for i in j:
        print(Fraction(int(i*2), 2))