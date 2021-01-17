#Nuclear Radii
#This programme estimates the radii of a nucleus based on the atomic number.


#Making the calculation into a funtion in case I need to expand the programme.
def nuclear_radii(A):
    return A**(1/3)

if __name__ == "__main__":
    #Adding ability to calculate ratio of atomic radii for past paper exam
    #question.
    ans = input("Are you calculating a radii ratio, y/n?:")
    if ans == "y":  #Calculate a ratio, just as the user says! :)
        
        #I like to loop for expandability in the future.
        A = []
        for i in range(2):
            a = float(input("Input an A value:"))
            A.append(a)
        print("The ratio of radii of nuclei A = {} to A = {} is: {}"
        .format(A[0], A[1], '%.3f' %(nuclear_radii(A[0]) / nuclear_radii(A[-1]))))
   
   else:   #Just calculate a radius.
        
        A = float(input("Input an A value:"))
        print("The radii of nuclei A = {} is: R = {} fm" .format(A, '%.3f' \
            %nuclear_radii(A)))