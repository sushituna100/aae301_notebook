'''
Author: Shishir Tumma
Assignment: HW02
Date: 9/11/25
'''

'''
Question 6
Find a constant alpha such that 1 is perpendicular to 1 + alpha*t
'''
#Import sympy for the math
import sympy as sp

#Define the variables
t, a =  sp.symbols('t alpha', real=True)

#Intialize the functions
f = 1
g = 1 + a*t

#Calculate the innerproduct
inner_prod = sp.integrate(f*g, (t, 0, 2*sp.pi))
print(inner_prod)
#Solve for alpha
alpha = sp.solve(sp.Eq(inner_prod, 0), a)

#Get first element of array
alpha_val = alpha[0]

#Verify
print("Alpha: " + str(alpha_val))

#Verify once more by doing the inner product
inner_prod_check = inner_prod.subs(a, alpha_val).simplify()

#if-else structure for checking whether it is in the family
if inner_prod_check == 0:
    print("Inner Product with alpha is equal to 0, so it does belong in the family")
    print("Inner product with alpha: " + str(inner_prod_check)  + "\n")
else:
    print("Inner Product with alpha doesn't equal 0, so it doesn't belong in the family")
    print("Inner product with alpha: " + str(inner_prod_check) + "\n")


'''
Question 7
A) Show that cos(t) is orthogonal to sin(t) in the Lebesgue^2(0, 2PI) space
B) Show that it is not orthogonal in the Lebesgue^2(0,1)
'''

def check_orthogonal(f, g, start, end):
    '''
    Takes in two functions/vectors f and g 
    and calculates if they are orthogonal or not using sppy
    
    Paramters:
    f : (equation) The first function
    g : (equation) The second function
    start : (float) The lower bounds of the integral
    end : (float) The upper bounds of the integral
    '''
    #Initialize the sympy variables
    t=  sp.symbols('t alpha', real=True)

    #Calcualtes the inner product of the paramters
    inner_prod = sp.integrate(f*g, (t, start, end))
    
    #Selection structure for whether or not it is orthogonal
    if inner_prod == 0:
        print(f"The funtions {f} and {g} are orthogonal because their inner product equals one\n")
    else:
        print(f"The functions {f} and {g} are not orthogonal because their inner product doesn't equal zero\n")

#Initialize the two functions in question
func1, func2 = sp.cos(t), sp.sin(t)

#Print out the results from the function in the right format
print("For Lebesgue^2(0,2pi): ")
check_orthogonal(func1, func2, 0, 2*sp.pi)

print("For Lebesgue^2(0,1): ")
check_orthogonal(func1, func2, 0, 1)

